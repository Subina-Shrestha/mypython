user_template="USER:{0}"
bot_template="BOT:{0}"
import keywords

pattern={}
for intent, keys in keywords.item():
    pattern[intent]=re.compile('|'.join(keys))
print(pattern)
def match_intent(message):
    match_intent=None

    for intent, pattern in patterns.items():
        if pattern.search(message):
            matched_intent=intent
            return matched_intent
def respond(message):
    intent=match_intent(message)
    key="default"

    if intent in response:
        key=intent
        return response[key]
def send_message(message):
    print (user_template.format(message))
    response=respond(message)
    print(bot_template.format(message))

send_message("hello there")
