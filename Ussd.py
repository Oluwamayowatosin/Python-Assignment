import sys
import subprocess
service = ' '
account = 500
data = 0
def main_Menu():
    global service
    print(""" 1. Data Plans\n 2. Social Bundles\n 3. Balance Check\n 4. Roaming/Int'l\n 5. Borrow Credit/Recharge\n 6. Gift Data\n 7. Video Packs\n 8. Hot Deals """)
    option = input('>>>>>>')
    if option == '1':
        buydata()
        data = input(">>>>>>")
        if data == "1":
            service = "Daily"
            print(""" 1. N50 for 40MB\n 2. N100 for 100MB\n 3. N100 for 350MB(IG/TIKTOK/Youtube)\n 4. N200 for 200mb(3 days)\n 5. N300 for 1GB\n 6. N500 for2GB(2days)\n 99. Next\n 0. Back """)
            n50 = input(">>>>>>")
            if n50 == "1":
                service = "N50 for 40MB"
                print("""
                You will be charged N50 for the purchase of 
                   40MB Daily Plan.To proceed, select
                1. Auto-Renew\n 2. One-off\n 3. Buy for a Friend\n 4. Redeem Promo Code\n 0. Back """)
                auto = input(">>>>>>")
                if auto == "1":
                    service = " Auto-Renew"
                    if account > 50:
                        print(""" 
                        Congratulations! You have successfully purchase 50MB
                              Daily plan for N50 to check balance Dial *131*4#.
                                             Thank you !
                        """)
                    elif account < 50:
                        print("""
                            Y'ello! Activation of 40MB Daily Plan failed due 
                            to insufficient balance. Dial *904# to recharge 
                               from you bank account OR *606# to borrow 
                                                airtime
                            """)

                    oneOff = input(">>>>>")
                    if oneOff == "2":
                        service = "Oneoff"
                        if account > 50:
                            print("""
                            Congratulations! You have successfully purchase 50MB
                              Daily plan for N50 to check balance Dial *131*4#.
                                             Thank you !
                            """)
                            main_Menu()
                        elif account < 50:
                            print("""
                            Y'ello! Activation of 40MB Daily Plan failed due 
                            to insufficient balance. Dial *904# to recharge 
                               from you bank account OR *606# to borrow 
                                                airtime
                            """)
                            shutdown_input = input("Dissmise>>>>>>>").capitalize
                            if shutdown_input == "D" :
                                sys.exit()           
            elif n50 == 0:
                 main_Menu()                    
        elif data == "2":
            service = "Weekly"
            print(''' 1. N200 for 1GB(IG/TikTok/Youtube ONLY)\n 2. N300 for 350MB\n 3. N500 for 1.5GB\n 4. N500 for 750MB(2-Week plan)\n 5. N1,500 for 6GB\n 6. N1,000 for 2GB\n 99. Next\n 0. Back ''')    
            weekly = input(">>>>>") 
            if weekly == "3":
                print("""
                  You will be charged N500 for the purchase of 
                      1.5GB weekly plan.To proceed, select
                               1.Auto-Renew
                                2.One-off
                                 0.Back
                """)
                one_off = input(">>>>>>")
                if one_off == "2":
                   one_Off()
                elif one_off == "0":
                        buydata()
                one_off = input(">>>>>>>>")
                if one_off == "1":
                    if account >= 500:
                         print("""
                            Congratulations! You have successfully purchase 1.5GB
                              Weekly plan for N500 to check balance Dial *131*4#.
                                             Thank you !
                            """)
                         data += 1500
                         main_Menu()
                    elif account < 500:
                        print("""
                            Y'ello! Activation of 1.5GB weekly Plan failed due 
                            to insufficient balance. Dial *904# to recharge 
                               from you bank account OR *606# to borrow 
                                                airtime
                            """)
                        shutdown_input = input("QUIT>>>>>>>").capitalize
                        if shutdown_input == "Q" :
                            sys.exit()
        elif data == "3":
            service = 'Monthly'
            print(""" 1. N1,000 for 1.5GB\n 2. N1200 for 2GB\n 3. N1,500 for 3GB\n 4. N2,000 for 4.5GB\n 5. N2,500 for 6GB\n 6. N3,500 for 12GB\n 7. N5,000 for N20GB\n 8. N6,000 for 25GB\n 99. Next\n 0. Back """)
            option = input(">>>>>")
            if option == "7":
                print("""
                  You will be charged N5000 for the purchase of 
                      20GB Monthly plan.To proceed, select
                               1.Auto-Renew
                                2.One-off
                            3.Buy for a Friend
                            4.Redeem Promo Code
                                 0.Back
                """)
                at_oneoff = input(">>>>>")
                if at_oneoff == "2":
                     one_Off()
                elif at_oneoff == "0":
                    main_Menu()
                airtime = input('>>>>>>>>')
                if airtime == "1":
                    if account >= 5000:
                         print("""
                            Congratulations! You have successfully purchase 20GB
                              Weekly plan for N5000 to check balance Dial *131*4#.
                                             Thank you !
                            """)
                         data += 20000
                         main_Menu()
                    elif account < 5000:
                        print("""
                            Y'ello! Activation of 20 GB Monthly Plan failed due 
                            to insufficient balance. Dial *904# to recharge 
                               from you bank account OR *606# to borrow 
                                                airtime
                            """)
                        shutdown_input = input("QUIT>>>>>>>").capitalize
                        if shutdown_input == "Q" :
                            sys.exit()
        elif data == "0":
            main_Menu()

    elif option == '2':
        service = "Social Bundles"
        print(""" """)
    elif option == '3':
        service = "Balance Check"
        # print ("your data balance:\n "+"Bonus: "+data_tota+"MB expires 25/09/2022")
        # print("""*1
            
        # """)
    elif option == '4':
        service = "Roaming/Int'l"
        print(""" """)
    elif option == '5':
        service = "Borrow Credit/Recharge"
        print(""" """)
    elif option == '6':
        service = "Gift Data"
        print(""" """)
    elif option == '7':
        service = "Video Packs"
        print(""" """)
    elif option == '8':
        service = "Hot Deals"
        print(""" """)
    else:
        print("Invalid input")
        sys.exit()

def buydata():
        service = "Data Plans"
        print(""" Buy Data Plans
        1. Daily\n 2. Weekly\n 3. Monthly\n 4. 2-3month\n 5. Always ON Plans\n 6. Broadband Plans\n 7. Family Packs\n 8. Hot Deals\n 9. FREE Youtube\n 10. Manage Data\n 0. Back """)

def one_Off():
    print(""" Kindly select payment type
                1. Airtime\n 2. Pulse Points\n 3. Pulse points and Airtime\n 4. About Pulse Points  """)
def checkBalance():
    print(""" Pulse Main Account: N500. Get 6X MORE 
          when you recharge with *888*PIN# today. Load 
              N200 get N1200.Details via SMS """)
    print("To Buy Data Bundle Dial *131#")
    menu()                             
def menu():
          code = {'*131#','*556#'}
          user_code = (input(">>>>>>>"))
          if user_code == '*131#':
            main_Menu()
          elif user_code == "*556#":
            checkBalance() 
          else:
            print(""" Yello! Seems you dialed a wrong code. Please select
            1. Buy Data/Other bundles\n 2. Borrow airtime/data\n 3. Goodbag Offers\n 4. Momo Agents\n 5. VAS\n 6. Chat Ziqi """)
            user_input = input(">>>>>")
            if user_input == '1':
                service = 'Buy Data/Other bundles'
                main_Menu()
            else:
             print("Inavalid Operation System, Try again")
             sys.exit        
menu()   
