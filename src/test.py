#########################################
#  Just to test out functions(IGNORE)   #
#########################################

from itertools import cycle
from trumpCard import deck
import pprint
import random

playOrder =["P1","P2"]
myIterator = cycle(playOrder)

pp = pprint.PrettyPrinter(indent=4)

# positions = cycle([1,2,3,4])
# print(next(positions))

# length = 10
# while(length>0):
#     print(next(myIterator))
#     length=length-1


def chooseMove(argument):
        switcher = {
        0: "God",
        1: "Resurrect",
        }
        return switcher.get(argument, "nothing")

# print(chooseMove(10))

# print([x for x in playOrder if x != "P1"][0]  )

# all the characteristics
# characteristics = [x for x in x deck[0].values]
x = dict(deck[0]).values()
# print([*[v for k,v in dict(deck[0]).items()][0]])

characteristics = [*[v for k,v in dict(deck[0]).items()][0]]

# switcher = {}
# switchInteger = 0
# def generateSwitcher(characteristics):
#     switcher = {}
#     switchInteger = 0
#     iterationCount = len(characteristics)
#     # print(iterationCount)
#     while(switchInteger < iterationCount):
#         # print(switchInteger)
#         # switcher[switchInteger] = characteristics[switchInteger]
#         switcher[characteristics[switchInteger]] = switchInteger 
#         switchInteger = switchInteger + 1
#     return switcher


# switcher = generateSwitcher(characteristics)        
# print(switcher)

# def strengthWeights(characteristics):
#     print("This will help assign weight of the characteristics \n High the better or Low the better \n")
#     newDict = {}
#     print("Assign 0 for the lower the better OR Assign 1 for the higher the better")
#     for characteristic in characteristics:
#         print("Characteristic: ",characteristic)
#         characteristicWeight = int(input("0 or 1 ? \n"))
#         newDict[characteristic] = characteristicWeight
#     return newDict

# new = strengthWeights(characteristics)
# print(new)



characteristicsSwitcher = {'Rank': 0, 'Weight': 1, 'Height': 2, 'FinishingMovePower': 3, 'Championship': 4, 'WinPercentage': 5}
spellSwitcher ={'God': 0, 'Resurrect': 1}
def selectCharacteristicsNSpell(player,characteristicsSwitcher,spellSwitcher):
        selected = {}
        if(player == "startPlayer"):
            print("The following are the available characteristics, select the number \n")
            pp.pprint(characteristicsSwitcher)
            selectedCharacteristicsInt = input("Which characteristics do you want to Choose? \n ")
            # characteristics = [key  for (key, value) in characteristicsSwitcher.items() if value == selectedCharacteristicsInt][0]
            
            # check the input range should not exceed
            selected["selectedCharacteristics"] = characteristics[int(selectedCharacteristicsInt)]

        # check conditions for 2nd player
        # cannot use God spell if the 1st player uses it
        answer = input("Do you want to use any spell? y/n \n")
        # check the input; only y and n allowed
        if(answer.lower() == "y"):    
            print("The following are the available characteristics, select the number \n")
            pp.pprint(spellSwitcher)
            selectedSpell = input("Which spell do you want to Choose? \n ")
            # check the input range should not exceed
            selected["selectedSpell"] = selectedSpell

        return selected

# selectedForRound = selectCharacteristicsNSpell("startPlayer",characteristicsSwitcher,spellSwitcher)        
# print(selectedForRound)

# example_dict = {"Sarthak":{"Office":"ABB","Job":"yes"}}
# print(example_dict.get('Sarthak', {}).get('Office'))


# deckPlayer1 = []
# deckPlayer2 = []
# for card in deck:
#     # print(deck.index(card))
#     if(deck.index(card)%2 ==0):
#         deckPlayer1.append(card)
#     else:
#         deckPlayer2.append(card)     

# pp.pprint(deckPlayer1)

# pp.pprint(deckPlayer2)
# print(deck)


# p1 = input("Player 1's name  : ")
# p2 = input("Player 2's name  : ")

# #check duplicate player names
# def checkDuplicateNaming(p1,p2):
#     if(p1 == p2):
#         print("Names cannot be same \n")
#         p2 = input("Player 2's name  : ")
#         return checkDuplicateNaming(p1,p2)
#     else:
#         print("Let's play ",p1," and ",p2)
#     return p2    

# p2 = checkDuplicateNaming(p1,p2)    

# # Dice
# dice = [1,2,3,4,5,6]

# # Toss to start the game with the winner of the toss
# def rollADice(p1,p2):
#     toss = {}
#     # playOrder = []
#     toss[p1] = random.choice(dice)
#     print(p1,"'s dice  is ",toss[p1])
#     toss[p2] = random.choice(dice)
#     print(p2,"'s dice  is ",toss[p2])

#     if(toss[p1] == toss[p2]):
#         print("Equal, so toss again!")
#         playOrderList = []
#         return rollADice(p1,p2)
#     elif(toss[p1]< toss[p2]):
#         print(p2,"Wins toss! and will start the game \n")
#         # winner = p2
#         playOrderList = [p2,p1]
#     elif(toss[p1]> toss[p2]):
#         print(p1,"Wins toss! and will start the game \n")
#         # winner = p1 
#         playOrderList = [p1,p2]

#     return playOrderList

# playOrder = rollADice(p1,p2) # Doubt: How to call function recursively and store the returned varriable?
# print(playOrder)
