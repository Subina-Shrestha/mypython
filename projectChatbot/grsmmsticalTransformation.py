#transformation of pronoun
import re
def swap_pronouns(phrase):
    if 'I 'in  phrase:
        return re.sub('I ','you',phrase)
    if 'you ' in phrase:
        return re.sub('you','me',phrase)
    else:
        return phrase
phrase="I want my dog"
swap_pronouns(phrase)
