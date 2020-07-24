from unittest import TestCase, main
from T7 import T7


class Test_T7(TestCase):
    def test_STi(self):
        t7.accumulator = 14
        t7.STi(10)
        self.assertEqual(t7.memory[10], t7.accumulator, "Function STi failed, incorrect data/address in memory")

        t7.STi(10)
        self.assertNotEqual(t7.memory[11], t7.accumulator, "Function STi failed, incorrect data/address in memory")

    def test_INP(self):
        t7.INP(2, 10)
        self.assertEqual(t7.memory[10], 2, "Function INP failed, incorrect data/address in memory")

    def test_LDi(self):
        t7.memory[4] = 2
        t7.LDi(4)
        self.assertEqual(t7.accumulator, t7.memory[4], "Function STi failed, incorrect data/address in memory")

    def test_ADD(self):
        t7.accumulator = 10
        t7.memory[1] = 2
        self.assertEqual(t7.ADD(t7.accumulator, 1), 12, "Wrong result!")
        self.assertNotEqual(t7.ADD(t7.accumulator, 1), 8, "Right result but it was suppost to fail!")

    def test_SUB(self):
        t7.accumulator = 10
        t7.memory[1] = 2
        self.assertEqual(t7.SUB (t7.accumulator, 1), 8, "Wrong result!")
        self.assertNotEqual(t7.SUB (t7.accumulator, 1), 12, "Right result but it was suppost to fail!")

    def test_COPY(self):
        t7.memory[10] = 30
        t7.memory[20] = 40
        t7.COPY(10, 20)
        self.assertEqual(t7.memory[10], t7.memory[20], "Function COPY failed, incorrect data/address in memory")

    def test_BVS(self):
        t7.accumulator = 3
        t7.pc.counter = 3
        t7.BVS(7)
        self.assertNotEqual(t7.pc.counter, t7.pc.counter + 1, "Function BVS failed, incorrect result")

        t7.accumulator = 0
        t7.BVS(7)
        self.assertEqual(t7.pc.counter, 7, "Function BVS failed, incorrect result")

    def test_COPY_PC(self):
        t7.CopyPC(10)
        self.assertEqual(t7.memory[10], t7.pc.counter - 1, "Function CopyPC failed, incorrect copy in memory")

    def test_JUMP(self):
        t7_processor = T7("instructions_t7.txt")
        jump_position = 4
        check_error = 0
        self.assertEqual(check_error, t7_processor.JUMP(jump_position), "Function JUMP failed, incorrect Index")

    def test_getCurrentInstruction(self):
        t7_processor = T7("instructions_t7.txt")
        self.assertEqual(t7_processor.getCurrentInstruction(), t7_processor.pc.instructions[t7_processor.pc.counter].split(" "), "Function getCurrentInstruction failed, incorrect instruction")

    def test_getNumberOfInstructions(self):
        t7_processor = T7("instructions_t7.txt")
        #Getting correct number of instructions
        with open("instructions_t7.txt", "r") as file:
            file_data = file.readlines()
        file_data = [line.strip("\n") for line in file_data]
        number_of_instructions = len(file_data)

        self.assertEqual(number_of_instructions,t7_processor.getNumberOfInstructions(),"Function getNumberOfInstructions failed, number of instructions do not match")

t7 = T7("instructions_t7.txt")
# t7.Dump()

if __name__ == "__main__":
    main()