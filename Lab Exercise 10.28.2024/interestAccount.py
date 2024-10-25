#InterestAccount class definition
#Author: 
#Date: 10/28/2024

from bankAccount import BankAccount

class InterestAccount(BankAccount):
    def __init__(self, name, number, balance, rate):
        #Add code here
        

    def addInterest(self):
        #Add code here
        
    
    def __str__(self):
        msg = self.name + ' ' + self.number + ' ' + \
        str(round(self.balance, 2)) + ' ' + str(round(self.rate, 2)) + '\n'
        return msg
#End of InterestAccount class definition
