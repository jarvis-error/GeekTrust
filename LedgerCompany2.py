import math
class Ledger:
    # Define variables
    def __init__(self,Bank_Name,Borrower_Name,Pricipal,Tenure,Interest):
        self.Bank_Name=Bank_Name
        self.Borrower_Name=Borrower_Name
        self.P=Pricipal
        self.N=Tenure
        self.R=Interest/100
    def PAYMENT(self,Bank_Name,Borrower_Name,Lump_Sum_Amount,Current_EMI):
        self.Lump_Sum=Lump_Sum_Amount
        self.Current_EMI=Current_EMI

    # To find the amount paid including lump_sum and remaining emi'S
    def BALANCE(self,Bank_Name,Borrower_Name,EMI_Number):
        # EMI per month
        EMI = ((self.P * self.N * self.R) + (self.P)) / (self.N * 12)
        # Rounding off to next number
        EMI = math.ceil(EMI)
        # Total amount excluding Lump_Sum amount
        Total_Paid = EMI * EMI_Number
        # To check if any Lump_sum amount is paid, if YES adds Lump_sum to Total paid till current EMI's
        if self.Lump_Sum>0:
            if self.Current_EMI<=EMI_Number:
                Total_Paid+=self.Lump_Sum

        Find_Remaining_Month = Total_Paid/EMI
        Remaining_EMI=(self.N*12)-Find_Remaining_Month
        Remaining_EMI=math.ceil(Remaining_EMI)
        print(Bank_Name, Borrower_Name, Total_Paid, Remaining_EMI)

# Create Object for each Loan operation
customer1=Ledger('IDIDI','Dale',5000,1,6)
customer2=Ledger('MBI','Harry',10000,3,7)
customer3=Ledger('UON','Shelly',15000,2,9)
# Calling Method Payment
customer1.PAYMENT('IDIDI','DALE',1000,5)
customer2.PAYMENT('MBI','Harry',5000,10)
customer3.PAYMENT('UON','Shelly',7000,12)
# Calling Method Balance
customer1.BALANCE('IDIDI','Dale',3)
customer1.BALANCE('IDIDI','Dale',6)
customer3.BALANCE('UON','Shelly',12)
customer2.BALANCE('MBI','Harry',12)
