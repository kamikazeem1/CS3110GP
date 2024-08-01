from UFA import UFA

def display(filename):
    print("\n\nInputted Finite State Automaton Info:")
    with open(filename, "r") as f:

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
            print(f"{currentState} {symbol} {nextState}")
            transition = f.readline().strip()

        fa = UFA(Q, A, E, d)
        print("Results of test strings:")
        for teststring in f:
            teststring = teststring.strip()
            if teststring:
                print(f"{teststring}\t{fa.process(teststring)}")
            else:
                print(f"Empty string\t{fa.process('')}")


display("M1input.txt")
display("M2input.txt")
display("M3input.txt")
display("M4input.txt")