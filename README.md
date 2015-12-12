# ugla-grades-watcher
Grades watcher script for students in University of Iceland who are impaitiently waiting for their grades.

## Requirements
You need to install [python 2.7 and pip](http://docs.python-guide.org/en/latest/starting/install/win/).
Open Command Prompt (for windows) or Terminal (for Mac OS X or GNU/Linux) and navigate to the project folder.
Install required python modules by typing the following:

	pip install -r requirements.txt

Copy `settings.example.config` to `settings.config` and edit it to your needs.
Run the watcher:

	python ugla_grades_watcher.py

Happy waiting for your grades.

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
