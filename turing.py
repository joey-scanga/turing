from collections import OrderedDict

def getTuples():
    print("Enter 5 tuples (format: A01RB, B 1RC, etc.) Press '.' to end.")
    tuples = []
    running = True
    while running:
        userInput = input()
        if userInput == '.':
            running = False
        elif len(userInput) == 5 and (userInput[3] == 'r' or userInput[3] == 'R' or userInput[3] == 'l' or userInput[3] == 'L'):
            tuples.append(userInput)
        else:
            print("Invalid input. \n")
    return tuples

def getTape(limit):
    tape = []
    yn = input("Use a blank tape? (yY or nN): ");
    if yn[0] == 'y' or yn[0] == 'Y':
        for i in range(0, limit):
            tape.append(' ')
        return tape
    elif yn[0] == 'n' or yn[0] == 'N':
        tapeInput = input("Enter tape contents: ")
        for i in range(0, len(tapeInput) - 1):
            tape.append(tapeInput[i])
        return tape
    else:
        print("Invalid input. \n")
        getTape()

def setLimit():
    limit = int(input("Enter the max number of iterations: "))
    return limit

def createTupleDictionary(tuples):
    tupleDict = {}
    for i in range(0, len(tuples)):
        tupleDict[tuples[i][0]] = []
        if(i == 0):
            tupleDict["StartingTupleKey"] = tuples[i][0]
    for tuple in tuples:
        tupleDict[tuple[0]].append(tuple)

    return tupleDict

def readTape(tupleDict, tape, limit):
    currentTapeIndex = 0
    startingTupleKey = None
    for x in tupleDict.keys():
        if x == tupleDict["StartingTupleKey"]:
            startingTupleKey = x
            break
    
    currentTupleKey = startingTupleKey
    for i in range(0, limit):
        for tuple in tupleDict[currentTupleKey]:
            if tuple[1].__str__() == tape[currentTapeIndex]:
                tape[currentTapeIndex] = tuple[2]
                if tuple[3] == 'R' or tuple[3] == 'r':
                    try:
                        currentTapeIndex += 1
                    except IndexError:
                        for j in range(10):
                            tape.append(' ')
                        currentTapeIndex += 1
                else:
                    try:
                        currentTapeIndex -= 1
                    except IndexError:
                        newTape = []
                        for j in range(0, 9):
                            newTape[j] = ' '
                        for j in range(10, len(tape)+9):
                            newTape[j] = tape[j - 10]
                        tape = newTape
                        currentTapeIndex = currentTapeIndex + 10
                        currentTapeIndex -= 1
                tapeString = ' '.join(map(str, tape))
                #print(*tape)
                print(tapeString+"{"+currentTupleKey+"}")
                currentTupleKey = tuple[4]
            else: 
                return
    
def main():
    tupleDict = createTupleDictionary(getTuples())
    print(tupleDict)
    limit = setLimit()
    tape = getTape(limit)
    readTape(tupleDict, tape, limit)
    
main()



