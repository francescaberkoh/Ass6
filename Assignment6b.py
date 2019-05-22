'''
Created on May 19, 2019

@author: Francesca
'''
from tkinter import*
import random

root = Tk()

deck = []

#Make deck of cards
for suit in ["of_spades", "of_clubs", "of_diamonds", "of_hearts"]:
    for v in range(1,14):
        deck.append([v,suit])

dealerdeck = []
playerdeck = []

#Making the player's hand
while len(playerdeck) < 3:
    random.shuffle(deck)
    p = deck.pop()
    if p not in playerdeck:
        playerdeck.append(p)
        
Pcard1 = playerdeck[0]
Pcard2 = playerdeck[1]
Pcard3 = playerdeck[2]

players = Pcard1[0] + Pcard2[0]

#Making the dealers hand
while len(dealerdeck) < 3:
    random.shuffle(deck)
    d = deck.pop()
    if d not in dealerdeck or playerdeck:
        dealerdeck.append(d)

print(playerdeck, dealerdeck)
print(Pcard1, Pcard2, Pcard3)

Dcard1 = dealerdeck[0]
Dcard2 = dealerdeck[1]
Dcard3 = dealerdeck[2]


dealers = Dcard1[0] + Dcard2[0]

You = Label(root, text = "You have these cards:"+ " " + str(Pcard1) + " " + str(Pcard2) + "        Your cards make a combined total of:" + " " + str(players))
You.grid(row=0, column=2)

#Making a function that displays card face for player
photo= PhotoImage(file = str(Pcard1[0]) +"_"+ str(Pcard1[1]) + ".png")
photo = photo.subsample(2,2)
test = Label(root, image = photo)
test.grid(row=1, column =1)

photo1= PhotoImage(file = str(Pcard2[0]) +"_"+ str(Pcard2[1]) + ".png")
photo1 = photo1.subsample(2,2)
test1 = Label(root, image = photo1)
test1.grid(row=1, column =2)

photo2= PhotoImage(file = str(Pcard3[0]) +"_"+ str(Pcard3[1]) + ".png")
photo2 = photo2.subsample(2,2)
test2 = Label(root, image = photo2)


Action = Label(root, text= "Would you like to Hit or Stay?")
TextBox = Entry(root)
Action.grid(row=2, column = 1)
TextBox.grid(row=3, column =1)

def show():
    test2.grid(row=1, column =3)

  
    
def send ():    
    userinput = TextBox.get()
    if players < 21:
        if userinput == "hit":
            current = Pcard1[0] + Pcard2[0] + Pcard3[0]
            player_result = Label(root, text= "You now have:" + " " + str(current) + " " + "With these cards:" + " " + str(Pcard1) + " " + str(Pcard2) + " "+ str(Pcard3))
            player_result.grid(row=4, column =1)
            show()
            dealer_result = Label(root, text= "Dealer has:" + " " + str(Dcard1) + " " + str(Dcard2) + " " + str(Dcard3) + " " + "The dealer has a combined total of:"+ " "+ str(dealers))
            dealer_result.grid(row=5, column =1)
            if current < 21 and dealers < 21 :
                if dealers == current:
                    Tie = Label(root, text = "It's a tie!")
                    Tie.grid(row=6, column =1)
                        
                if current < dealers:
                    DealerWins = Label(root, text = "Dealer Wins :(")
                    DealerWins.grid(row=6, column =1)
                if current > dealers:
                    playerwins = Label(root, text = "You Win!")
                    playerwins.grid(row=6, column =1)
            else:
                if current > 21:
                    DealerWins3 = Label(root, text = "You Busted! Dealer Wins :(")
                    DealerWins3.grid(row=6, column =1)
                elif dealers> 21:
                    playerwins3 = Label(root, text = "Dealer Busted! You Win!")
                    playerwins3.grid(row=6, column =1)
    
                
        else:
            dealer_result = Label(root, text= "Dealer has:" + " " + str(Dcard1) + " " + str(Dcard2) + " " + str(Dcard3) + " " + "The dealer has a combined total of"+ " "+ str(dealers))
            dealer_result.grid(row=4, column =1)
            if players < 21 and dealers < 21 :
                if dealers == players:
                    Tie = Label(root, text = "It's a tie!")
                    Tie.grid(row=5, column =1)
                        
                if players < dealers:
                    DealerWins = Label(root, text = "Dealer Wins :(")
                    DealerWins.grid(row=5, column =1)
                if players > dealers:
                    playerwins = Label(root, text = "You Win!")
                    playerwins.grid(row=5, column =1)
            else:
                if players > 21:
                    DealerWins3 = Label(root, text = "You Busted! Dealer Wins :(")
                    DealerWins3.grid(row=5, column =1)
                elif dealers> 21:
                    playerwins3 = Label(root, text = "Dealer Busted! You Win!")
                    playerwins3.grid(row=5, column =1)
    else:
        if players == 21:
            BlackJack = Label(root, text="BlackJack!")
            BlackJack.grid(row=4, column =1) 
        else:
            Over = Label(root, text="You BUST!")
            Over.grid(row=4, column =1)
sendb = Button (root, text = "Check", command = send)
sendb.grid(row=3, column =2)

root.mainloop()