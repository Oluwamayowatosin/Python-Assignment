Question_db = ["1. what is a noun?\n", "2. what is a verb?\n", "3. what is a pronoun?\n", "4. what is an adverb?\n", "5. what is the capital of oyo?\n"]
answers_db = [["name", "person", "animal", "place", "things"], ["action", "word"], ["use", "noun"], ["qualifies", "verb"],["ibadan"]]
x = 0
#correct = 0
# score = 0
studentscore = []

student_list = []
no_student = int(input("Enter the number of student: "))
for k in range(0, no_student):
     m= input()
     student_list.append(m)
print(student_list)

for y in student_list:
    print("Your Exam Start Now\n", str(y))
    x = 0
    score = 0
    for j in Question_db:
        correct = 0
        print(j)
        userinput = input("Enter the correct Answer\n")
        answer = answers_db[x]
        for option in answer:
            if option in userinput:
                correct +=1
        if len(answer) == correct:
            print("you are correct")
            score +=5
        else:
            print("you are wrong")
        x +=1
    studentscore.append(score)
    print("hello" " " +str(y)+ ", your total score is" " " +str(score)) 
print(studentscore)
studentscoreMax = max(studentscore)
maxIndex = studentscore.index(studentscoreMax) 
print("Congratulation" " " +str(student_list[maxIndex])+ " " "you have a maximum score of" " " +str(studentscore[maxIndex]))

score = [24, 30]
student = [ ' ', ' ']
x = 0
hightestScore = []
for na in score:
    if na == max(score):
        hightestScore.append(student[x])
    x +=1
print(", " .join(hightestScore))        
