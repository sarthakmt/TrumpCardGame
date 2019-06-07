####################################################
#  Execution Module with the logic implementation  #
#              ********RUN THIS*********           #
####################################################

import random
from trumpCard import deck
import pprint
from itertools import cycle
from utilities import generateSwitcher
from scoreBoard import createScoreboardSkeleton,gameData,scoreBoard

# Player vs Player
rounds = int(input("select number of rounds. Only from 3 or 5 or 7 "))

def checkRounds(rounds):
    roundList = [3,5,7]
    if rounds not in roundList:
        print("Please select the right integer")
        rounds = int(input("select number of rounds. Only from 3 or 5 or 7 "))
        return checkRounds(rounds)
    else:
        print("No-of Rounds Selected: "+str(rounds))
    return rounds        

rounds = checkRounds(rounds)

# Set player names
p1 = input("Player 1's name  : ")
p2 = input("Player 2's name  : ")

# prettyprint dictionaries
pp = pprint.PrettyPrinter(indent=4)

#check duplicate player names
def checkDuplicateNaming(p1,p2):
    if(p1 == p2):
        print("Names cannot be same \n")
        p2 = input("Player 2's name  : ")
        return checkDuplicateNaming(p1,p2)
    else:
        print("Let's play ",p1," and ",p2)    
    return p2    

p2 = checkDuplicateNaming(p1,p2)

# Dice
dice = [1,2,3,4,5,6]

# Toss to start the game with the winner of the toss
def rollADice(p1,p2):
    toss = {}
    # playOrder = []
    toss[p1] = random.choice(dice)
    print(p1,"'s dice  is ",toss[p1])
    toss[p2] = random.choice(dice)
    print(p2,"'s dice  is ",toss[p2])

    if(toss[p1] == toss[p2]):
        print("Equal, so toss again!")
        playOrderList = []
        return rollADice(p1,p2)
    elif(toss[p1]< toss[p2]):
        print(p2,"Wins toss! and will start the game \n")
        # winner = p2
        playOrderList = [p2,p1]
    elif(toss[p1]> toss[p2]):
        print(p1,"Wins toss! and will start the game \n")
        # winner = p1 
        playOrderList = [p1,p2]

    return playOrderList    

# Order of Play
playOrder = rollADice(p1,p2) 
print(playOrder)

# create a deck
# fetch from trumpCard.py
startDeck = deck

# all the characteristics put in a list from the deck dictionary
characteristics = [*[v for k,v in dict(deck[0]).items()][0]]

# all the spells
spells = ["God","Resurrect"]

# Round counter initialized
roundCounter =  1

# You can manually assign the weights for characteristics
# weights = strengthWeights(characteristics) # from utilities import strengthWeights
weights = {'Rank': 0, 'Weight': 1, 'Height': 1, 'FinishingMovePower': 1, 
'Championship': 1, 'WinPercentage': 1}

# startGame fucntion
def startGame(startDeck,playOrder,roundCounter,characteristics,spells,weights,rounds): 
    # shuffle the deck
    random.shuffle(startDeck)
    deckPlayer = {}
    deckPlayer1Temp = []
    deckPlayer2Temp = []
    
    # Distribute cards
    for card in startDeck:
        if(startDeck.index(card)%2 ==0):
            deckPlayer1Temp.append(card)
        else:
            deckPlayer2Temp.append(card)     

    deckPlayer[playOrder[0]] = deckPlayer1Temp
    deckPlayer[playOrder[1]] = deckPlayer2Temp
    exhaustDeck = [] # remember to randomize the cards when it goes to exhaustDeck
    
    # Select characteristics and spell
    def selectCharacteristicsNSpell(playerType,player,characteristicsSwitcher,spellSwitcher,initialScoreboard,GodFlag):
        selected = {}
        # cannot use God spell if the 1st player uses it
        if initialScoreboard[player]["spellLeft"] == 1 and GodFlag == True:
            answer = input("Do you want to use any spell? y/n \n")
            # check the input; only y and n allowed
            if(answer.lower() == "y"):    
                print("The following are the available characteristics, select the number \n")
                pp.pprint(spellSwitcher)
                selectedSpell = input("Which spell do you want to Choose? \n ")
                # check the input range should not exceed
                selected["selectedSpell"] = spells[int(selectedSpell)]
                if spells[int(selectedSpell)] == "God":
                    initialScoreboard[player]["spellLeft"] = 0
                    GodFlag = False
                elif spells[int(selectedSpell)] == "Resurrect":
                    if len(exhaustDeck) > 1:
                        initialScoreboard[player]["spellLeft"] = 0
                        selected["selectedSpell"] = "Resurrect"
                    else:    
                        print("Sorry! You can't use the Resurrect as there are less than 2 cards in ExhaustDeck \n")
                        selected["selectedSpell"] =  ""
            else:
                selected["selectedSpell"] = ""    
        else:
            selected["selectedSpell"] = ""

        if(playerType == "startPlayer"):
            print("The following are the available characteristics, select the number \n")
            pp.pprint(characteristicsSwitcher)
            selectedCharacteristicsInt = input("Which characteristics do you want to Choose? \n ")
            # characteristics selected by startPlayer
            selected["selectedCharacteristics"] = characteristics[int(selectedCharacteristicsInt)]
       
        return selected

    # When God Spell called
    def godSpell():
        print("You are GOD ! ")
        size1 = len(deckPlayer1)
        card1Number = int(input("Select any card from 0 to "+str(size1 - 1)+ " "))
        cardPicked1 = deckPlayer1[card1Number]
        size2 = len(deckPlayer2)
        card2Number = int(input("Select for other guy, a number of your choice from 0 to "+str(size2 - 1)+ " "))
        cardPicked2 = deckPlayer2[card2Number]
        cardsForBoth = []
        cardsForBoth.append(cardPicked1)
        cardsForBoth.append(cardPicked2)
        return cardsForBoth

    def resurrectSpell(exhaustDeck):
        sizeExhaust = len(exhaustDeck)
        print("You can RESURRECT ! Generating the random number \n")
        randomGenerator = random.randrange(sizeExhaust-1)
        print("Random number generated: ",str(randomGenerator))
        return randomGenerator    

    def checkWhoWon(selected,characteristic,weight,initialScoreboard):
        print(selected)
        p1 = list(selected)[0]
        print(p1)
        p2 = list(selected)[1] 
        selectedByOne = int(selected[p1]['Value'])
        selectedBySecond = int(selected[p2]['Value'])
        winner = ""
        if weight==0:
            print("LOW the better")
            if selectedByOne<selectedBySecond:
                print("Player to start Won: ",p1)
                winner = p1
            elif selectedByOne>selectedBySecond:    
                print("Player to start Second: ",p2)
                winner = p2
        elif weight==1:    
            print("HIGH the better")
            if selectedByOne>selectedBySecond:
                print("Player to start Won: ",p1)
                winner = p1
            elif selectedByOne<selectedBySecond:    
                print("Player to start Second: ",p2)
                winner = p2
        initialScoreboard[winner]["points"] = initialScoreboard[winner]["points"] + 1        
        return winner   

    def turn(startPlayer,secondPlayer,roundCounter,characteristicsSwitcher,spellSwitcher,initialScoreboard,GodFlag):
        print("Play Order, 1st: ",startPlayer," and 2nd: ",secondPlayer )
        
        ## Call Logic function for characteristics selection, Spell
        selectedForRound = {}

        # Start player picks card
        selectedForRound[startPlayer] = selectCharacteristicsNSpell("startPlayer",startPlayer,characteristicsSwitcher,spellSwitcher,initialScoreboard,GodFlag)
        if selectedForRound[startPlayer]["selectedSpell"] == "God":
            cardsForTwo = godSpell()
            cardPicked1 = cardsForTwo[0]
            deckPlayer1.remove(cardPicked1)
            
            cardPicked2 = cardsForTwo[1]
            deckPlayer2.remove(cardPicked2)
        elif selectedForRound[startPlayer]["selectedSpell"] == "Resurrect":
            cardNumber = resurrectSpell(exhaustDeck)
            cardPicked1 = exhaustDeck[cardNumber]
            exhaustDeck.remove(cardPicked1)
        else:    
            cardPicked1 = deckPlayer1[0]
            deckPlayer1.remove(cardPicked1)
            
        print("Turn of ",startPlayer," and the card is: \n")
        pp.pprint(cardPicked1)

        # Comparison characteristics
        # charToCompare = selectedForRound[startPlayer][characteristics]
        charToCompare = selectedForRound.get(startPlayer, {}).get('selectedCharacteristics') # get value from nested dict
        print("characteristics to compare: ",str(charToCompare))
        selectedForRound[startPlayer]["Value"]= cardPicked1[list(cardPicked1)[0]][charToCompare]
        print(selectedForRound)

        # second player picks card
        ## Call Logic function for characteristics selection, Spell
        
        if selectedForRound[startPlayer]["selectedSpell"] == "God":
            # cardPicked2 already picked by opponent
            selectedForRound[secondPlayer]= {}
            selectedForRound[secondPlayer]["Value"]= cardPicked2[list(cardPicked2)[0]][charToCompare]
        else:
            selectedForRound[secondPlayer] = selectCharacteristicsNSpell("secondPlayer",secondPlayer,characteristicsSwitcher,spellSwitcher,initialScoreboard,GodFlag)
            selectedForRound[secondPlayer]["selectedCharacteristics"]= charToCompare
            
            if selectedForRound[secondPlayer]["selectedSpell"] == "Resurrect":
                cardNumber = resurrectSpell(exhaustDeck)
                cardPicked2 = exhaustDeck[cardNumber]
                exhaustDeck.remove(cardPicked2)
                selectedForRound[secondPlayer]["Value"]= cardPicked2[list(cardPicked2)[0]][charToCompare]
            else:    
                cardPicked2 = deckPlayer2[0] # must change accordingly
                deckPlayer2.remove(cardPicked2)
                selectedForRound[secondPlayer]["Value"]= cardPicked2[list(cardPicked2)[0]][charToCompare]            

        print("Turn of ",secondPlayer," and the card is: \n")
        pp.pprint(cardPicked2)    
        
        # Call Comparison of charactersitics logic 
        # declare winner 
        #pass real value of characteristics and weights
        weight = weights[charToCompare]
        winner =  checkWhoWon(selectedForRound,charToCompare,weight,initialScoreboard)
        exhaustDeck.append(cardPicked1)
        exhaustDeck.append(cardPicked2)

        # shuffle exhaustDeck
        random.shuffle(exhaustDeck)
        
        print("Round completed and the player Won is:\n",winner)
        # print("exhaustDeck : ",exhaustDeck)
    
    # generate charactersitics switch case for playing
    characteristicsSwitcher = generateSwitcher(characteristics)            
    print(characteristicsSwitcher)

    # generate spell switch case for playing
    spellSwitcher = generateSwitcher(spells)
    print(spellSwitcher)
       
    playerCycle = cycle(playOrder)
    roundMe = scoreBoard()
    loopUntil = len(deckPlayer1Temp) + len(deckPlayer2Temp)
    while(loopUntil > 2 and roundCounter < rounds+1):
        # The player winnning toss starts first and then the cycle continues
        startPlayer = next(playerCycle)
        secondPlayer = [x for x in playOrder if x != startPlayer][0]
        deckPlayer1 = deckPlayer[startPlayer]
        deckPlayer2 = deckPlayer[secondPlayer]
        GodFlag = True
        roundName = "Round"+str(roundCounter)
        print(roundName)
        
        # Initial spells are 1 each and points start from 0
        initialScoreboard = createScoreboardSkeleton()
        if roundCounter  == 1:        
            spellLeft1 = 1
            spellLeft2 = 1
            points1 = 0
            points2 =0
        else:
            # fetch values from previous round
            previousRound = "Round"+str(roundCounter-1)
            spellLeft1 = roundMe.__dict__["Round"][previousRound][startPlayer]["spellLeft"]
            spellLeft2 = roundMe.__dict__["Round"][previousRound][secondPlayer]["spellLeft"]
            points1 = roundMe.__dict__["Round"][previousRound][startPlayer]["points"]
            points2 = roundMe.__dict__["Round"][previousRound][secondPlayer]["points"]
    
            print(spellLeft1," ",spellLeft2)
            print(points1," ",points2)
        
        # Scoreboard system
        initialScoreboard.addPlayerData(startPlayer,spellLeft1,points1)
        initialScoreboard.addPlayerData(secondPlayer,spellLeft2,points2)
        scoreCardTemp = initialScoreboard.__dict__["scoreboardSkeleton"]
        turn(startPlayer,secondPlayer,roundCounter,characteristicsSwitcher,spellSwitcher,scoreCardTemp,GodFlag)
        
        newData = gameData()
        newData.addValues(**scoreCardTemp)
        roundMe.addRound(roundName,newData.__dict__["stats"])
        scoreCard = roundMe.__dict__["Round"]
        pp.pprint(scoreCard)
        roundCounter+=1
        loopUntil = len(deckPlayer1) + len(deckPlayer2)

    print("Game Over!!!")
    return "Game Over!!!"

## Execution starts from here:
startGame(startDeck,playOrder,roundCounter,characteristics,spells,weights,rounds)