from tkinter import *
import math

root = Tk()
root.title('Diogo_s Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column= 0, columnspan=4, padx=20, pady=20)


def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = 'addition'
	f_num = int(first_number)
	e.delete(0,END)
	
def button_equal():
	second_number = e.get()
	e.delete(0, END)
	if math == 'addition':
		e.insert(0, f_num + int(second_number))
	elif math == 'subtraction':
		e.insert(0, f_num - int(second_number))
	elif math == 'division':
		e.insert(0, f_num / int(second_number))
	elif math == 'multiplication': 
		e.insert(0, f_num * int(second_number))
	else: print('Introduza primeiros um numero!')

def button_sub():	
	first_number = e.get()
	global f_num
	global math
	math = 'subtraction'
	f_num = int(first_number)
	e.delete(0,END)

def button_div():
	first_number = e.get()
	global f_num
	global math
	math = 'division'
	f_num = int(first_number)
	e.delete(0,END)

def button_times():
	first_number = e.get()
	global f_num
	global math
	math = 'multiplication'
	f_num = int(first_number)
	e.delete(0,END)

def button_sqrt():
	first_number = e.get()
	e.delete(0, END)
	sqrt = float(math.sqrt(int(first_number)))
	e.insert(0, sqrt)

def button_square():
	first_number = e.get()
	e.delete(0, END)
	sqrt = float(math.pow(int(first_number), 2))
	e.insert(0, sqrt)

def button_divx():
	first_number = e.get()
	e.delete(0, END)
	divx = float(1/int(first_number))
	e.insert(0, divx)


button_1 = Button(root, text='1', padx=30, pady=30, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=30, pady=30, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=30, pady=30, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=30, pady=30, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=30, pady=30, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=30, pady=30, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=30, pady=30, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=30, pady=30, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=30, pady=30, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=30, pady=30, command=lambda: button_click(0))
button_div = Button(root, text='÷', padx=30, pady=30, command=button_div)
button_times = Button(root, text='x', padx=30, pady=30, command=button_times)
button_sub = Button(root, text='-', padx=30, pady=30, command=button_sub)
button_plus = Button(root, text='+', padx=30, pady=30, command=button_add)
button_equal = Button(root, text='=', padx=70, pady=30, command=button_equal, bg='#000080')
button_clear = Button(root, text='C', padx=30, pady=30, command=button_clear, bg='grey')
button_sqrt = Button(root, text='√x', padx=30, pady=30, command=button_sqrt)
button_square = Button(root, text='x²', padx=30, pady=30, command=button_square)
button_divx = Button(root, text='1/x', padx=30, pady=30, command=button_divx)


button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_plus.grid(row=4,column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_times.grid(row=2, column=3)

button_clear.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_equal.grid(row=5, column=2, columnspan=2)

button_div.grid(row=1, column=3)
button_sqrt.grid(row=1, column=2)
button_square.grid(row=1, column=1)
button_divx.grid(row=1, column=0)
