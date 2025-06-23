text = "world hello hello hello hello"

firstH = text.find("h")
lastH = text.rfind("h")

middletext = text[firstH+1:lastH].replace("h", "H").replace(" ", "")

newtext = text[:firstH+1] + middletext + text[lastH:]

print(newtext)