text = "The goal is to turn data into information, and information into insight"

a = text.replace(","," ").replace("."," ").split()

b = [word.upper() for word in a]

print(b)