#define variables
name="echobot"
weather="cloudy"

#define a dictionary with predefined responses
responses={"what is your name?":"my name is {0}".format(name)
}
def respond(messages):
    if messages in responses:
        return responses(messages)
    else:
        return "sorry unable to return the message"

