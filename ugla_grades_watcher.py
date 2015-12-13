#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import time
import getpass
import datetime
import ConfigParser

import requests
from lxml import etree
from unidecode import unidecode
from prettytable import PrettyTable
from slackclient import SlackClient

from make_config import make_example_config

requests.packages.urllib3.disable_warnings() # don't ask
html_utf8_parser = etree.HTMLParser(encoding="utf-8")
settings_file = 'settings.config'
if not os.path.isfile(settings_file):
	make_example_config()
config = ConfigParser.RawConfigParser()
config.read(settings_file)

# SETTINGS
# ---------------------------------------------------------
UGLA_LOGIN_PROVIDED = config.getboolean('Login', 'ugla_login_provided')
USERNAME = config.get('Login', 'username')
PASSWORD = config.get('Login', 'password')
WATCH_FOREVER = config.getboolean('Watch', 'watch_forever')
LOG_TO_TERMINAL = config.getboolean('Watch', 'log_to_terminal')
INTERVAL = config.getint('Watch', 'interval')
USE_SLACKBOT = config.getboolean('Slack', 'use_slackbot')
ACT_LIKE_ROBOT = config.getboolean('Slack', 'act_like_robot')
SLACKBOT_TOKEN = config.get('Slack', 'slackbot_token')
SLACK_CHANNEL = config.get('Slack', 'slack_channel')
# ---------------------------------------------------------

HEADER = '''
+---------------------------------------------------------------------------------+
| .       .    .         .           .       .           .           .         .  |
|      .         .            .          .       .                                |
|            .         ..xxxxxxxxxx....               .       .             .     |
|    .             MWMWMWWMWMWMWMWMWMWMWMWMW                       .              |
|              IIIIMWMWMWMWMWMWMWMWMWMWMWMWMWMttii:        .           .          |
| .      IIYVVXMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWxx...         .           .  |
|     IWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMx..                    |
|   IIWMWMWMWMWMWMWMWMWMNWZACHWANDWOWENMWMWMWMWMWMWMWMWMWMWMWMWMx..        .      |
|    ""MWMWMWMWMWM"""""""".  .:..   ."""""MWMWMWMWMWMWMWMWMWMWMWMWMWti.           |
| .     ""   . `  .: . :. : .  . :.  .  . . .  """"MWMWMWMWMWMWMWMWMWMWMWMWMti=   |
|        . .   :` . :   .  .'.' '....xxxxx...,'. '   ' ."""YWMWMWMWMWMWMWMWMWMW+  |
|     ; . ` .  . : . .' :  . ..XXXXXXXXXXXXXXXXXXXXx.    `     . "YWMWMWMWMWMWMW  |
|.    .  .  .    . .   .  ..XXXXXXXXWWWWWWWWWWWWWWWWXXXX.  .     .     """""""   .|
|        ' :  : . : .  ...XXXXXWWW"   W88N88@888888WWWWWXX.   .   .       . .     |
|   . ' .    . :   ...XXXXXXWWW"    M88N88GGGGGG888^8M "WMBX.          .   ..   : |
|         :     ..XXXXXXXXWWW"     M88888WWRWWWMW8oo88M   WWMX.     .    :    .   |
|           "XXXXXXXXXXXXWW"       WN8888WWWWW  W8@@@8M    BMBRX.         .  : :  |
|  .       XXXXXXXX=MMWW":  .      W8N888WWWWWWWW88888W      XRBRXX.  .       .   |
|     ....  ""XXXXXMM::::. .        W8@889WWWWWM8@8N8W      . . :RRXx.    .       |
|         ``..."''  MMM::.:.  .      W888N89999888@8W      . . ::::"RXV    .  :   |
| .       ..''"''      MMMm::.  .      WW888N88888WW     .  . mmMMMMMRXx          |
|      ..' .            ""MMmm .  .       WWWWWWW   . :. :,miMM"""  : ""`    .    |
|   .                .       ""MMMMmm . .  .  .   ._,mMMMM"""  :  ' .  :          |
|               .                  ""MMMMMMMMMMMMM""" .  : . '   .        .      .|
|          .              .     .    .                      .         .           |
|.                 .                       .          .         .        .     .  |
+---------------------------------------------------------------------------------+
|                               ugla-grades-watcher                               |
|                  https://github.com/Loknar/ugla-grades-watcher                  |
+---------------------------------------------------------------------------------+
'''

def ugla_login_success(res):
	'''
	Usage:  success = ugla_login_success(res)
	Before: res is a requests response object
	After:  success is True if login was successful according to res, else False

	When ugla login is successful we get a 302 status code (redirect), the
	requests module handles redirects automaticly but we're provided with history
	of it, so we check the history to see if we got 302 status code.
	When ugla login is not successful we receive 200 status code.
	'''
	if len(res.history) > 0 and res.history[0].status_code == 302:
		return True
	return False

def uniden(mystring):
	'''
	Usage:  mystring2 = uniden(mystring)
	Before: mystring is a string, can be str or unicode
	After:  mystring2 is unidecoded mystring if mystring is unicode,
	        else mystring2 = mystring
	'''
	if isinstance(mystring, unicode):
		return unidecode(mystring)
	return mystring

def login_to_ugla():
	'''
	Usage:  session = login_to_ugla()
	Before: nothing
	After:  session is a requests session object with successful ugla login

	This function asks for login credentials or uses config supplied login based on
	your config file. It exits the program if login attempt failed.
	'''
	session = requests.session()
	session.get('https://ugla.hi.is/')
	if UGLA_LOGIN_PROVIDED:
		print 'Using provided ugla login.'
		username = USERNAME
		password = PASSWORD
	else:
		print 'Type in your ugla login.'
		username = str(raw_input('Username: '))
		password = getpass.getpass()
	data = {
		'username': username,
		'password': password
	}
	res = session.post('https://ugla.hi.is/', data=data)
	if not ugla_login_success(res):
		print 'Login failed, please try again.'
		sys.exit()
	print 'Login successful, checking grades ...\n'
	return session

def parse_course_table(table_dom):
	'''
	Usage:  table_info = parse_course_table(table_dom)
	Before: table_dom is an lxml etree object of the course table provided on ugla
	After:  table_info is an object with selected headers and list of matching columns
	        from the table_dom
	'''
	headers = [uniden(x.text) for x in table_dom[0][0]][:5]
	columns = []
	for stuff in table_dom[1]:
		number = uniden(stuff[0][0].text)
		name   = uniden(stuff[1][0].text)
		ects   = uniden(stuff[2].text)
		grade  = uniden(stuff[3].text)
		passed = uniden(stuff[4].text)
		column = (number, name, ects, grade, passed)
		columns.append(column)
	return {
		'headers': headers,
		'columns': columns
	}

def get_courses_info(session):
	'''
	Usage:  table_info, session = get_courses_info(session)
	Before: session is a successful requests ugla login session
	After:  fetched data from ugla,
	        table_info is an object with parsed courses info data from ugla,
	        session is an updated ugla login session

	The session must stay active or the login will time out.
	'''
	res = session.get('https://ugla.hi.is/vk/namskeidin_min.php?sid=40')
	res.raise_for_status()
	htmltext = res.content
	tree = etree.HTML(htmltext, parser=html_utf8_parser)
	course_table_xpath = './/*[@id="nf1_div"]/div/div/div[3]/div/table'
	table_dom = tree.find(course_table_xpath)
	table_info = parse_course_table(table_dom)
	return table_info, session

def pretty_table_string(table_info):
	'''
	Usage:  pretty_table = pretty_table_string(table_info)
	Before: table_info contains courses info from table on ugla
	After:  pretty_table is a string containing visually pleasing table with
	        info from table_info
	'''
	mytable = PrettyTable(table_info['headers'])
	for column in table_info['columns']:
		mytable.add_row(column)
	return str(mytable)

def watch_grades_forever(session, memory):
	'''
	Usage:  watch_grades_forever(session, memory)
	Before: session is a successful requests ugla login session,
	        memory is an object containint course ids as keys and grades as values
	After:  it never ends
	'''
	while True:
		time.sleep(INTERVAL)
		timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
		if LOG_TO_TERMINAL:
			print '\n%s - Checking grades status ...' % timestamp
		unchanged = True
		table_info, session = get_courses_info(session)
		pretty_table = pretty_table_string(table_info)
		for column in table_info['columns']:
			if column[0] not in memory:
				memory[column[0]] = None
			if memory[column[0]] != column[3]:
				msg = '%s\n%s Detected new grade for course %s %s\n```\n%s\n```\n' % (
					timestamp,
					':exclamation:',
					column[0],
					':exclamation:',
					pretty_table
				)
				print ''
				print msg
				slackbot_msg(msg)
				memory[column[0]] = column[3]
				unchanged = False
		if LOG_TO_TERMINAL and unchanged:
			print '--- no changes detected ---\n'

def slackbot_msg(message, channel=SLACK_CHANNEL):
	'''
	http://bulbapedia.bulbagarden.net/wiki/Slaking
	'''
	if ACT_LIKE_ROBOT:
		message = message.upper()
	sc = SlackClient(SLACKBOT_TOKEN)
	if sc.rtm_connect():
		sc.rtm_send_message(channel, message)
	else:
		print 'Warning: slackbot_msg() failed, invalid token?'

if __name__ == '__main__':
	print HEADER
	session = login_to_ugla()
	table_info, session = get_courses_info(session)
	print pretty_table_string(table_info)
	memory = {}
	for column in table_info['columns']:
		memory[column[0]] = column[3]
	if WATCH_FOREVER:
		print '\nWatching grades forever.\nPress Ctrl + C to stop ...\n'
	else:
		sys.exit()
	try:
		watch_grades_forever(session, memory)
	except KeyboardInterrupt:
		print 'Stopped.'
		sys.exit()
