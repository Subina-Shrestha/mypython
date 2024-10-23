#tuple unpacking
a,b,c=("ram",1,2)
print(f"a is {a},b is {b}, c is {c}")

#lambda function is anonymous function chahiyeko bela define gare huncha
#lambda arguments:expression(syntax)
power=lambda a,b:a**b
x=4
y=10
print(f"{x} raised to {y} is {power(x,y)}")

#wap using functions to take a string and return the number of vowel in that string
def count_vowels(sentence):
    sentence=sentence.upper()
    vowels = "AEIOU"  # list of vowels (lowercase and uppercase)
    count = 0
    for x in sentence:
        if x in vowels:
            count += 1
    return count

# Example usage
user= "Hello World"
print("Number of vowels:", count_vowels(user))