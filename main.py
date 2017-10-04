import csv


print("Reading Text File....")
with open("DFA.txt", 'r') as fileStream:
    states = fileStream.readline()
    alphabet = fileStream.readline()
    initialState = fileStream.readline()
    acceptingStates = fileStream.readline()
    transitionFunction = fileStream.readline()
    for line in fileStream:
        transitionFunction.append(fileStream.readline())

    # for i, line in enumerate(fileStream):
    #     # we need to read the file with comma delimiter
    #     # and use the values
    #     if i == 1:
    #         print("line 1: ")
    #         line1 = line.split(",")
    #     # this separates each line to an array


fileStream.close()

print("States = ", states)
print("Alphabet = ", alphabet)
print("Initial State = ", initialState)
print("Accepting States = ", acceptingStates)
print("Transition Function = ", transitionFunction)


'''
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
