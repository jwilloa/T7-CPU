from ProgramCounter import ProgramCounter


class T7:
    def __init__(self, instruction_file):
        self.memory = [0] * 128
        self.memory[0] = 1
        self.accumulator = 0
        self.pc = ProgramCounter()
        try:
            self.pc.LoadFromFile(instruction_file)
        except:
            print("There a problem reading the instruction file")

    def getCurrentInstruction(self):
        return self.pc.GetInstructionAndData(self.pc.counter)

    def getNumberOfInstructions(self):
        return self.pc.number_of_instructions

    def isInstructionRemaining(self):
        if self.pc.counter != self.getNumberOfInstructions():
            return True
        else:
            return False

    def INP(self, value, address):
        self.memory[address] = value
        self.pc.IncrementCounter()

    def STi(self, address):
        self.memory[address] = self.accumulator
        self.pc.IncrementCounter()

    def LDi(self, address):
        try:
            self.accumulator = self.memory[address]
            self.pc.IncrementCounter()
        except:
            print("LDi function failed")

    def ADD(self, address):
        self.accumulator += self.memory[address]
        self.pc.IncrementCounter()
        return self.accumulator

    def SUB(self, address):
        self.accumulator -= self.memory[address]
        self.pc.IncrementCounter()
        return self.accumulator

    def BVS(self, index):
        try:
            if index > self.pc.number_of_instructions:
                raise OutofBoundsIndexPC
            elif self.accumulator == 0:
                self.pc.JumpCounter(index)
            else:
                self.pc.IncrementCounter()
        except OutofBoundsIndexPC:
            print("ERROR: The given index is out of the pc counter range")

    def JUMP(self, index):
        return self.pc.JumpCounter(index)

    def COPY(self, address1, address2):
        self.memory[address2] = self.memory[address1]
        self.pc.IncrementCounter()

    def CopyPC(self, address):
        self.memory[address] = self.pc.counter
        self.pc.IncrementCounter()

    def Dump(self):
        print('===============================================================')
        print('T7 Programme Debuggers')
        print('===============================================================\n')
        print('The Main Memory has ' + str(len(self.memory)) + ' bits:')
        counter = 0
        for address, item in enumerate(self.memory):
            if item != 0:
                print('address[' + str(address) + '] = value: ' + str(item))
                counter += 1
        if counter == 0:
            print("The Main Memory is completely empty")
        elif counter <= len(self.memory):
            print('\nAll other addresses in the Memory are empty')

        print('---------------------------------------------------------')
        print('CPU Accumulator:')
        print('Accumulator: ' + str(self.accumulator))

        # print('\n')
        print('---------------------------------------------------------')
        # print('\n')
        print('Program Counter:')
        for item in self.pc.instructions:
            if item is not None:
                print(item)
        print('\nCurrent Counter of PC: ' + str(self.pc.counter))
        self.pc.IncrementCounter()


class IncorrectJumpException(Exception):
    pass


class OutofBoundsIndexPC(Exception):
    pass