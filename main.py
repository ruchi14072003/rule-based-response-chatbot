#question:answer

import time
now = time.ctime()

qna = {

    "hello":"hi there! How can I help you?",
    "how are you":"I am just a computer program, but thanks for asking!",
    "what is your name":"My name is siri",
    "what is the time now": now,
    "goodbye":"Goodbye!",

}

while True:
    qs = input()

    if(qs == "quit"):
        break
    
    else:
        print(qna[qs])
