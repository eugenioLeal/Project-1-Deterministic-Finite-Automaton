# Read .txt file
print("Reading Text File....")
with open("DFA.txt", 'r') as fileStream:
    # Reading each line and storing first 4 lines in lists
    states = fileStream.readline().split(',')
    alphabet = fileStream.readline().split(',')
    initialState = fileStream.readline().split(',')
    acceptingStates = fileStream.readline().split(',')
    # Keep reading file until the last line and save all the transition Functions
    transitionFunctions = []
    for line in fileStream:
        transitionFunctions.append(line.split(','))
fileStream.close()

# This lines remove the \n (the last element) of each list
states = states[:-1]
alphabet = alphabet[:-1]
initialState = initialState[:-1]
acceptingStates = acceptingStates[:-1]
row = 0;
while row < len(transitionFunctions):
    transitionFunctions[row] = transitionFunctions[row][:-1]
    row += 1

# Printing all the data gathered from the file
def printData():
    print("States = ", states)
    print("Alphabet = ", alphabet)
    print("Initial State = ", initialState)
    print("Accepting States = ", acceptingStates)
    # We need to read all the transition functions from the file
    print("Transition Functions = ", transitionFunctions)
# Comment/Uncomment printData() to Hide/Show the data gathered from the file
printData()

# Building a dictionary with "dictionary values" (dictionary of dictionaries) where the first keys are the states of the DFA
# example of DFA with two states: DFA = { 'current_state1': {'transition': next_state}, 'current_state2': {'transition': next_state} }
# for example DFA[0]['a'] returns the value of the next state, starting from
# 0 and making a transition with 'a'
DFA = {}

# Creating nested dictionaries for each state
for i in states:
    DFA[i] = {}
# Assigning nested keys and values
for i in transitionFunctions:
    DFA[i[0]][i[1]] = i[2]

print("DFA: ", DFA)


def accepts(dfa, initial, accepting, String):
    # initializing the value of current state as initial
    state = initial
    for c in String:
        # c represents value of alphabet in this case (a or b)
        state = dfa[state][c]
    # if the last transition is in one of the accepting states return true
    return state in accepting

keepChecking = True
while keepChecking :
    String = input("Enter a string to be checked by DFA: ")
    if accepts(DFA, initialState[0], acceptingStates, String) :
        print("accepted")
    else:
        print("rejected")
    continueChecking = input("Do you want to try with another string? (y/n) ")
    if continueChecking != 'y' or continueChecking != "yes" or continueChecking != "Y" or continueChecking != "YES":
        keepChecking = False
