# import datetime

# FiveTo6 = ''' Its time for morning Devotion. 5:Am to 6:Am thanks'''
# SixTo8 = ''' It time to be in the Church. 6:Am to 8:Am thanks'''
# EightTo11 = ''' Service hour. 8:Am to 11:Am thanks'''
# ElevenTo20 = ''' Sunday things visiting family and friends. 11:Am to 20:Pm thanks'''
# TwentyTo21 = ''' Nigt prayre. 21:Pm to 22:pm thanks'''
# TwentyoneTo22 = ''' Its time for morning Devotion. 21:pm to 22:Pm thanks'''

# def Time():
#     hour = int(datetime.now().striftime("%M"))
#     # check = int(datetime.datetime.now().strftime("%M")) 
#     if hour >= 5 and hour < 6:
#         print(FiveTo6)
#         return FiveTo6
#     elif hour >= 6 and hour < 8:
#         print(SixTo8)
#         return SixTo8
#     elif hour >= 8 and hour < 11:
#         print(EightTo11) 
#         return EightTo11
#     elif hour >= 11 and hour < 20:
#         print(ElevenTo20) 
#         return ElevenTo20
#     elif hour >= 20 and hour < 21:
#         print(TwentyTo21)
#         return TwentyTo21
#     elif hour >= 21 and hour < 22:
#         print(TwentyoneTo22) 
#         return TwentyoneTo22
#     else:
#         print("In this time, You are sleeping ")

#         return '''In this time, You are sleeping'''  
#     Time()            

            
        

import datetime as dt
# tim = dt.datetime.now()
# from playsound import playsound
while True:
    tm = dt.datetime.now()
    if tm.strftime("%I") == "11" and tm.strftime("%M") == "01" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
        print("Its time for morning Devotion. 5:Am to 6:Am thanks.")
    elif tm.strftime("%I") == "11" and tm.strftime("%M") == "02" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
        print("It time to be in the Church. 6:Am to 8:Am thanks.")
    elif tm.strftime("%I") == "11" and tm.strftime("%M") == "03" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
        print("Service hour. 8:Am to 11:Am thanks.")  
    elif tm.strftime("%I") == "11" and tm.strftime("%M") == "04" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
        print("Sunday things visiting family and friends. 11:Am to 20:Pm thanks")   
    elif tm.strftime("%I") == "11" and tm.strftime("%M") == "05" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
        print("Nigt prayer. 21:Pm to 22:pm thanks")
    elif tm.strftime("%I") == "11" and tm.strftime("%M") == "06" and tm.strftime("%S") == "00" and tm.strftime("%p") == "AM":
        print("It's time to Sleep. 21:Pm to 22:pm thanks")
         
    # else:
    #     print("sleeping Already")                         
    #     playsound("C:\python\music\OLUWA.mp3")
    newmin = tm.strftime("%S")
    if newmin == "00":
        break




# import datetime
# while True:
#     dtim = datetime.datetime.now()
#     day = dtim.strftime("%A")
#     hour= dtim.strftime("%I")
#     minute = dtim.strftime("%M")
#     seconds = dtim.strftime("%S")
#     # print(minute)

#     if dtim.strftime("%A") == "monday":
#         if dtim.strftime("%I") == "8" and dtim.strftime("%M") == "36"  and dtim.strftime("%S") == "00":
#             for i in range(1):
#                 print("New day new Week")
    # elif day == "tuesday": 
    #     if hour == "8" and minute == "19"  and seconds == "00" and sec == seconds:
    #         for i in range(1):
    #             print("Fasting day")
    #         sec +=1
    # elif day == "wednesday":
    #     if hour == "8" and minute == "20"  and seconds == "00" and sec == seconds:
    #         for i in range(1):
    #             print("Evening srevice")
    #         sec +=1  
    # elif day == "thursday":
    #     if hour == "8" and minute == "21"  and seconds == "00" and sec == seconds:
    #         for i in range(1):
    #             print("Free class")
    #         sec +=1
    # elif "friday":
    #    if hour == "8" and minute == "22"  and seconds == "00" and sec == seconds:
    #         for i in range(1):
    #             print("Time for practices")
    #         sec +=1
    # elif "saturday":
    #     if hour == "8" and minute == "23"  and seconds == "00" and sec == seconds:
    #         for i in range(1):
    #             print("Weekend Things")
    #         sec +=1
    # elif "sunday":
    #     if hour == "8" and minute == "24"  and seconds == "00" and sec == seconds:
    #         for i in range(1):
    #             print("It's Time to go to Church")
    #         sec +=1
    # else:
    #     print("Ivalide input")                                                               
