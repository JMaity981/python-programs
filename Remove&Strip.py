def remove_and_strip(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
str="      Python is high level language      "
print(remove_and_strip(str,"is"))