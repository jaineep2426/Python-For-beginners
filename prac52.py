#Can you change the self parameter inside the class to something else.Try changing self to "slf" or "jainee" to see effect.

class Train:

    def __init__(slf , TrainNo):
        slf.TrainNo=TrainNo
    def book(slf , fro , to):
        print(f"The Train is booked {slf.TrainNo} from {fro} to {to}")   
    def getStatus(slf ):
        print(f"TrainNo {slf.TrainNo} is running on time")
    def getFare(slf , fro , to):
        print(f"The Train fare {slf.TrainNo} from {fro} to {to}")    

t=Train(12345)
t.book("Ahmedabad" , "Gandhinagar")
t.getStatus()
t.getFare("Gandhinagar" , "Ahmedabad")     