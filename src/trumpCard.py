########################################
#    Data Loading and Deck Creation    #
########################################
import csv
from pathlib import Path

# Create trump card data from csv
def _createTrumpCardDeck(csvFile):
    deck = []
    with open(csvFile,encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # print(dict(row).keys())
            row = dict(row)
            player = row['Player']
            # player = trumpCard()
            newDict = {}
            row.pop('Player', None) 
            newDict[player] = row
            # newDict[player] = resultset
            # print(newDict)
            deck.append(newDict)

    return deck
    
base_path = Path(__file__).parent
file_path = (base_path / "../data/trumpCard.csv").resolve()
deck = _createTrumpCardDeck(file_path)

# class trumpCard:
#     def __init__(self):
#         self.characteristics = {}

#     def addCharacteristic(self,typeChar,passedValue):
#         self.characteristics[typeChar] = passedValue

# undertaker = trumpCard()
# undertaker.addCharacteristic("rank",3)
# undertaker.addCharacteristic("winPercentage",66)
# undertaker.addCharacteristic("weight",328)  
# deck['undertaker'] = undertaker

# johnCena = trumpCard()
# johnCena.addCharacteristic("rank",1)
# johnCena.addCharacteristic("winPercentage",71)
# johnCena.addCharacteristic("weight",251)  
# deck['johnCena'] = johnCena

# print(deck.items())
# print("deck  ",deck['johnCena'].characteristics)
# print("deck  ",deck['undertaker'].characteristics)