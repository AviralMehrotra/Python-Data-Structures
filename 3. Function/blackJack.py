import random 
import numpy as np
cards= np.array(["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q",
                "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q",
                "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q",
                "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "K", "Q",])

key=-1
random.shuffle(cards)
def baseCards(player):
    global key
    for i in range(2):
        key+=1
        player.append(cards[key])
    return player

def checkSum(player):
    sum=0
    for i in player:
        if i == "K" or i == "J" or i == "Q":
            sum+=10
        elif i == "A":
            sum+=11
        else:
            sum+=int(i)
    return sum
    
def drawCards(player, x):
    global key
    key+=1
    player.append(cards[key])
    sum= checkSum(player)
    return player, sum


user=[]
computer=[]
print(""" _______  ___      _______  _______  ___   _          ___  _______  _______  ___   _ 
|  _    ||   |    |   _   ||       ||   | | |        |   ||   _   ||       ||   | | |
| |_|   ||   |    |  |_|  ||       ||   |_| |        |   ||  |_|  ||       ||   |_| |
|       ||   |    |       ||       ||      _|        |   ||       ||       ||      _|
|  _   | |   |___ |       ||      _||     |_      ___|   ||       ||      _||     |_ 
| |_|   ||       ||   _   ||     |_ |    _  |    |       ||   _   ||     |_ |    _  |
|_______||_______||__| |__||_______||___| |_|    |_______||__| |__||_______||___| |_|""")
print("Hello everyone! Welcome to BlackJack!\n")
baseCards(user)
baseCards(computer)
print(f"User, your cards are: {user} \n")
userSum= checkSum(user)
computerSum= checkSum(computer)
print(f"One of the computer's card is {computer[0]} \n")
while computerSum<17:
    computer, computerSum = drawCards(computer, 1)
    print("Computer draws a card !\n")

if computerSum>21:
    print(f"Computer is Busted as sum is {computerSum}, User Wins")
    exit()
    
if userSum<17:
    print(f"Your cards sum is {userSum}, \n\tDrawing a Card from the deck!!\n")
    user, userSum= drawCards(user, 0)
    if userSum>21:
        print(f"User is Busted as sum is {userSum}, Computer Wins")
while True:
    drawOrStand= input(f"Your cards sum is {userSum}, Do you want to Draw a card or Stand: ").lower()
    if drawOrStand== "draw":
        user, userSum= drawCards(user, 0)
        if userSum>21:
            print(f"\nUser is Busted as sum is {userSum}, Computer Wins")
    else:
        break


if drawOrStand== "stand":
    if userSum<computerSum:
        print("\n\ncomputer wins ")
    elif userSum>computerSum:
        print("\n\nuser wins ")
    elif userSum==computerSum:
        print("\n\nIt's a draw ")


