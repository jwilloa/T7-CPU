from T7 import T7


class Main:
    def __init__(self, instruction_file):
        self.CPU = T7(instruction_file)
        self.steps = 0

    def Run_T7_Instructions(self):
        while self.CPU.isInstructionRemaining():
            instruction = self.CPU.getCurrentInstruction()
            print(instruction)
            command = instruction[0]
            instruction.pop(0)
            args = ",".join(instruction)
            i_string = "self.CPU." + command + "(" + args + ")"
            eval(i_string)
            self.steps += 1


#filename = 'Multiplication_Instructions.txt'
#mm = Main(filename)
#mm.Run_T7_Instructions()
