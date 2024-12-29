
import time
time.sleep(0.5)
def respond(message):
    return "I can hear you! You said .{}".format(message)
def send_message(message):
    # nothing here
    pass
msg="hello"
print(respond(msg))
