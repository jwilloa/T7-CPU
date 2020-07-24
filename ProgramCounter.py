class ProgramCounter:
    def __init__(self):
        self.instructions = [None] * 128
        self.counter = 0
        self.number_of_instructions = 0

    def IncrementCounter(self):
        self.counter += 1

    def JumpCounter(self, index):
        try:
            if (index > self.number_of_instructions):
                raise IncorrectJumpException
            else:
                self.counter = index
                return 0
        except IncorrectJumpException:
            print("ERROR: JUMP Function failed, The given index is out of the pc counter range")
            return 1

    def LoadFromFile(self, filename):
        with open(filename, "r") as file:
            file_data = file.readlines()
        file_data = [line.strip("\n") for line in file_data]
        self.number_of_instructions = len(file_data)

        for instruction_number in range(self.number_of_instructions):
            self.instructions[instruction_number] = file_data[instruction_number]

    def GetInstructionAndData(self, index):
        raw_instruction = self.instructions[index]
        instruction_data = raw_instruction.split(" ")
        return instruction_data

class IncorrectJumpException(Exception):
    pass