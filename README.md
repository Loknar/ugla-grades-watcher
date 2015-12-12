# ugla-grades-watcher
Grades watcher script for students in University of Iceland who are impaitiently waiting for their grades.

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

## Requirements
You need to install [python 2.7 and pip](http://docs.python-guide.org/en/latest/starting/install/win/). You can setup notifications to your phone by creating a free [Slack](https://slack.com/) channel and setup the [android](https://play.google.com/store/apps/details?id=com.Slack&hl=en) or [IOS](https://itunes.apple.com/us/app/slack/id803453959) app on your phone.

Open Command Prompt (for windows) or Terminal (for Mac OS X or GNU/Linux) and navigate to the project folder. Install required python modules by typing the following:

	pip install -r requirements.txt

Copy `settings.example.config` to `settings.config` and edit it to your needs.

Run the watcher:

	python ugla_grades_watcher.py

For Slack notifications you need to create a slackbot and put the slackbot token in your `settings.config` file. Happy waiting for your grades.

## settings.config

### Login
Login settings.

#### ugla_login_provided
Set to true if you wish to save your login in the config for ease of use.

#### username
Your username.

#### password
Your password.

### Watch
Watch settings.

#### watch_forever
Set to true if you want the script to watch for new grades in your ugla.

#### log_to_terminal
Set to true if you want to see printed in your command promt / terminal when the script checks for changes.

#### interval
Amount of seconds between grades checks.

### Slack
Slack settings.

#### use_slackbot
Set to true if you're awesome and have a slack board with your friends and have access to a slackbot on it.

#### act_like_robot
Makes your robot act like one.

#### slackbot_token
Your slackbot token.

#### slack_channel
Name of the channel you want the slackbot to send notifications to. Note that the slackbot must first be invited to this channel for this to work.
