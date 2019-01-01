import random
import sys

Questions = [
    "How are you?"
    "What are you doing?"
    "How is the weather today?"
    ]
Answers = [
    "I m fine thank you!"
    "Nothing interesting"
    "The weather is nice"
    ]
def list_faq():
    for i in range(len(Questions)):
        print(str(i)+":"+Questions[i])
def check_for_FAQ_by_index():
    list_faq()
    question_id = input("Which question do you want me to answer?")
    response = ""

    if "bye" in question_id:
        sys.exit()
    elif int(question_id) < len(Questions):
        response = Answers[int(question_id)]
    else:
        response = "I dont know the answer to that"
    return response

def check_for_FAQ(question):
    response = ""
    if question in Questions:
        index = Questions.index(question)
        response = Answers[index]
    else:
        response = "I don't know the answer to that"
    return response
while True:
    response = check_for_FAQ_by_index()
    print("Your Bot: "+ response)
    
