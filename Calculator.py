from tkinter import*
# Tkinter is the standard GUI library for python
import math


root =Tk()
root.title("Calculator")
root.geometry("416x550+500+40")

calc =Frame(root, bd=20, pady=5, bg='gainsboro', relief = RIDGE)
# Frame acts as a container to hold the widgets.
# pady gives how many pixel to pad widget vertically outside the border
calc.grid()
# grid() organizes the wigets(like buttons) in a table like structure in the parent widget

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value =True
        self.check_sum =False
        self.op=""
        self.result= False

    def numberEnter(self, num):
        self.result = False
        firstnum =txtDisplay.get()
        secondnum =str(num)
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
        self.current =float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
            
    def operation(self, op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result=False
        
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "mul":
            self.total *= self.current
        if self.op == "div":
            self.total /= self.current
        self.input_value = True
        self.check_sum= False
        self.display(self.total)

    def Clear_Entry(self):
        self.result = False
        self.current= "0"
        self.display(0)
        self.input_value = True

    def ClearAll_Entry(self):
        self.Clear_Entry()
        self.total=0

    def Delete_it(self):
        numlen = len(txtDisplay.get())
        txtDisplay.delete(numlen -1 ,'end')
        if numlen == 1:
            self.Clear_Entry()
            self.total = 0


    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def squareroot(self):
        self.result= False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current )

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current )

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current )

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current )

    def square(self):
        self.result = False
        self.current = math.pow(float(txtDisplay.get()), 2)
        self.display(self.current )






added_value =Calc()

txtDisplay = Entry(calc, font=('arial', 16, 'bold'), bd=20, width=28, justify =RIGHT)
# Entry is used to input the single line text entry from the user
# justify specifies the side from which the input is taken
txtDisplay.grid(row =0, column =0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad ="789456123"
i=0
btn = []

for j in range (3,6):
    for k in range (3):
        btn.append(Button (calc, width=6, height=2, font=('arial', 16, 'bold'), bd=4, text = numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x = numberpad[i]: added_value.numberEnter(x)
# command tells the function or method tobe called when the button is clicked
        i += 1

# -------------------------------------------------------------------------
btnDelete = Button(calc, width=6, height=2, text="DEL", font=('arial', 16, 'bold'), bd=4, bg="red",
                   command=added_value.Delete_it).grid(row=1, column=0, pady=1)
btnClearAll = Button(calc, width=6, height=2, text="CE", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=added_value.ClearAll_Entry).grid(row=1, column=1, pady=1)
btnlog = Button(calc, width=6, height=2, text="log", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=added_value.log).grid(row=1, column=2, pady=1)
btsquare = Button(calc, width=6, height=2, text="^2", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=added_value.square).grid(row=1, column=3, pady=1)

# -------------------------------------------------------------------------
btnSqroot = Button(calc, width=6, height=2, text="√", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=added_value.squareroot).grid(row=2, column=0, pady=1)
btnCos = Button(calc, width=6, height=2, text="Cos", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=added_value.cos).grid(row=2, column=1, pady=1)
btnSin = Button(calc, width=6, height=2, text="Sin", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=added_value.sin).grid(row=2, column=2, pady=1)
btnTan = Button(calc, width=6, height=2, text="Tan", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=added_value.tan).grid(row=2, column=3, pady=1)

# -------------------------------------------------------------------------
btnAdd = Button(calc, width=6, height=2, text="+", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=lambda :added_value.operation("add")).grid(row=3, column=3, pady=1)
btnSub = Button(calc, width=6, height=2, text="-", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=lambda: added_value.operation("sub") ).grid(row=4, column=3, pady=1)
btnMul = Button(calc, width=6, height=2, text="x", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=lambda: added_value.operation("mul") ).grid(row=5, column=3, pady=1)
btnDiv = Button(calc, width=6, height=2, text="÷", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=lambda :added_value.operation("div")).grid(row=6, column=3, pady=1)


# -------------------------------------------------------------------------
btnZero = Button(calc, width=6, height=2, text="0", font=('arial', 16, 'bold'), bd=4,
                   command=lambda :added_value.numberEnter('0')).grid(row=6, column=0, pady=1)
btnDecimal = Button(calc, width=6, height=2, text=".", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=lambda :added_value.numberEnter('.')).grid(row=6, column=1, pady=1)
btnEqualsTo = Button(calc, width=6, height=2, text="=", font=('arial', 16, 'bold'), bd=4, bg="gainsboro",
                   command=added_value.sum_of_total).grid(row=6, column=2, pady=1)

root.mainloop()
# mainloop() is used when your application is ready to run. mainloop() is an infinite loop
# used to run the application, wait for an event to occur and process the event as long as the window is not closed.

# Working of the operation function
# Let's say we want to perform 10+2=12 operation.When we enter 1 numberEnter(1) function will be called.
# self.result will be false,firstnum will be 1,secondnum will be 1.self.input_value is true so self.current will be 1
# self.input_value will be changed to false ,1 will be displayed
# When we enter 0 numberEnter(0) function will be called.
# firstnum will be 1,secondnum will be 0.self.input_value is false.self.current will become 10 which will be displayed.
# when the add operator button is pressed operation function will be called.op will be add.
# self.check_sum is false, self.result is false so self.total will become 10.self.input_value and self.check_sum will become true
# self.op will be add.When will enter 2,numberEnter function will be called.self.current will be 2 which will be displayed.
# when = is pressed slef.result will become true.As self.checksum is true valid_function will be called.

