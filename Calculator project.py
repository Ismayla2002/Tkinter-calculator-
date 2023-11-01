import tkinter
from tkinter import *
from tkinter import Tk, Label, Button, Entry
import math
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
from tkinter.ttk import *
from time import strftime
from math import *
import hdpitkinter
from hdpitkinter import *

root=HdpiTk()
root.title("Calculator")

#Create the temperature converter

def converter():
	def fahrenheit_to_celsius():
	    fahrenheit = ent_temperature.get()
	    celsius = (5 / 9) * (float(fahrenheit) - 32)
	    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
	
	frm_entry = tk.Frame(master=root, bd=2)
	ent_temperature = tk.Entry(master=frm_entry, width=10)
	lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
	
	ent_temperature.grid(row=0, column=0, sticky="e")
	lbl_temp.grid(row=0, column=1, sticky="w")
	
	btn_convert = tk.Button(
	    master=root,
	    text="\N{RIGHTWARDS BLACK ARROW}",command=fahrenheit_to_celsius, pady=4, bd=2, bg='aqua')
	lbl_result = tk.Label(master=root, text="\N{DEGREE CELSIUS}")
	
	frm_entry.place(x=180)
	btn_convert.place(x=400, y=-5)
	lbl_result.place(x=510)

#Create functions for results

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

#create trigonometric func

def cosinus():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(cos(result)))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        
func_cosinus = tk.Button(root, text='Cos', padx=23,pady=33, command=cosinus, bg='gray50', bd=7, activebackground='black')
func_cosinus.place(x=6, y=625)

def sinus():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(sin(result)))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        
func_sinus = tk.Button(root, text='Sin', padx=26,pady=33, command=sinus, bg='gray47', bd=7, activebackground='black')
func_sinus.place(x=122, y=625)

def tangent():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(tanh(result)))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        
func_tangent = tk.Button(root, text='tan', padx=23,pady=33, command=tangent, bg='gray46', bd=7, activebackground='black')
func_tangent.place(x=235, y=625)

#function squareRoot

def square():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(sqrt(result)))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
#Create button for square
square_num = tk.Button(root, text='√', padx=25,pady=33, command=square, bg='gray45', bd=7, activebackground='black')
square_num.place(x=344, y=625)

#function logarithme 
def logarithm():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(log(result)))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
#create button for logarithme 
func_log = tk.Button(root, text='Ln', padx=25,pady=33, command=logarithm, bg='gray45', bd=7, activebackground='black')
func_log.place(x=430, y=625)
#exponential
def exponential():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(log(result)))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
#button for exponential 
func_exponential = tk.Button(root, text='Exp', padx=20,pady=33, command=exponential, bg='gray45', bd=7, activebackground='black')
func_exponential.place(x=530, y=625)
#number absolute
def absolute():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(fabs(result)))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
#button for absolute number
absolute_n = tk.Button(root, text='|abs|', padx=2,pady=25, command=absolute, bg='gray45', bd=6, activebackground='black')
absolute_n.place(x=634, y=645)

#function to clear entry
def clear():
    entry.delete(0, tk.END)

#undo entry 
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

#function for the time
def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
#create a label for the time
label = Label(root, font=("Digital-font", 10), background="black", foreground="white")
label.place(x=5)

point = tk.Button(root, text='.', padx=37, pady=20, command=lambda: button_click("."), bg='black', fg='white',bd=6)
point.place(x=395, y=1280)

exit = tk.Button(root, text='Exit', padx=81, pady=20, command=quit, bg='red', bd=6)
exit.place(x=487, y=1280)

clear = tk.Button(root, text='C', padx=123, pady=33, command=clear, bg='blue', bd=7, activebackground='blue')
clear.place(x=420, y=745)

calcul = tk.Button(root, text="=", padx=87, pady=55, command=calculate, fg='white', bg='black', bd=5, activebackground='white')
calcul.place(x=130, y=1130)

back = tk.Button(root, text='← ', padx=170, pady=20, fg='white', bg='black', command=backspace, bd=6,activebackground='white')
back.place(x=3, y=1280)

entry = tk.Entry(root, width=41, justify=tk.RIGHT, bg='black', fg='white', bd=2)
entry.grid(row=0, column=0, columnspan=6, padx=7, pady=45, ipady=280)

#create button widgets for the numbers (0-9)
button_1 = tk.Button(root, text="1", padx=50, pady=40, fg='blue', bg='white',bd=4, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=50, pady=40, fg='blue', bg='white',bd=5,command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=60, pady=40,fg='blue', bg='white',bd=4, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=50, pady=40, fg='blue', bg='white',bd=4,command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=50, pady=40, fg='blue', bg='white',bd=5,command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=60, pady=40, fg='blue', bg='white',bd=4,command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=50, pady=40, fg='blue', bg='white',bd=4,command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=50, pady=40,fg='blue', bg='white', bd=5,command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=60, pady=40, fg='blue', bg='white',bd=4,command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=50, pady=50, fg='blue', bg='white',bd=4,activebackground='white',command=lambda: button_click(0))

#create buttons for calculations 
button_add = tk.Button(root, text="+", padx=40, pady=46, fg='blue', bg='white',bd=5,command=lambda: button_click("+"))
button_subtract = tk.Button(root, text="-", padx=131, pady=40, fg='blue', bg='white', bd=6,command=lambda: button_click("-"))
button_multiply = tk.Button(root, text="x", padx=126, pady=44, fg='blue', bg='white',bd=6,command=lambda: button_click("*"))
button_divide = tk.Button(root, text="/", padx=110, pady=50, fg='blue', bg='white',bd=6,command=lambda:
button_click("/"))

#set button position 
button_multiply.place(x=423, y=997)
button_divide.place(x=460, y=1130)
button_add.place(x=340, y=1137)
button_subtract.place(x=420, y=870)
button_1.place(x=4, y=1000)
button_2.place(x=130, y=745)
button_3.place(x=260, y=872)
button_4.place(x=4, y=872)
button_5.place(x=130, y=872)
button_6.place(x=260, y=745)
button_7.place(x=4, y=745)
button_8.place(x=130, y=1000)
button_9.place(x=260, y=1000)
button_0.place(x=4, y=1130)

#create a menu        
menu = Menu(root)
root.config(menu=menu)
#call functions and run the app
time()
converter()
root.mainloop()