# myName = "Oluwamayowa"
# age = "20yrs"
# score = "98.5"
# print("my name is  "+myName+" i'M "+age+" old i score "+score+" in my Level1 Project")



#Day2 Assignment
# def addition():
#     val1 = 56
#     val2 =23
#     print(val1 + val2)
# addition()

val1 = int(input("Enter val1"))
val2 = int(input("Enter val2"))
print(""" 1. Addition\n 2. Subtract\n 3. multiply\n 4. divide """)
user = input("Enter Option")
if int(user) ==1:
    print(val1 + val2)
elif int(user) ==2:
    print(val1 - val2)
elif int(user) ==3:
    print(val1 * val2)
elif int(user) ==4:
    print(val1 / val2)
else:
    print("Invalid Input")                
