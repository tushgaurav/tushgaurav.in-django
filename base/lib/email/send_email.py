import os
import requests

SELF_EMAIL = "tushar.gaurav416+debug@gmail.com"

def send_self(sender, subject, text):
	requests.post(
		"https://api.mailgun.net/v3/noreply.tushgaurav.in/messages",
		auth=("api", os.environ['MAILGUN_API']),
		data={"from": "django-site " + "<" + sender + ">",
			"to": [SELF_EMAIL, "tushar@noreply.tushgaurav.in"],
			"subject": "NEW MESSAGE :" + subject,
			"text": text})

def send_simple_message(to, subject, text, mail_self):
	if (mail_self):
		send_self(to, subject, text)
	return requests.post(
		"https://api.mailgun.net/v3/noreply.tushgaurav.in/messages",
		auth=("api", os.environ['MAILGUN_API']),
		data={"from": "Tushar Gaurav <tushar@noreply.tushgaurav.in>",
			"to": [to, "tushar@noreply.tushgaurav.in"],
			"subject": subject,
			"text": text})