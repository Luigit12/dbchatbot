import time, random, re, qa

name_chatbot = 'soofbot'

def metoyou(message):
    if ' me' in message:
            return re.sub(' me ', ' you ', message)
    elif ' your' in message:
            return re.sub(' your', ' my', message)
    else:
            return message

def answer(message):
    for pattern in patterns:
        match = re.search(pattern, message)
    if match:
        print(metoyou(name_chatbot + ": " + patterns[pattern].format(match.group(1))))

    if message == 'Stop!':
        exit()

    if message in qalist:
        return qalist[message]

    elif not message in qalist and patterns:
        return "I am sorry, can you repeat?"

def main(username):
    while True:
        question = input(username + ': ')
        print(name_chatbot + ': ' + answer(question))

patterns = qa.patterns
qalist = qa.qalist
