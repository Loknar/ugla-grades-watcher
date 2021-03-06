# ugla-grades-watcher
Grades watcher script for students in University of Iceland who are impatiently waiting for their grades.

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

## Requirements and setup
You need to install [python 2.7 and pip](http://docs.python-guide.org/en/latest/starting/install/win/). You can setup notifications to your phone by creating a free [Slack](https://slack.com/) channel and setup the [android](https://play.google.com/store/apps/details?id=com.Slack&hl=en) or [IOS](https://itunes.apple.com/us/app/slack/id803453959) app on your phone.

Open Command Prompt (for windows) or Terminal (for Mac OS X or GNU/Linux) and navigate to the project folder. Install required python modules by typing the following:

	pip install -r requirements.txt

Copy `settings.example.config` to `settings.config` and edit it to your needs.

Run the watcher:

	python ugla_grades_watcher.py

For Slack notifications you need to create a [slack bot](https://api.slack.com/bot-users) ([press here](https://my.slack.com/services/new/bot)) and put the bot API token in your `settings.config` file.

Happy waiting for your grades! :blush:

## settings.config

### Login

#### ugla_login_provided
Set to true if you save your login credentials in the config for ease of use. If it's false you will be prompted for username and password when you start the script.

#### username
Your username to ugla.hi.is, providing this is optional, see ugla_login_provided.

#### password
Your password to ugla.hi.is, providing this is optional, see ugla_login_provided.

### Watch

#### watch_forever
Set to true if you want the script to watch for new grades in your ugla. If it's false the script shuts down after checking your grades status once.

#### log_to_terminal
Set to true if you want to see printed in your command promt / terminal when the script checks for changes.

#### interval
Amount of seconds between grades checks. Please don't spam our poor Ugla, checking more frequently than once every minute is just rude.

### Slack

#### use_slackbot
Set to true if you're awesome and you have a slack board with your friends and have access to a slackbot on it.

#### act_like_robot
Makes your robot act like one.

#### slackbot_token
Your slack bot token.

#### slack_channel
Name of the channel you want the slackbot to send notifications to. Note that the slackbot must first be invited to this channel for this to work.
