import random
responses={
    "whats your name?":["my name is echo",
                        "they call me echo",
                        "hey wasssup its echo"
                        ]        
            }
def respond(message):
    if message in responses:
        return random.choice(responses[message])
#if we have to choose the answer type
    elif message.endswith("?"):
        return random.choice(responses[message])
respond ("whats your name?")
    