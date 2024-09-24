# read a text from a given file 'poem.txt' and find out the contains the word "Twinkle"

f=open("prac37.txt")

content=f.read()
if("Twinkkle" in content):
    print("Twinkkle is present in the content")
else:
    print("Twinkkle is not present in the content")
f.close()