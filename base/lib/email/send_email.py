import os
import requests

def send_simple_message(to, subject, text):
	return requests.post(
		"https://api.mailgun.net/v3/noreply.tushgaurav.in/messages",
		auth=("api", os.environ['MAILGUN_API']),
		data={"from": "Tushar Gaurav <tushar@noreply.tushgaurav.in>",
			"to": [to, "tushar@noreply.tushgaurav.in"],
			"subject": subject,
			"text": text})