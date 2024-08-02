

from UFA import UFA

def display(filename):

    with open(filename, "r") as f:

        print(f"\n\nFA Description: {f.readline().strip()}")
        print("Inputted Finite State Automaton Info:\n")

        Q = {str(i) for i in range(int(f.readline()))}
        print(f"1) Set of states: {Q}, initial state is state 0 (default)")

        A = set(f.readline().split())
        print(f"2) Set of final state(s): {A}")

        E = set(f.readline().split())
        print(f"3) Alphabet set: {E}")
        
        d = {}
        print("4) Transitions:")
        transition = f.readline().strip()
        while transition and transition[0] == '(':
            elements = transition.strip("()").split()
            currentState, symbol, nextState = elements
            key = (currentState, symbol)
            if key in d:
                d[key].add(nextState)
            else:
                d[key] = {nextState}
            print(f"\t{currentState} {symbol} {nextState}")
            transition = f.readline().strip()

        fa = UFA(Q, A, E, d)
        print("\nResults of test strings:\n")
        maxLength = 0
        empty = "Empty string"
        ts = []
        for teststring in f:
            ts.append(teststring.strip())
            maxLength = len(teststring) if len(teststring) > maxLength else maxLength
        
        for teststring in ts:
            if teststring:
                print(f"{teststring:<{maxLength+2}}\t{fa.process(teststring)}")
            else:
                print(f"{empty:<{maxLength+2}}\t{fa.process('')}")

display("M1input.txt")
display("M2input.txt")
display("M3input.txt")
display("M4input.txt")
display("original1.txt")
display("original2.txt")
display("original3.txt")
display("original4.txt")
