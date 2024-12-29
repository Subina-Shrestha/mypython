import time
time.sleep(0.5)
responses={
    "whats your name?":"they call me bot",
    "whats the weather today?":"I am not sure though"
}
def respond(message):
    if message in responses:
        return responses(message)
    else:
        return "sorry I am unable to respond"
