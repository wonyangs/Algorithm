trans_dict = {
    "CU" : "see you",
    ":-)" : "I’m happy",
    ":-(" : "I’m unhappy",
    ";-)" : "wink",
    ":-P" : "stick out my tongue",
    "(~.~)" : "sleepy",
    "TA" : "totally awesome",
    "CCC" : "Canadian Computing Competition",
    "CUZ" : "because",
    "TY" : "thank-you",
    "YW" : "you’re welcome",
    "TTYL" : "talk to you later"
}

while True:
    input_text = input()
    print(trans_dict.get(input_text, input_text))
    if input_text == "TTYL":
        break
