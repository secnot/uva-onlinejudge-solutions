import sys
from itertools import count



def digit(n, num):
    return num%(10**(n+1))//10**n



class Interpreter(object):

    def __init__(self, program):
        self._reg = [0 for r in range(10)]
        self._mem = [0]*1000
        self._pc = 0

        self._instructions = [
                self.i000, self.i100, self.i200,\
                self.i300, self.i400, self.i500,\
                self.i600, self.i700, self.i800, self.i900]

        for n, instruction in enumerate(program):
            self._mem[n] = instruction
        
        self._icounter = 0 # executed instructions count

    def i100(self, op1, op0):
        self._pc = None

    def i200(self, op1, op0):
        self._reg[op1] = op0
        self._pc += 1

    def i300(self, op1, op0):
        self._reg[op1] = (self._reg[op1]+op0)%1000
        self._pc += 1

    def i400(self, op1, op0):
        self._reg[op1] = (self._reg[op1]*op0)%1000
        self._pc += 1

    def i500(self, op1, op0):
        self._reg[op1] = self._reg[op0]
        self._pc += 1

    def i600(self, op1, op0):
        self._reg[op1] = (self._reg[op1]+self._reg[op0])%1000
        self._pc += 1

    def i700(self, op1, op0):
        self._reg[op1] = (self._reg[op1]*self._reg[op0])%1000
        self._pc += 1

    def i800(self, op1, op0):
        self._reg[op1] = self._mem[self._reg[op0]]
        self._pc += 1

    def i900(self, op1, op0):
        self._mem[self._reg[op0]] = self._reg[op1]
        self._pc += 1

    def i000(self, op1, op0):
        if not self._reg[op0]:
            self._pc += 1
        else:
            self._pc = self._reg[op1]

    def decode_execute(self, ins):
        family, op1, op0 = digit(2, ins), digit(1, ins), digit(0, ins)
        self._instructions[family](op1, op0)

    def run(self):

        while self._pc is not None:
            ins = self._mem[self._pc]
            self.decode_execute(ins)
            self._icounter +=1

        return self._icounter


def load_num():
    line = sys.stdin.readline()
    if line in ('', '\n'):
        return None
    else:
        return int(line)


def load_prog(): 
    prog = []

    while True:
        instruction = load_num()
        if instruction is None:
            break

        prog.append(instruction)

    return prog



if __name__ == '__main__':

    # Number of programs
    nprog = load_num()

    # Discard empty line
    sys.stdin.readline()

    for n in range(nprog):

        prog = load_prog()
        inter = Interpreter(prog)
        print(inter.run())

        if n+1 < nprog:
            print('')
