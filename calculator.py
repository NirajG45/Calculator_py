import tkinter as tk

# Calculator functions
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))  # eval() expression ko calculate karta hai
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Main window
cal = tk.Tk()
cal.title("Calculator")
cal.geometry("300x400")

expression = ""
input_text = tk.StringVar()

# Input field
input_frame = tk.Frame(cal, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # internal padding

# Buttons frame
btns_frame = tk.Frame(cal, width=312, height=272.5, bg="grey")
btns_frame.pack()

# First row
clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=btn_clear)
clear.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: btn_click("/"))
divide.grid(row=0, column=3, padx=1, pady=1)

# Second row
btn_7 = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(7))
btn_7.grid(row=1, column=0, padx=1, pady=1)

btn_8 = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(8))
btn_8.grid(row=1, column=1, padx=1, pady=1)

btn_9 = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(9))
btn_9.grid(row=1, column=2, padx=1, pady=1)

multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: btn_click("*"))
multiply.grid(row=1, column=3, padx=1, pady=1)

# Third row
btn_4 = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(4))
btn_4.grid(row=2, column=0, padx=1, pady=1)

btn_5 = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(5))
btn_5.grid(row=2, column=1, padx=1, pady=1)

btn_6 = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(6))
btn_6.grid(row=2, column=2, padx=1, pady=1)

subtract = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: btn_click("-"))
subtract.grid(row=2, column=3, padx=1, pady=1)

# Fourth row
btn_1 = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(1))
btn_1.grid(row=3, column=0, padx=1, pady=1)

btn_2 = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(2))
btn_2.grid(row=3, column=1, padx=1, pady=1)

btn_3 = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(3))
btn_3.grid(row=3, column=2, padx=1, pady=1)

add = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: btn_click("+"))
add.grid(row=3, column=3, padx=1, pady=1)

# Fifth row
btn_0 = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0))
btn_0.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

dot = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("."))
dot.grid(row=4, column=2, padx=1, pady=1)

equal = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=btn_equal)
equal.grid(row=4, column=3, padx=1, pady=1)

cal.mainloop()
