############################################
#      All generic utilities in here       #  
############################################

# SwitchCase generator
def generateSwitcher(characteristics):
    switcher = {}
    switchInteger = 0
    iterationCount = len(characteristics)
    # print(iterationCount)
    while(switchInteger < iterationCount):
        # print(switchInteger)
        switcher[characteristics[switchInteger]] = switchInteger 
        switchInteger = switchInteger + 1
    return switcher

# Manual assignments of weights to each characteristics
def strengthWeights(characteristics):
    print("This will help assign weight of the characteristics \n High the better or Low the better \n")
    newDict = {}
    print("Assign 0 for the lower the better OR Assign 1 for the higher the better")
    for characteristic in characteristics:
        print("Characteristic: ",characteristic)
        characteristicWeight = int(input("0 or 1 ? \n"))
        newDict[characteristic] = characteristicWeight
    return newDict     