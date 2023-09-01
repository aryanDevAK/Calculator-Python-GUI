import tkinter as tk
root = tk.Tk()
root.title("Calculator")

def clearScreen():
    screen_num.delete(0, tk.END)

def button_click(number):
    temp = screen_num.get()
    screen_num.delete(0, tk.END)
    screen_num.insert(0, str(temp) + str(number))

def button_click_add():
    first_number = screen_num.get()
    screen_num.delete(0, tk.END)
    global num, math
    math = "add"
    num = int(first_number)

def button_click_subtract():
    first_number = screen_num.get()
    screen_num.delete(0, tk.END)
    global num, math
    math = "subtract"
    num = int(first_number)

def button_click_multiply():
    first_number = screen_num.get()
    screen_num.delete(0, tk.END)
    global num, math
    math = "multiply"
    num = int(first_number)

def button_click_divide():
    first_number = screen_num.get()
    screen_num.delete(0, tk.END)
    global num, math
    math = "divide"
    num = int(first_number)

def equalTo():
    second_number = screen_num.get()
    screen_num.delete(0, tk.END)

    if math == "add":
        screen_num.insert(0, num + int(second_number))
    if math == "subtract":
        screen_num.insert(0, num - int(second_number))
    if math == "multiply":
        screen_num.insert(0, num * int(second_number))
    if math == "divide":
        screen_num.insert(0, int(num / int(second_number)))

screen_num = tk.Entry(root, width=50, border=5, borderwidth=5, bg="#fff", fg="#000")
screen_num.grid(row=0, column=0, columnspan=4)

button_1 = tk.Button(root, text="1", padx=30, pady=30, border=5, borderwidth=5, command=lambda : button_click(1))
button_2 = tk.Button(root, text="2", padx=30, pady=30, border=5, borderwidth=5, command=lambda : button_click(2))
button_3 = tk.Button(root, text="3", padx=30, pady=30, border=5, borderwidth=5, command=lambda : button_click(3))
button_4 = tk.Button(root, text="4", padx=30, pady=30, border=5, borderwidth=5, command=lambda : button_click(4))
button_5 = tk.Button(root, text="5", padx=30, pady=30, border=5, borderwidth=5, command=lambda : button_click(5))
button_6 = tk.Button(root, text="6", padx=30, pady=30, border=5, borderwidth=5, command=lambda : button_click(6))
button_7 = tk.Button(root, text="7", padx=30, pady=30, border=5, borderwidth=5, command=lambda : button_click(7))
button_8 = tk.Button(root, text="8", padx=30, pady=30, border=5, borderwidth=5, command=lambda : button_click(8))
button_9 = tk.Button(root, text="9", padx=30, pady=30, border=5, borderwidth=5, command=lambda : button_click(9))
button_0 = tk.Button(root, text="0", padx=70, pady=30, border=5, borderwidth=5, command=lambda : button_click(0))
button_point = tk.Button(root, text=".", padx=31, pady=31, border=5, borderwidth=5, command=lambda : button_click("."), state="disabled")
button_equalTo = tk.Button(root, text="=", padx=30, pady=80, border=5, borderwidth=5, command=equalTo)
button_clearScreen = tk.Button(root, text="Clr", padx=26, pady=26, border=5, borderwidth=5, command=clearScreen)
button_add = tk.Button(root, text="+", padx=30, pady=80, border=5, borderwidth=5, command=button_click_add)
button_subtract = tk.Button(root, text="-", padx=30, pady=30, border=5, borderwidth=5, command=button_click_subtract)
button_multiply = tk.Button(root, text="*", padx=30, pady=30, border=5, borderwidth=5, command=button_click_multiply)
button_divide = tk.Button(root, text="/", padx=30, pady=30, border=5, borderwidth=5, command=button_click_divide)

button_0.grid(row=5, column=0, columnspan=2)
button_point.grid(row=5, column=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_equalTo.grid(row=4, column=3, rowspan=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_add.grid(row=2, column=3, rowspan=2)

button_clearScreen.grid(row=1, column=0)
button_divide.grid(row=1, column=1)
button_multiply.grid(row=1, column=2)
button_subtract.grid(row=1, column=3)

root.mainloop()