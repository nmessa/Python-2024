##Lab Exercise 1.14.2025 Problem 2
##Author: 

# War.py
import random
#define suits
suits = ['clubs', 'diamonds', 'hearts', 'spades']

#define face values
faces = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
         'ten', 'jack', 'queen', 'king', 'ace']

#Create an empty list to hold generated cards
cards = []

#Build deck of cards
#Add code here
        
#Shuffle the deck
#Add code here
        

#Create and initialize variables
keepGoing = True
hands = 0
ties = 0
my_score = 0
your_score = 0
card_count = 0

#Start game loop
while keepGoing and (hands < 26):
    #add one to hands
    #Add code here
    
    #Get my_card from deck
    #Add code here
    
    #increment card_count
    #Add code here
    
    #Get your_card from desk
    #Add code here
    
    #Increment card_count
    #Add code here

    #Print each player's hand
    #Add code here
    
    input()   #Pause

    #get face value for each card
    #Add code here


    #Test to see who won
    if faces.index(mc) > faces.index(yc):
        #Add code here
        
    elif faces.index(yc) > faces.index(mc):
        #Add code here
        
    else:
        #Add code here

    #Print current score
    print ("Score: Computer",my_score, ", You",your_score)

    #check for another round
    answer = input("Hit [Enter] to keep going, any other keys to exit: ")
    keepGoing = (answer == "")

#Print results of game
print("Game Over")
if my_score > your_score:
    print ("I win the game!")
elif your_score > my_score:
    print ("You win the game!")
else:
    print ("It was a tie game!")

##Sample Output
##I have the nine of clubs
##You have the three of clubs
##
##I win!
##Score: Computer 1 , You 0
##Hit [Enter] to keep going, any other keys to exit: 
##I have the ten of hearts
##You have the seven of hearts
##
##I win!
##Score: Computer 2 , You 0
##Hit [Enter] to keep going, any other keys to exit: 
##I have the five of clubs
##You have the queen of spades
##
##You win!
##Score: Computer 2 , You 1
##Hit [Enter] to keep going, any other keys to exit:
##
##
##More Rounds Here
##
##
##    
##I have the nine of diamonds
##You have the four of diamonds
##
##I win!
##Score: Computer 15 , You 11
##Hit [Enter] to keep going, any other keys to exit: 
##Game Over
##I win the game!
