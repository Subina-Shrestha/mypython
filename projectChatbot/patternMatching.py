#for pattern matching
import re
pattern="do you remember (.*)"
message="do you remember strawberries and cigarette?"
match=re.search(pattern,message)
if match:
    print("string matches")
else:
    print( "sorry unable to respond!!")
