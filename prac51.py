#Write a class Train which as a method to book a ticket get status and get fair information of train running under Indian Railways.

class Train:

    def __init__(self , TrainNo):
        self.TrainNo=TrainNo
    def book(self , fro , to):
        print(f"The Train is booked {self.TrainNo} from {fro} to {to}")   
    def getStatus(self ):
        print(f"TrainNo {self.TrainNo} is running on time")
    def getFare(self , fro , to):
        print(f"The Train fare {self.TrainNo} from {fro} to {to}")    

t=Train(12345)
t.book("Ahmedabad" , "Gandhinagar")
t.getStatus()
t.getFare("Gandhinagar" , "Ahmedabad")             
        