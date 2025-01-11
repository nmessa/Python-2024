##Lab Exercise 1.14.2025 Problem 1
##Author: 
##This program simulates a form of Yahtzee.  It will run until the player
##gets to 1000 points.  The player rolls 5 dice and earns points according
##to the following table:
##    5 of kind = 50
##    4 of a kind = 25
##    3 of a kind = 10
##The program keeps track of the number of triples, quadruple, and
##quintuples are rolled.  The goal of the game is to earn 1000 points
##in as few rolls as possible


# FiveDice.py
import random

#Initialize Variables
keep_going = True
score = 0
count = 0
three = 0
four = 0
five = 0

# Game loop 
while keep_going:
    #Add one to count
    count += 1
    
    #initialize dice list
    dice = [0,0,0,0,0]

    #roll five dice
    #Add code here

    #print result of roll
    #Add code here

    
    # Sort the dice
    #Add code here

    
    # Check for five of a kind, four of a kind, three of a kind
    # Yahtzee - all five dice are the same
    #Add code here

        
    # FourOfAKind - first four are the same, or last four are the same
    #Add code here

        
    # ThreeOfAKind - first three, middle three, or last three are the same
    #Add code here


    #Keep rolling until you get 1000 points
    #Add code here


#print result of game
print("It took", count, 'rolls to get 1000 points')
print("Threes:", three)
print("Fours:", four)
print("Yahtzee:", five)
    
    
