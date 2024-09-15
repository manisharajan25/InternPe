def MasterMind():
    def take_input(no_of_digits):
        flag=False
        while flag==False:
            try:
                p=input("type a number with "+str(no_of_digits)+" digits: ")
                if len(str(p))==no_of_digits and p.isnumeric()==True:
                    flag=True
                else:
                    print("Error, length of number is not equal to "+str(no_of_digits))
            except:
                print("Error, Give a valid positive non Zero value.")
        return str(p)
    
    Player_1=input("Enter Player 1 name: ")
    Player_2=input("Enter Player 2 name: ")
    
    #select the number of digits players will choose
    flag=False
    while flag==False:
        try:
            n=int(input("type the number of digits, players will choose: "))
            if n>0:
                flag=True
            else:
                print("Error, Give a valid positive non Zero value.")
        except:
            print("Error, Give a valid positive non Zero value.")
    
    print(Player_1 +" will select the integer")
    p1=take_input(n)
        
    #to remove the selected item from screen
    for _ in range(20):
        print(".")
    print(Player_2 +" will start guessing")
    g2=None
    c2=0
    while g2!=p1:
        g2=take_input(n)
        c2+=1
        for i in range(n):
            if p1[i]==g2[i]:
                print(g2[i]+" is correct.")
            else:
                print(g2[i]+" is not correct.")
    print("Match Found.")
    if c2!=1:
        print(Player_2 +" will select the integer.")
        p2=take_input(n)
        #to remove the selected item from screen
        for _ in range(20):
            print(".")
        print(Player_1 +" will start guessing")
        g1=None
        c1=0
        while g1!=p2:
            g1=take_input(n)
            c1+=1
            for i in range(n):
                if p2[i]==g1[i]:
                    print(g1[i]+" is correct.")
                else:
                    print(g1[i]+" is not correct.")
        print("Match Found.")
        
        print(Player_1 +" Guessed "+ str(c1) +" times.")
        print(Player_2 +" Guessed "+ str(c2) +" times.")
        if c1>c2:
            print(Player_2 +" is the master mind.")
        elif c1<c2:
            print(Player_1 +" is the master mind.")
        else:
            print("No One is the master mind.")
            
    else:
        print(Player_2 +" is the master mind.")
    return 0


MasterMind()
