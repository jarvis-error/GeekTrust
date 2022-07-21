import math
class Ledger:
    # define variables
    def __init__(self,Bank_Name,Borrower_Name,Pricipal,Tenure,Interest):
        self.Bank_Name=Bank_Name
        self.Borrower_Name=Borrower_Name
        self.P=Pricipal
        self.N=Tenure
        self.R=Interest/100

    # To find the amount paid and remaining emi'S
    def BALANCE(self,Bank_Name,Borrower_Name,EMI_Number):
        EMI=(((self.P*self.N*self.R)+(self.P)))/(self.N*12)
        EMI=math.ceil(EMI)
        Total_Paid=EMI*EMI_Number
        Remaining_EMI=(self.N*12)-EMI_Number
        print(Bank_Name,Borrower_Name,Total_Paid,Remaining_EMI)


# Create Object for each Loan operation
customer1=Ledger('IDIDI','Dale',10000,5,4)
customer2=Ledger('MBI','Harry',2000,2,2)
customer3=Ledger('UON','Shelly',15000,2,9)

# Calling Methods
customer1.BALANCE('IDIDI','Dale',5)
customer1.BALANCE('IDIDI','Dale',40)
customer2.BALANCE('MBI','Harry',12)
customer2.BALANCE('MBI','Harry',0)
