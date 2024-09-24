#Repeat prac40 for a list for such word to be censored.

words = ["Donkey", "achha" , "Bad"]

with open("prac40.txt" , "r") as f:
    content=f.read()
for word in words:
  content=content.replace(word , "#" * len(word))

with open("prac40.txt" , "w") as f:
    f.write(content)  