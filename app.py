import random
from flask import Flask, request
from pymessenger.bot import Bot
import reply


app = Flask(__name__)
ACCESS_TOKEN='USE_YOUR_OWN_ACCESS_TOKEN'
VERIFY_TOKEN='USE_YOUR_OWN_TOKEN'
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def receive_message():
	if request.method == 'GET':
		# Toekn verification First
		token_sent = request.args.get("hub.verify_token")
		return verify_fb_token(token_sent)
	else:

		# receives messages sent by the user

		output = request.get_json()
		for event in output['entry']:
			messaging = event['messaging']
			for message in messaging:
				if message.get('message'):

					# Gets facebook user id in recipent_id to send back the response

					recipent_id = message['sender']['id']
					try:
						message_text = message["message"]["text"]
						reply = predict(message_text)
						send_message(recipent_id, reply)
					except:
						try:
							message_text = message["message"]['attachments']
							send_message(recipent_id, "no image please")
						except:
							send_message(recipent_id, "Sorry! I didn't get that")
	
	return "Message Processed"


# Token verification with facebook 

def verify_fb_token(token_sent):
	if token_sent == VERIFY_TOKEN:
		return request.args.get("hub.challenge")
	return 'Invalid verification token'

# sending message to the user

def send_message(recipent_id,response):	
	bot.send_text_message(recipent_id, response)
	return "success"

def predict(income_msg):
	return reply.classify(income_msg)

if __name__ == '__main__':
	app.run()