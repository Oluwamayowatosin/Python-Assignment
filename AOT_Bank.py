from select import select
import mysql.connector
import sys
import random
import time


class AOT_Class:
    def __init__(self):
        self.connection()
        self.option()

    def connection(self):
        self.mycon = mysql.connector.connect(host="localhost", user="root", passwd="", database="bank_db")
        self.mycursor = self.mycon.cursor()
        # cursor.execute("CREATE TABLE user_details (First_Name VARCHAR (20), Last_name TEXT (20), Sex VARCHAR (8), Address VARCHAR (50), Account_Type VARCHAR(10), Phone_Number VARCHAR(11),Account_no INT(11), Account_Pin INT(11) Account_Balance INT(11))")
  
    def option(self):
        print("""Welcome to AOT Bank plc
            1. Register
            2. Transaction
            3. Quit""")    
        self.userInput = input("Enter your option to countinue: ")
        if self.userInput == "1":
            self.register()
        elif self.userInput == "2":
            self.transaction()
        elif self.userInput == "3":
            self.quit()
        else:
            print("Invalid input")
            self.option() 
    
    
    def register(self):
       # global account_name
        self.connection()
        detail = ["fName", "lName", "gender", "address", "acct_num", "phone", "acct_pin"]
        request = ["First name", "Last name", "Gender", "Address", "Account_Type", "Phone number", "Account pin"]
       # account_name = (detail[0])
        for i in range(7):
            detail[i] = input("Enter your "+request[i]+"  ")
        acct_no = "02"+str(random.randint(10000000, 90000000))
        myquery = """INSERT INTO user_details (First_Name, Last_name, Gender, Address, Account_Type, Phone_Number,
                 Account_no, Account_Pin) VALUE(%s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (detail[0], detail[1], detail[2], detail[3], detail[4], detail[5], acct_no, detail[6])
        self.cursor = self.mycon.cursor()
        self.mycursor.execute(myquery, val)
        self.mycon.commit()
        print ("Please wait your Transaction is being processing")
        time.sleep(5)
        print(self.mycursor.rowcount, """registration is successful 
              Your account number is """+acct_no)
        self.mycon.close()
        self.option()
        
        
    def transaction(self):
        transact = ["1. Withdraw", "2. Deposit", "3. Transfer", "4. Check Balance", "5. Quickairtime", "6. loan", "7. Customer Details", "8. close Account", "9. cancel"]
        self.acct_no = input("Enter your account number: ")
        self.acct_pin = input("Enter your account pin: ")
        query = "SELECT * FROM user_details WHERE Account_no=%s AND Account_Pin=%s"
        val = (self.acct_no, self.acct_pin)
        self.mycursor.execute(query, val)
        self.record = self.mycursor.fetchall()
        if self.record:
            print("You are welcome dear "+self.record[0][1]+" "+self.record[0][2])
            for val in transact:
                print(val)
            self.userInput = input("Enter an option to continue: ")
            if self.userInput == "1":
                self.withdraw()
            elif self.userInput == "2":
                self.deposit()
            elif self.userInput == "3":
                self.transfer()
            elif self.userInput == "4":
                self.checkBalance()
            elif self.userInput == "5":
                self.quickairtime() 
            elif self.userInput == "6":
                self.customerDetails() 
            elif self.userInput == "7":
                self.closeAccount()             
            elif self.userInput == "8":
                self.option()
            else:
                print("Invalid input")
                self.option() 
        else:
            print("Invalid account details. please go and register first to continue")
            self.option()
            

    def withdraw(self):
        amount = {"1":1000, "2":2000, "3":5000, "4":10000, "5":20000, "6":50000, "7":"Others"}
        for key, val in amount.items():
            print(key, val)
        self.userInput = input("Enter your withdrawer amount: ")
        query = "SELECT Account_Balance FROM user_details WHERE Account_no=%s"
        account = (self.acct_no,)
        self.mycursor.execute(query, account)
        self.balance = self.mycursor.fetchone()
        if amount[self.userInput] == "Others":
            self.userInput = int(input("Enter your amount> "))

        if self.balance[0] < amount[self.userInput]:
            print("Insuffient amount")
            self.option()
        else:
            newBalance = self.balance[0] - amount[self.userInput] 
            query = "UPDATE user_details SET Account_Balance = %s WHERE Account_no=%s"
            account = (newBalance, self.acct_no)
            self.mycursor.execute(query, account)
            self.mycon.commit()
            print ("Please wait your Transaction is being processing")
            time.sleep(5)
            print("Take you cash of "+str(amount[self.userInput]))
            self.option()


    def deposit(self):
        amount = {"1":1000, "2":2000, "3":5000, "4":10000, "5":20000, "6":50000}
        for key, val in amount.items():
            print(key, val)
        self.userInput = input("Enter your deposit amount: ")
        query = "SELECT Account_Balance FROM user_details WHERE Account_no=%s"
        account = (self.acct_no)
        self.mycursor.execute(query, account)
        self.balance = self.mycursor.fetchone()
        newBalance = amount[self.userInput] + self.balance[0]
        query = "UPDATE user_details SET Account_Balance = %s WHERE Account_no=%s"
        account = (newBalance, self.acct_no)
        self.mycursor.execute(query, account)
        self.mycon.commit()
        print ("Please wait your Transaction is being processing")
        time.sleep(5)
        print(amount[self.userInput], "deposit is successful") 
        self.option()
        
        
    def transfer(self):
        amount = {"1":1000, "2":2000, "3":5000, "4":10000, "5":20000, "6":50000}
        for key, val in amount.items():
            print(key, val)
        user_amount = input("Enter your transfer amount: ")
        recipient = input("Enter your recipient account number: ")
        query = "SELECT First_Name, Last_Name, Account_Balance FROM user_details WHERE Account_no=%s"
        query2 = "SELECT Account_Balance FROM user_details WHERE Account_no=%s"
        self.mycursor.execute(query, (recipient,))
        recipient_balance = self.mycursor.fetchone()
        self.mycursor.execute(query2, (self.acct_no,))
        user_balance = self.mycursor.fetchone()
        if recipient_balance and user_balance[0] > amount[user_amount]:
            newBalance = recipient_balance[2] + amount[user_amount]
            new_user_balance = user_balance[0] - amount[user_amount]
            query = "UPDATE user_details SET Account_Balance = %s WHERE Account_no=%s"
            self.mycursor.execute(query, (new_user_balance, self.acct_no))
            self.mycon.commit()
            query = "UPDATE user_details SET Account_Balance = %s WHERE Account_no=%s"
            self.mycursor.execute(query, (newBalance, recipient))
            self.mycon.commit()
            print ("Please wait your Transaction is being processing")
            time.sleep(5)
            print(str(amount[user_amount])+" transfered succefully to "+ recipient_balance[0]+" "+ recipient_balance[1])
            self.option()


    def checkBalance(self):
        query = "SELECT Account_Balance FROM user_details WHERE Account_no=%s"
        account = (self.acct_no,)
        self.mycursor.execute(query, account)
        self.balance = self.mycursor.fetchone()
        print ("processing")
        time.sleep(5)
        print("Your balance is "+ str(self.balance[0]))
        self.option()

    def quickairtime(self):
        amount = {"1":1000, "2":2000, "3":5000, "4":10000, "5":20000, "6":50000, "7":"Others"}
        for key, val in amount.items():
            print(key, val)
        self.userInput = input("Enter your Recharge amount: ")
        self.phone_No = input("Enter your phone Number: ")
        network = {"1":"Mtn", "2":"Glo", "3":"Airtel", "4":"9mobile"}
        for key, val in network.items():
            print(key, val)
        self.networkImput = input("Select your Biller: ")
        query = "SELECT Account_Balance FROM user_details WHERE Account_no=%s"
        account = (self.acct_no,)
        self.mycursor.execute(query, account)
        self.balance = self.mycursor.fetchone()
        newBalance = self.balance[0] - amount[self.userInput] 
        query = "UPDATE user_details SET Account_Balance = %s WHERE Account_no=%s"
        account = (newBalance, self.acct_no)
        self.mycursor.execute(query, account)
        self.mycon.commit()
        print ("Please wait your Transaction is being processing")
        time.sleep(5)
        print("Recharge of " +str(amount[self.userInput]) +"" " was successful")
        self.option()
                
    def customerDetails(self):
            acct_no = input("Enter Account Number: ")
            query = "SELECT * FROM USER_DETAILS WHERE Account_no=%s"
            account = (self.acct_no,)
            self.mycursor.execute(query, account)
            result = self.mycursor.fetchone()
            for i in result:
                print(i, end=" ")
            self.option()
            
            
    def closeAccount(self):
            acct_no = input("Enter Account Number: ")
            query= "DELETE FROM USER_DETAILS WHERE Account_no=%s"
            account = (self.acct_no,)
            self.mycursor.execute(query, account)
            self.mycon.commit()
            print("Account Data deleted Successfully....")
            self.option() 
           
    def quit(self):
        self.mycon.close()
        sys.exit()

bank = AOT_Class()

