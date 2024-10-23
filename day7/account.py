while True:
    print("welcome to gorkha ko bank")
    print("1. Create new account")
    print("2. deposit")
    print("3. withdraw")
    print("4. list all the accounts")
    print("5. search account by name")
    print("exit")
    print()

    account_list=[]
    
    choice=int(input("enter your choices:"))
    
    match choice:
        case 1:
            print("new account selected")
        case 2:
            print("deposit selecteed")
        case 3:
            print("withdraw selected")
        case 4:
            print("all the account selected")
        case 5:
            print("search account selected")
        case 0:
            print("exiting.....")
            break






    