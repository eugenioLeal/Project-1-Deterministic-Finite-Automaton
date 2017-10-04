# DFA que acepta numero par de a's

# dictionary where keys are the states and alphabet values
# for example DFA[0]['a'] returns the value of the next state, starting from 0 and making a transition with 'a'
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
