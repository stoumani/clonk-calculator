from tkinter import END

import customtkinter
import math


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Clonk - Scientific Calculator")
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False
        # width
        self.evwidth = 400
        self.bwidth1 = self.evwidth / 4 - 20

        # colors
        self.configure(fg_color="#181b1f")
        self.obc = "#fb2f64"
        self.obch = "#cc2753"
        self.nbc = "#181b1f"
        self.nbch = "#14161a"

        # values
        self.values = customtkinter.CTkEntry(master=self, width=self.evwidth)
        self.values.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # number buttons
        self.button_1 = customtkinter.CTkButton(master=self, text="1", command=lambda: self.g_num("1"),
                                                width=self.bwidth1,
                                                fg_color=self.nbc, hover_color=self.nbch)
        self.button_2 = customtkinter.CTkButton(master=self, text="2", command=lambda: self.g_num("2"),
                                                width=self.bwidth1,
                                                fg_color=self.nbc, hover_color=self.nbch)
        self.button_3 = customtkinter.CTkButton(master=self, text="3", command=lambda: self.g_num("3"),
                                                width=self.bwidth1,
                                                fg_color=self.nbc, hover_color=self.nbch)
        self.button_4 = customtkinter.CTkButton(master=self, text="4", command=lambda: self.g_num("4"),
                                                width=self.bwidth1,
                                                fg_color=self.nbc, hover_color=self.nbch)
        self.button_5 = customtkinter.CTkButton(master=self, text="5", command=lambda: self.g_num("5"),
                                                width=self.bwidth1,
                                                fg_color=self.nbc, hover_color=self.nbch)
        self.button_6 = customtkinter.CTkButton(master=self, text="6", command=lambda: self.g_num("6"),
                                                width=self.bwidth1,
                                                fg_color=self.nbc, hover_color=self.nbch)
        self.button_7 = customtkinter.CTkButton(master=self, text="7", command=lambda: self.g_num("7"),
                                                width=self.bwidth1,
                                                fg_color=self.nbc, hover_color=self.nbch)
        self.button_8 = customtkinter.CTkButton(master=self, text="8", command=lambda: self.g_num("8"),
                                                width=self.bwidth1,
                                                fg_color=self.nbc, hover_color=self.nbch)
        self.button_9 = customtkinter.CTkButton(master=self, text="9", command=lambda: self.g_num("9"),
                                                width=self.bwidth1,
                                                fg_color=self.nbc, hover_color=self.nbch)
        self.button_0 = customtkinter.CTkButton(master=self, text="0", command=lambda: self.g_num("0"),
                                                width=self.bwidth1,
                                                fg_color=self.nbc, hover_color=self.nbch)

        # displaying number buttons
        self.button_1.grid(row=3, column=0, pady=5, padx=10)
        self.button_2.grid(row=3, column=1, pady=5, padx=10)
        self.button_3.grid(row=3, column=2, pady=5, padx=10)

        self.button_4.grid(row=2, column=0, pady=5, padx=10)
        self.button_5.grid(row=2, column=1, pady=5, padx=10)
        self.button_6.grid(row=2, column=2, pady=5, padx=10)

        self.button_7.grid(row=1, column=0, pady=5, padx=10)
        self.button_8.grid(row=1, column=1, pady=5, padx=10)
        self.button_9.grid(row=1, column=2, pady=5, padx=10)
        self.button_0.grid(row=4, column=0, pady=5, padx=10)

        # operation buttons
        self.add = customtkinter.CTkButton(master=self, text="+", command=lambda: self.operate("+"), width=self.bwidth1,
                                           fg_color=self.obc, hover_color=self.obch)
        self.sub = customtkinter.CTkButton(master=self, text="-", command=lambda: self.operate("-"), width=self.bwidth1,
                                           fg_color=self.obc, hover_color=self.obch)
        self.div = customtkinter.CTkButton(master=self, text="/", command=lambda: self.operate("/"), width=self.bwidth1,
                                           fg_color=self.obc, hover_color=self.obch)
        self.mul = customtkinter.CTkButton(master=self, text="*", command=lambda: self.operate("*"), width=self.bwidth1,
                                           fg_color=self.obc, hover_color=self.obch)
        self.sin = customtkinter.CTkButton(master=self, text="sin", command=lambda: self.operate("math.sin("),
                                           width=self.bwidth1,
                                           fg_color=self.obc, hover_color=self.obch)

        self.equal = customtkinter.CTkButton(master=self, text="=", command=self.evaluate, width=self.bwidth1)
        self.clear = customtkinter.CTkButton(master=self, text="clear", command=self.all_clear, width=self.bwidth1)

        # displaying operation buttons
        self.add.grid(row=1, column=3, pady=5, padx=10)
        self.sub.grid(row=2, column=3, pady=5, padx=10)
        self.div.grid(row=3, column=3, pady=5, padx=10)
        self.mul.grid(row=4, column=3, pady=5, padx=10)
        self.sin.grid(row=5, column=3, pady=5, padx=10)

        self.equal.grid(row=4, column=1, pady=5, padx=10)
        self.clear.grid(row=4, column=2, pady=5, padx=10)

    def g_num(self, n):
        new_n = self.values.get() + n
        self.values.delete(0, customtkinter.END)
        self.values.insert(0, new_n)

    def all_clear(self):
        self.values.delete(0, customtkinter.END)

    def operate(self, o):
        self.f_num = int(self.values.get())
        self.op = o
        self.values.delete(0, customtkinter.END)

    def evaluate(self):
        s_num = int(self.values.get())
        self.values.delete(0, customtkinter.END)

        if self.op == "+":
            self.values.insert(0, self.f_num + s_num)
        elif self.op == "-":
            self.values.insert(0, self.f_num - s_num)
        elif self.op == "*":
            self.values.insert(0, self.f_num * s_num)
        elif self.op == "/":
            self.values.insert(0, self.f_num / s_num)

    def numberEnter(self, num):
        self.result = False
        firstnum = self.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(self.get())

    def display(self, value):
        self.delete(0, END)
        self.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(self.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(self.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(self.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(self.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(self.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(self.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(self.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(self.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(self.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(self.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(self.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(self.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(self.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(self.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(self.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(self.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(self.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(self.get()))
        self.display(self.current)

if __name__ == "__main__":
    app = App()
    app.mainloop()
