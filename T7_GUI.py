import tkinter as tk
from tkinter import *
from tkinter import filedialog
from Main import Main

class GUI:
    def __init__(self, file):
        self.main = Main(file)

class Design:
    def __init__(self):
        self.root = tk.Tk()
        self.ram_labels = []
        self.mm = None

    def root_Win(self):
        self.root.title("T7 CPU GUI")
        self.root.geometry("550x300+700+300")

        dd.open_File()

        self.textBox = tk.Text(self.root, height=15, width=13)
        self.textBox.place(x=10, y=20)
        self.textBox.insert(END, open(searchFile).read())

        self.buttonOne = Button(self.root, text="Load file", command=dd.update_File)
        self.buttonOne.place(x=10, y=265)
        self.buttonTwo = Button(self.root, text="Run code", command=dd.run_File)
        self.buttonTwo.place(x=80, y=265)

        self.root.mainloop()

    def open_File(self):
        global searchFile
        searchFile = filedialog.askopenfilename()

    def update_File(self):
        self.findText = self.textBox.get("1.0",END)
        self.file = open(searchFile,'wt')
        self.file.write(self.findText)
        self.file.close()

    def run_File(self):
        self.mm = Main(searchFile)
        self.mm.Run_T7_Instructions()
        dd.variables()

    def variables(self):
        self.accumulator_Label = Label(self.root, bg="white", text="Accumulator").place(x=130, y=20)
        self.accumulator_Var = Label(self.root, bg="white", text=self.mm.CPU.accumulator).place(x=220, y=20)

        self.counter_Label = Label(self.root, bg="white", text="Counter").place(x=130, y=40)
        self.counter_Var = Label(self.root, bg="white", text=self.mm.CPU.pc.counter).place(x=220, y=40)

        self.steps_Label = Label(self.root, bg="white", text="Steps").place(x=130, y=60)
        self.steps_Var = Label(self.root, bg="white", text=self.mm.steps).place(x=220, y=60)

        x = 300
        for i in range(20):
            if i < 10:
                self.ram_num = tk.Label(self.root, fg="red", bg="white", text=str(i), height = 1, width = 2)
                self.ram_num.place(x=x, y=20)
                self.ram_labels.append(self.ram_num)
                x+=21
            if i >= 10:
                self.ram_num = tk.Label(self.root, fg="red", bg="white", text=str(i), height = 1, width = 2)
                self.ram_num.place(x=x-210, y=70)
                self.ram_labels.append(self.ram_num)
                x+=21
        x = 300
        for i in range(20):
            if i < 10:
                self.ram_val = tk.Label(self.root, fg="white", bg="dark grey", text=self.mm.CPU.memory[i], height = 1, width = 2)
                self.ram_val.place(x=x, y=40)
                self.ram_labels.append(self.ram_num)
                x+=21
            if i >= 10:
                self.ram_val = tk.Label(self.root, fg="white", bg="dark grey", text=self.mm.CPU.memory[i], height = 1, width = 2)
                self.ram_val.place(x=x-210, y=90)
                self.ram_labels.append(self.ram_num)
                x+=21

dd = Design()
dd.root_Win()




