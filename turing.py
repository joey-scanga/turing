
def getTuples():
    print("Enter 5 tuples (format: A01RB, B 1RC, etc.) Press '.' to end.")
    tuples = []
    running = True
    while running:
        userInput = input()
        if userInput == '.':
            running = False
        elif len(userInput) == 5 and (userInput[3] == 'r' or userInput[3] == 'R' or userInput[3] == 'l' or userInput[3] == 'L' or userInput[3] == 'N' or userInput[3] == 'n'):
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
    #Sets the starting tape index, as well as the starting key (the first one entered by the user)
    currentTapeIndex = 0
    startingTupleKey = None
    for x in tupleDict.keys():
        if x == tupleDict["StartingTupleKey"]:
            startingTupleKey = x
            break
    
    currentTupleKey = startingTupleKey
    for i in range(0, limit):
        foundTuple = False
        for tuple in tupleDict[currentTupleKey]:

            #Checks if the tuple's "read" character matches the one on the tape.
            if tuple[1] == '*':
               
                foundTuple = True
                if tuple[2] != '*':
                    tape[currentTapeIndex] = tuple[2]
                    
                #If the tuple moves the pointer to the right, this will check if 
                #the array is long enough to do that; if not, it will append 10 
                #blank characters to the right of the tape.
                if tuple[3] == 'R' or tuple[3] == 'r':
                    try:
                        currentTapeIndex += 1
                    except IndexError:
                        tape.append(' ')
                        #currentTapeIndex += 1
                #Since Python takes negative indexes and uses them to show the
                #last item in a list (instead of throwing an error), if the
                #pointer goes past the left of the array, 10 blank characters will
                #be added to the left.
                elif tuple[3] == 'L' or tuple[3] == 'l':
                    currentTapeIndex -= 1
                    if currentTapeIndex < 0:
                        newTape = [' ']
                        for character in tape:
                            newTape.append(character)
                        tape = newTape
                        currentTapeIndex = currentTapeIndex + 10
                else:
                    pass
                #Prints tape in readable format.
                tapeString = ' '.join(map(str, tape))
                print("{"+currentTupleKey+"}"+tapeString)
                #The pointerTape draws an arrow to where the current tape index is
                #at the end of an instruction.
                pointerTape = tape.copy()
                for j in range(0, len(pointerTape)):
                    if j == currentTapeIndex:
                        pointerTape[j] = '^'
                    else:
                        pointerTape[j] = ' '
                print('   '+' '.join(map(str, pointerTape)))
                noKeyFound = True
                finalState = currentTupleKey
                #Checks to see if there are any valid instructions left; if not, the
                #machine will halt. 
                for k in tupleDict.keys():
                    if k == tuple[4]:
                        currentTupleKey = tuple[4]
                        noKeyFound = False
                if noKeyFound:
                    print("Halted!")
                    print("Final state: "+finalState)
                    return
                #Checks if max iterations have been reached.
                if i == limit - 1:
                    print("Ended: max iterations reached")
                    print("Final state: "+finalState)
                break
            elif tuple[1] == tape[currentTapeIndex]:
               
                foundTuple = True
                if tuple[2] != '*':
                    tape[currentTapeIndex] = tuple[2]
                  
                #If the tuple moves the pointer to the right, this will check if 
                #the array is long enough to do that; if not, it will append 10 
                #blank characters to the right of the tape.
                if tuple[3] == 'R' or tuple[3] == 'r':
                    try:
                        currentTapeIndex += 1
                    except IndexError:
                        tape.append(' ')
                        #currentTapeIndex += 1
                #Since Python takes negative indexes and uses them to show the
                #last item in a list (instead of throwing an error), if the
                #pointer goes past the left of the array, 10 blank characters will
                #be added to the left.
                elif tuple[3] == 'L' or tuple[3] == 'l':
                    currentTapeIndex -= 1
                    if currentTapeIndex < 0:
                        newTape = [' ']
                        for character in tape:
                            newTape.append(character)
                        tape = newTape
                        currentTapeIndex = currentTapeIndex + 10
                else:
                    pass
                #Prints tape in readable format.
                tapeString = ' '.join(map(str, tape))
                print("{"+currentTupleKey+"}"+tapeString+"{"+tuple[4]+"}")
                #The pointerTape draws an arrow to where the current tape index is
                #at the end of an instruction.
                pointerTape = tape.copy()
                for j in range(0, len(pointerTape)):
                    if j == currentTapeIndex:
                        pointerTape[j] = '^'
                    else:
                        pointerTape[j] = ' '
                print('   '+' '.join(map(str, pointerTape)))
                noKeyFound = True
                finalState = currentTupleKey
                #Checks to see if there are any valid instructions left; if not, the
                #machine will halt. 
                for k in tupleDict.keys():
                    if k == tuple[4]:
                        currentTupleKey = tuple[4]
                        noKeyFound = False
                if noKeyFound:
                    print("Halted!")
                    print("Final state: "+finalState)
                    return
                #Checks if max iterations have been reached.
                if i == limit - 1:
                    print("Ended: max iterations reached")
                    print("Final state: "+finalState)
                break

        if foundTuple == False:
            print("Halted: no valid instruction to continue.")

def main():
    tupleDict = createTupleDictionary(getTuples())
    print(tupleDict)
    limit = setLimit()
    tape = getTape(limit)
    readTape(tupleDict, tape, limit)
    
main()



