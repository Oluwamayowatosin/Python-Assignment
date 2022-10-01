import sys
import time

print("Welcom to AVC Bank!!")
card = input("insert your ATM Card")
time.sleep(1)
func = ""
account_no = "0049860572"
Accoun_Name = "Atanda Mayowa"
Balance ="20000"
password =1224


def login():
    pin = int(input("Enter your four digit pin \n"))
    if pin==password:
        print("Welcome "+Accoun_Name+"  "+account_no+"")
        operation()
    else:
        print("Wrong pin number. Please try again")
        login()
        

def operation():
    global func
    print("""Select Transaction:\n1. Open Account\n 2. Check Balance\n 3. Withdraw\n 4. Deposit\n 5. Transfer\n 6. Recharge\n 7. Exit""")
    option = input(">>>")
    if option=="1":
        func = "Openaccount"
        Openaccount()
    elif option=="2":
        func = "Checkbalance"
        Checkbalance()
    elif option=="3":
        func = "Withdraw"
        Withdraw()
    elif option=="4":
        func = "Deposit"
        Deposit()
    elif option=="5":
        func = "Transfer"
        Transfer()
    elif option=="6":
        func = "Recharge"
        Recharge()            
    elif option=="7":
        sys.Exit()
    else:
        print("Invalid input")
        operation()

def tryAgain():
    print("Enter 1. Repeat Transaction again\n 2.Make other Transaction")
    user = input(">>>")
    if user=="1":
        if func =="Openaccount":
            Openaccount()
        elif func == "Checkbalance":
            Checkbalance()
        elif func=="Withdraw":
            Withdraw()
        elif func=="Deposit":
            Deposit()
        elif func=="Transfer":
            Transfer()
        elif func=="Recharge":
            Recharge()               
    elif user=="2":
        operation()
    else:
        print("Invalid input")
        tryAgain()
 
def Openaccount():
    account_no = "2221938503"
    fname = input("Enter your fname\n")
    lname = input("Enter your lname\n")
    phone_No =  int(input("Enter your phone number\n"))
    print("Congratulation Dear 2"+fname+" "+lname+" you have succefully open an acccount with ABC bank and your Account Number is "+account_no+" ")
    tryAgain()
  
def Checkbalance():
    print("Dear "+Accoun_Name+" your account Balance is "+Balance+" ")
    tryAgain()

def Withdraw():
    print(''' selcet Account:\n 1. Current\n 2. Savings\n ''')
    option = input(">>>")
    if option =="1":
        func = "Current"
    elif option =="2":
        func = "Savings"   
    print('''Select Option:\n 1. 1000\n 2. 2000\n 3. 5000\n 4. 1000\n 5. 20000\n 6. Other amount ''')
    option = input(">>>")
    if option=="1":
        func = "1000"
        print("Transaction Completed")
    elif option=="2":
        func = "2000"
        print("Transaction Completed")
    elif option=="3": 
        func = "5000"
        print("Transaction Completed")
    elif option=="4":
        func = "10000"
        print("Transaction Completed")
    elif option=="5":
        func = "20000"
        print("Transaction Completed")
    elif option=="6":
        func = "otheramount"
        otheramount = (input("Enter Amount to withdraw\n"))
        balance ="20000"
        if balance >= otheramount:
            balance = balance - otheramount
            print("your new balance is:", + balance)
        else:
            print("insufficient balance")
    else:
        print("Invalid input")
        operation()
    tryAgain() 


def Deposit():
    AccountNo = int(input("Enter AccouNo"))
    AccountNm = input("Enter AccountNm")
    Depositors = input("Enter depositor Name")
    AmountDp = input("Ënter the amount to be deposit:\n ")
    balance ="20000"
    balance = balance + AmountDp
    print("Deposite is successfully and Account balance is", + balance)
    tryAgain  

def Transfer():
    fromAcctNo = int(input("Transfer From AccouNo\n"))
    ToAcctNo = int(input("Transfer to AccountNo\n"))
    print(''' selcet Bank:\n 1. Gtbank\n 2. First Bank\n 3. Wema\n 4. UBA\n 5. Access\n''')
    option = input(">>>")
    if option =="1":
        func = "Gtbank"
    elif option =="2":
        func = "FirstBanks"
    elif option=="3":
        func ="Wema"
    elif option=="4":
        func="UBA"
    elif option=="5":
        func= "Access"  
    Amount_Trsf = (input("Enter Amount Transfering\n"))       
    balance ="20000"
    if balance >= Amount_Trsf:
            balance = balance - Amount_Trsf
            print("Transaction Succefully Completed your new balance is:", + balance)
    else:
            print("insufficient balance")
    tryAgain() 
    

def Recharge():
    print(''' selcet Type:\n 1. VTU(Airtime/Data)\n 2. EPIN\n ''')
    option = input(">>>")
    if option =="1":
        func = "VTU(Airtime/Data)"
    elif option =="2":
        func = "EPIN"     
    accountDbt = input("Enter account to Debit\n")
    mobileNo = input("Enter Mobile Number\n")
    amount = input("Enter amount\n")
    pin=input("Enter your pin to complete Transactrion\n") 
    balance = "20000"
    pin="1224"
    if (balance >= amount and  pin=="1224"):  
        print("Transaction successfully Complited")
    else:
        print("Insufficient Balance Please try again")    
    # else:
    #     print("Invalid details supplied. Please try again")
        tryAgain()

login() 





