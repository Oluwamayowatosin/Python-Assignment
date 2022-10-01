# user = input("Enter the word here >>>").lower()
# non_word = ["of", "and", "is", "for", "the"]
# splited_word = user.split(" ")
# acronyms = ""
# for acro in splited_word:
#     if acro not in non_word:
#         acronyms += acro[0]
# print(acronyms.upper())



from playsound import playsound
sound = [("c:\prjct&Assgnmts\music\Our.mp3"), ("c:\prjct&Assgnmts\music\Wonder.mp3"), ("c:\prjct&Assgnmts\music\OLUWA.mp3"),]
for i in sound:
    playsound(i)
range
print([x for x in range(1, 100, 5)])    
