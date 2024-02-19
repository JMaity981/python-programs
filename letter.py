letter= '''Deer <|name|>
You are selected
Date: <|date|>'''
name = input("Enter Your Name: ")
date = input("Enter Date: ")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)
print(letter)