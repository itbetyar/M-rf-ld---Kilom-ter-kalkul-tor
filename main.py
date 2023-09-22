# IT Betyar 2022 - Merfold - kilometer atvalto

import tkinter as tk      # library importalas
# from tkinter import ttk   # Itt tobb ujabb widgetek van
import ttkbootstrap as ttk

def convert():            # A convert funkcio letrehozasa
    # print(entry.get())
    mile_input = entryInt.get()    # a merfold input valtozoba irjuk a beirt erteket
    km_output = mile_input * 1.61  # a km valtozoba irjuk a kalkulaciot
    output_string.set(km_output)   # az output_string valtozot feltoltjuk a km ertekkel

# Program ablak letrehozasa
window = ttk.Window(themename='darkly')
window.title('Mile to Kilometer')
window.geometry('400x200')

# Focim felirat
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack(pady = 10)

# input field - beviteli mezo
# pack method = egymas ala helyezi a teteleket
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()                   # spec object entry field value tarolasra
entry = ttk.Entry(master= input_frame, textvariable=entryInt, font = 'Calibri 12')  # itt megadjuk
button = ttk.Button(master= input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack()

# output - kimenet azaz a vegso eredmeny kiirasa
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, 
    text='Output',         # ha van textvariable akkor felulirja ezt
    font= 'Calibri 24',
    textvariable = output_string)  # textvariable felulirja fontit
output_label.pack(pady = 5)

#run - megjelenitjuk az ablakot
window.mainloop()
