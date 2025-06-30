#CALCULATOR
from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry('600x300') #creation of window
def Calculate():
    try: 
        num1 = float(entry1.get())
        num2 = float(entry2.get())
    except ValueError:
        result_label.config(text="Enter valid numbers.")
        return
    operation = operation_var.get()
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result_label.config(text="Cannot divide by zero.")
            return
        result = num1/num2
    else:
        result_label.config(text="Select an operation.")
        return
    result_label.config(text=f"Result:{result}")

label1 = Label(window , text="Number 1:",background= 'pink')
label1.config(font=("times new roman",15,"bold"))
label1.grid(row=0,column=0,padx=25,pady=15)
entry1 = Entry(window)
entry1.grid(row=0,column=1,padx=25,pady=15)

label2 = Label(window , text="Number 2:",background= 'pink')
label2.config(font=("times new roman",15,"bold"))
label2.grid(row=1,column=0,padx=25,pady=15)
entry2 = Entry(window)
entry2.grid(row=1,column=1,padx=25,pady=15)

operation_var = StringVar()
operation_var.set("+")

label3 = Label(window , text="Operation:",background= 'pink')
label3.config(font=("times new roman",15,"bold"))
label3.grid(row=2,column=0,padx=10,pady=5)

operations_frame = Frame(window)
operations_frame.grid(row=2, column=1, padx=25, pady=15)
def set_operation(op):
    operation_var.set(op)

button_add = Button(operations_frame,text="+",command= lambda: set_operation("+"),background='lightblue')
button_add.pack(side=LEFT, padx=10)

button_sub = Button(operations_frame,text="-",command= lambda: set_operation("-"),background='lightblue')
button_sub.pack(side=LEFT,padx=10)

button_mul = Button(operations_frame,text="*",command= lambda: set_operation("*"),background='lightblue')
button_mul.pack(side=LEFT,padx=10)

button_div = Button(operations_frame,text="/",command= lambda: set_operation("/"),background='lightblue')
button_div.pack(side=LEFT,padx=10)

submit_button = Button(window, text="Calculate",command=Calculate)
submit_button.config(font=("times new roman",15,"bold"))
submit_button.grid(row=3,column=0,columnspan =2,pady=10)

result_label = Label(window, text="Result:")
result_label.config(font=("times new roman",15,"bold"))
result_label.grid(row=4,column=0,columnspan =2,pady=5)

window.mainloop()








   


