﻿'''Create tele_bot via https://t.me/BotFather'''


import requests
from translator_bot import find_matched_sentences, user, message, sentences


token = "5692827918:AAFGwWI12tXI6jQvNmHNOfMCudgyWCeH04U"
root_url = "https://api.telegram.org/bot"

positive_codes = [200, 201, 202, 203, 204]


def get_bot_info(token):
	
	#check the connection to Telegram chat t.me/TestAndrBeDevBot 
	
	url = f"{root_url}{token}/getMe"
	response = requests.get(url)
	response.raise_for_status() 
	bot_info = response.json()
	return bot_info


def get_updates(token):
	
	#This function return token of Telegram chat t.me/TestAndrBeDevBot
	
	url = f"{root_url}{token}/getUpdates"
	response = requests.get(url)
	updates = response.json()
	if response.status_code in positive_codes:
		result = updates["result"][-1]
		chat_id = result.get("message").get("chat")["id"]
		return chat_id
	else:
		bad_result = f'bad request {response.status_code}'
		return bad_result


chat_id = get_updates(token) # get token from the function get_updates


def send_message(chat_id, text):
	
	#This function send message to Telegram chat t.me/TestAndrBeDevBot
	
	url = f"{root_url}{token}/sendMessage"
	response = requests.post(url, data={'chat_id': chat_id, "text": text})
	return response



#print(find_matched_sentences(user, message, sentences))
answer = find_matched_sentences(user, message, sentences)
# print(get_updates(token))
# print(get_bot_info(token))
print(send_message(chat_id, answer))
