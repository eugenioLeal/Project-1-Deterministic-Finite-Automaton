# Message:
# This code is a working implementation of a DFA
# To make this implementation work in our main.py file we need to generate the dictionary keys and
# values when reading the file
# status : completed

# This implementation uses dictionary with "dictionary values" where the first keys are the states of the DFA
# for example DFA[0]['a'] returns the value of the next state, starting from
# 0 and making a transition with 'a'
# DFA that accepts even number of a's
even_A_DFA = { 0:{'a':1, 'b':0},
               1:{'a':0, 'b':1} }
# DFA that accepts odd number of 1's
odd_1_DFA = { 0:{'1':1, '0':0},
              1:{'1':0, '0':1} }
# DFA that accepts the chain "aab" as a subchain
subchain_aab_DFA = {0:{'a':1, 'b':0, 'c':0},
                    1:{'a':2, 'b':0, 'c':0},
                    2:{'a':2, 'b':3, 'c':0},
                    3:{'a':3, 'b':3, 'c':3} }


def accepts(dfa, initial, accepting, String):
    # initializing the value of current state as initial
    state = initial
    for c in String:
        # c represents value of alphabet in this case (a or b)
        state = dfa[state][c]
    # if the last transition is in one of the accepting states return true
    return state in accepting

print("even_A_DFA accepts \"aab\" ?", accepts(even_A_DFA,0,{0},'aab'))
print("even_A_DFA accepts \"a\" ?", accepts(even_A_DFA,0,[0],'a'))
print("even_A_DFA accepts \"aabaa\" ?", accepts(even_A_DFA,0,{0},'aabaa'))

# The diffference between even_A_DFA and odd_1_DFA in accepts() function is the accept states (third parameter)
# accepted states = estados finales
print("odd_1_DFA accepts \"000001000101\" ?", accepts(odd_1_DFA,0,{1},'000001000101'))

print("subchain_aab_DFA accepts \"aabaa\" ?", accepts(subchain_aab_DFA,0,{3},'aabaa'))
print("subchain_aab_DFA accepts \"aaaabbb\" ?", accepts(subchain_aab_DFA,0,{3},'aabaa'))
