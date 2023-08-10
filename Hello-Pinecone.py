import os
import openai
import logging as log
from subprocess import call

log.basicConfig(filename='openai-history.log', encoding='utf-8', level=log.DEBUG)

# Load your API key from an environment variable or secret management service
openai.api_key = ""

with open("system_prompt.txt", 'r') as sprompt:
	system_prompt= sprompt.read()

messages = [
    {"role": "system", "content": system_prompt},
]

while True:
    user_input = input("User: ")
    if user_input == 'q':
        break

    log.info('User:' + user_input)
    item = {"role": "user", "content": user_input}
    messages.append(item)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    log.info(response)
    print('Pinecone: ' + str(response['choices'][0]['message']['content']) + '\n')
    call(["/usr/bin/python3", "Speak.py", str(response['choices'][0]['message']['content'])])
    messages.append(response['choices'][0]['message'])