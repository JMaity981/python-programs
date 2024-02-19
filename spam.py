text = input("Enter the text\n")
if("make a lot of money" in text or "buy now" in text or "subscribe this" in text or "click this" in text):
    print("The text is a spam message")
else:
    print("The text is not a spam message")