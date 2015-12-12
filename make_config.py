import ConfigParser

def make_example_config():
	config = ConfigParser.RawConfigParser()
	config.add_section('Login')
	config.add_section('Watch')
	config.add_section('Slack')
	config.set('Login', 'UGLA_LOGIN_PROVIDED', 'false')
	config.set('Login', 'USERNAME', 'myuser')
	config.set('Login', 'PASSWORD', 'mypass')
	config.set('Watch', 'WATCH_FOREVER', 'false')
	config.set('Watch', 'LOG_TO_TERMINAL', 'false')
	config.set('Watch', 'INTERVAL', '60')
	config.set('Slack', 'USE_SLACKBOT', 'false')
	config.set('Slack', 'ACT_LIKE_ROBOT', 'false')
	config.set('Slack', 'SLACKBOT_TOKEN', 'xoxp-7789698678-JHfF8jQpfdi5FJkhfoP3xcD2')
	config.set('Slack', 'SLACK_CHANNEL', 'ugla-grades-watch')
	with open('settings.example.cfg', 'wb') as configfile:
	    config.write(configfile)

if __name__ == '__main__':
	make_example_config()
