

class UFA:

    def __init__(self, Q, A, E, d):
        self.Q = Q
        self.A = A
        self.E = E
        self.d = d
        self.qi = '0'

    def process(self, inputString):
        
        currentStates = {self.qi}
        exit = False
        symgen = self.NextSymbol(inputString)
        
        while not exit:
            symbol = next(symgen)
            # If symbol is in the alphabet...
            if symbol in self.E:
                # Move to next state
                nextStates = set()
                for state in currentStates:
                    nextStates.update(self.NextState(state, symbol))
                currentStates = nextStates

                # if there is no transition defined, exit loop and reject
                if not currentStates:
                    exit = True
                    return self.Reject()
            # We reach the end of the string OR the symbol is not in the alphabet
            else:
                exit = True
                # If there is a symbol that is not a part of the alphabet,
                # automatically reject
                if symbol:
                    return self.Reject()
                # At the end of the string, accept if current state is an accepting state
                # reject if current state is not an accepting state
                elif currentStates.intersection(self.A):
                    return self.Accept()
                else:
                    return self.Reject()

    def NextState(self, state, symbol):
        return self.d.get((state, symbol), set())

    def Accept(self):
        return "Accept"

    def Reject(self):
        return "Reject"

    def NextSymbol(self, inputString):
        for symbol in inputString:
            yield symbol
        yield None
