import random
print("Welcome to Stone, Paper, Knife")


def playermove():
    global pla
    pla = str(input("Player Move: "))
    if pla.lower() == "s" or pla.lower() == "p" or pla.lower() == "k":
        pla = pla.upper()
    else:
        print("Please Enter a Valid Move.")
        playermove()

def computer():
    global comp
    com = random.randint(1,3)
    if com == 1:
        comp = "S"
    elif com == 2:
        comp = "P"
    elif com == 3:
        comp = "K"
    else:
        computer()
    print("Computer Move:",comp)

def main():
    playermove()
    computer()
    if pla == comp:
        print("Tie")
    elif pla == "S":
        if comp == "P":
            print("Computer Wins")
        elif comp == "K":
            print("Player Wins")
    elif pla == "P":
        if comp == "K":
            print("Computer Wins")
        elif comp == "S":
            print("Player Wins")
    elif pla == "K":
        if comp == "S":
            print("Computer Wins")
        elif comp == "P":
            print("Player Wins")

main()
    
