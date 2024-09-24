p1="Hello Guys!"
p2="I am Jainee Patel"
p3="Please follow"
p4="My linkdin account"

message=input("Enter Your Comment:")

if((p1 in message)or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This message is a spam ")
else:
    print("This message is not a spam")