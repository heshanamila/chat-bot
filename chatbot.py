import random

Greeting_words = ("hello","hi","ssup","greeting")
Greeting_response = ["hey","Good morning","Wssup"]
def check_for_greeting(sentence):
    for word in sentence.split(' '):
        if word.lower() in Greeting_words:
            return random.choice(Greeting_response)
        else:
            return "I dont know what you are talking about"
while True:
    sentence = input("You: ")
    response = check_for_greeting(sentence)
    print("your Bot: "+response)

    if 'bye' in sentence:
        break
