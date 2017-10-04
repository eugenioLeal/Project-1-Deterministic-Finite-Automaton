# Esta es una copia del main.py para que puedas probar y que no haya conflictos con
# github en el merge
import csv


print("Reading Text File....")
with open("DFA.txt", 'r') as fileStream:
    # Reading each line and storing it in variables
    states = fileStream.readline()
    alphabet = fileStream.readline()
    initialState = fileStream.readline()
    acceptingStates = fileStream.readline()
    # Keep reading file until the last line and somehow save all the transition Functions
    '''
    # Testing
    transitionFunctions = fileStream.readline()
    for line in fileStream:
        transitionFunctions.append(fileStream.readline())
    '''


fileStream.close()

print("States = ", states)
print("Alphabet = ", alphabet)
print("Initial State = ", initialState)
print("Accepting States = ", acceptingStates)
# We need to read all the transition functions from the file
# print("Transition Function = ", transitionFunctions)



'''
# Testing file i/o
with open('DFA.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    fileList = []
    i = 0
    while i < 3
    next()
    for row in reader:
        print(row)
'''
'''
print("Testing with csv file")
with open('DFA.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(row)
'''
'''
print("\n")
f = open("DFA.csv", newline='')
for row in csv.reader(f):
    print(row)
'''
