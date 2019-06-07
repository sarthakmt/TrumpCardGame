############################
#    Scoreboard Sytem      # 
############################

import pprint
import inspect

pp = pprint.PrettyPrinter(indent=4)

# Scorecard Class
class scoreBoard:
    # initialization of round
    def __init__(self):
        self.Round ={}

    # adding subsequent rounds
    def addRound(self,roundNum,addAllStatsOfGame):
        self.Round[roundNum] = addAllStatsOfGame
        return self.Round
    
# Game related data
class gameData:
    def __init__(self):
        self.stats = {}

    # Create a dictionary from the game values
    def addValues(self,**gameData):
        for key,value in gameData.items():
            self.stats[key] = value 
        return self.stats    

# The initial framework of spell and point related data per person per round 
class createScoreboardSkeleton:
    def __init__(self):
        self.scoreboardSkeleton = {}

    def addPlayerData(self,player,spellLeft,points):
        self.scoreboardSkeleton[player] = {}
        self.scoreboardSkeleton[player]["spellLeft"] = spellLeft
        self.scoreboardSkeleton[player]["points"] = points
        return self.scoreboardSkeleton

        


# demoPlayBoard = {
# 	"Round1": {
# 		"S": {
# 			"spellLeft": 1,
# 			"points": 0
# 		},
# 		"Z": {
# 			"spellLeft": 1,
# 			"points": 0
# 		}
# 	}
# }

# # newBoard = scoreBoard()
# X = {
# 		"S": {
# 			"spellLeft": 1,
# 			"points": 0
# 		},
# 		"Z": {
# 			"spellLeft": 1,
# 			"points": 1
# 		}
# 	}

# X1 = {
# 		"M": {
# 			"spellLeft": 1,
# 			"points": 0
# 		},
# 		"Z": {
# 			"spellLeft": 1,
# 			"points": 1
# 		}
# 	}


#TEST
# initialScoreboard = createScoreboaardSkeleton()
# initialScoreboard.addPlayerData("S",1,0)
# initialScoreboard.addPlayerData("Z",1,1)
# scorecard1 = initialScoreboard.__dict__["scoreboardSkeleton"]

# roundMe = scoreBoard()
# newData = gameData()
# newData.addValues(**scorecard1)
# roundMe.addRound("Round1",newData.__dict__["stats"])

# print(roundMe.__dict__["Round"])

