import re
import time
time.sleep(0.5)
pattern="do you remember (.*)"
message="do you remember strawberries and cigarettes?"
match=pattern.search(pattern,message).group(1)
match("yeah strawberries and cigarette")
respond=choose_response(patter)
response ("how could I forget")