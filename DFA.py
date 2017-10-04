# Team Message:
# This code is an implementation of a DFA
# To make this implementation work in our main.py file we need to generate the dictionary keys and
# values when reading the file

# Implementation of DFA that accepts even number of a's

# dictionary with "dictionary values" where keys are the states of the DFA
# for example DFA[0]['a'] returns the value of the next state, starting from
# 0 and making a transition with 'a'
DFA = { 0:{'a':1, 'b':0},
        1:{'a':0, 'b':1} }


def accepts(dfa,initial,accepting,String):
    # initializing the value of current state as initial
    state = initial
    for c in String:
        # c represents value of alphabet in this case (a or b)
        state = dfa[state][c]
    # if the last transition is in one of the accepting states return true
    return state in accepting

print("accepts \"aab\"", accepts(DFA,0,{0},'aab'))
print("accepts \"a\"", accepts(DFA,0,{0},'a'))
print("accepts \"aabaa\"", accepts(DFA,0,{0},'aabaa'))
