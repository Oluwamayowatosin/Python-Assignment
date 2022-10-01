import sys
import os
import time
import mysql.connector as sql
import random

CBT_db = sql.connect(host="127.0.0.1", user="root", password ='', database="CBT_DATABASE")
cursor = CBT_db.cursor()
# cursor.execute("CREATE DATABASE CBT_DATABASE")
# cursor.execute("CREATE TABLE STUDENT_REG (STUDENT_ID INT(50) PRIMARY KEY AUTO_INCREMENT, STUDENT_FULLNAME VARCHAR(30),GENDER VARCHAR(10),PHONE_NO VARCHAR(11)  PASSWORD_ INT(11), REG_ID INT(15), SCORE INT(3))")

class CBT_dbClass:
    def __init__(self):
        self.connection()
        self.option()
        
    def connection(self):
        self.CBT_db = sql.connect(host="localhost", user="root", passwd="", database="CBT_database")
        self.cursor = self.CBT_db.cursor()
  
    def option(self):
        print("""CBT EXAMINATION
              1. Register
              2. login
              4. Quit""")
        self.userInput = input("Enter your option to countinue: ")
        if self.userInput == "1":
            self.Register()
        elif self.userInput == "2":
            self.Login()
        elif self.userInput == "3":        
            self.Quit()    
        else:
            print("Invalid input")
            self.option() 
            
            
    def Register(self):
           # global student_name
        self.connection()
        detail = ["fName", "gender","phone", "password"]
        request = ["Full Name", "Gender","Phone Number", " Password"]
       # student_name = (detail[0])
        for i in range(4):
            detail[i] = input("Enter your "+request[i]+"  ")
            reg_id = "02"+"REG"+str(random.randint(10000000, 90000000))
        myquery = """INSERT INTO student_reg (Full_Name, Gender, Phone_No, Password, Reg_Id) VALUE(%s, %s, %s, %s, %s)"""
        val = (detail[0], detail[1], detail[2], detail[3], reg_id)
        self.cursor.execute(myquery, val)
        self.CBT_db.commit()
        print ("Please wait your Registration is being processing")
        time.sleep(5)
        print(self.cursor.rowcount, """registration is successful 
              Your Registration ID is """+reg_id)
        self.CBT_db.close()
        self.option()   
        
        
        
    def Login(self):
        login = ["1. Exam_Question", "2. Student_Details", "3. Cancel"]
        self.Full_name = input("Enter full Name: ")
        self.Reg_Id = input("Enter your Reg_Id: ")
        query = "SELECT * FROM student_reg WHERE Full_Name=%s AND Reg_Id=%s"
        val = (self.Full_name, self.Reg_Id)
        self.cursor.execute(query, val)
        self.record = self.cursor.fetchall()
        if self.record:
            print("You are welcome dear "+self.record[0][1]+" "+self.record[0][5])
            for val in login:
                print(val)
            self.userInput = input("Enter an option to continue: ")
            if self.userInput == "1":
                self.Exam_Question()
            elif self.userInput == "2":
                self.Student_Details()    
            elif self.userInput == "3":
                self.option()
            else:
                print("Invalid input")
                self.option() 
        else:
            print("Invalid account details. please go and register first to continue")
            self.option()           
    
    
    def Exam_Question(self):
        print("Your Exam start now:")
        Question_db = ["1. what is a noun?\n", "2. what is a verb?\n", "3. what is a pronoun?\n", "4. what is an adverb?\n", "5. what is the capital of oyo?\n", ]
        answers_db = [["name", "person", "animal", "place", "things"], ["action", "word"], ["use", "noun"], ["qualifies", "verb"],["ibadan"]]
        
        x = 0

        self.score = 0
        for que in Question_db:
            self.correct = 0
            print(que)
            userinput = input("Your answer ")
            self.answer = answers_db[x]
            for option in self.answer:
                if option in userinput:
                    self.correct +=1
            print(self.correct)
            if len(self.answer) ==self.correct:
                print("You are correct")
                self.score +=5
            else:
                print("You are wrong")
            x +=1  
            query = "UPDATE student_reg SET Score = %s WHERE Reg_Id=%s"
            account = (self.score, self.Reg_Id)
            self.cursor.execute(query, account)
            self.CBT_db.commit()
            time.sleep(2) 
        print("Fetching your Result............")
        print("Your total score is "+ str(self.score))
        self.option()
           
        
    def Student_Details(self):
        query = "SELECT * FROM student_reg WHERE Reg_Id=%s"
        val = (self.Reg_Id,)
        self.cursor.execute(query, val)
        result = self.cursor.fetchone()
        for i in result:
            time.sleep(2)
            print(i, end=" ")
        self.option()        
            
    def Quit(self):
        self.CBT_db.close()
        sys.exit()

CBT = CBT_dbClass()            
            
