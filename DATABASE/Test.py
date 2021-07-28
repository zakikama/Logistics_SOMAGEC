from OrdreMission import *
import sqlite3
from sqlite3 import Error
from tkinter import *
import tkinter as tk
from tkinter import ttk
from Table import Table
from Vehicule import *
from Remorque import *
from Chantier import *
from Engin import *
from Chauf_Grais import *
from tkinter import font as tkfont
from tkcalendar import *
import tkinter.font
from PIL import ImageTk, Image
import bcrypt
import json
from datetime import datetime
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np



def Figure_Globale():
    figure = Figure(dpi=120)
    plot = figure.add_subplot(1, 1, 1)
    bars1=[len(get_matricule_Parc_Vehicule()),len(get_matricule_Parc_Remorque()),len(get_code_Parc_Engin()),len(get_matricule_Chauffeurs_Graisseurs())]
    bars2=[len(get_matricule_Parc_Vehicule_statut("Libre")),len(get_matricule_Parc_Remorque_statut("Libre")),len(get_code_Parc_Engin_statut("Libre")),len(get_matricule_Chauffeurs_Graisseurs_statut("Libre"))]
    bars3=[len(get_matricule_Parc_Vehicule_statut("Panne")),len(get_matricule_Parc_Remorque_statut("Panne")),len(get_code_Parc_Engin_statut("Panne")),len(get_matricule_Chauffeurs_Graisseurs_statut("Panne"))]
    xticks=["vehicules","Remorque","Engin","Personnel"]
    barWidth1 = 0.065
    barWidth2 = 0.032
    x_range = np.arange(len(bars1) / 8, step=0.125)
    plot.bar(x_range, bars1, color='#C1C1C1', width=barWidth1/2, edgecolor='grey', label='Total')
    plot.bar(x_range, bars2, color='#ff6815', width=barWidth2/2, edgecolor='#ff6815', label='Disponible')
    plot.bar(x_range, bars3, color='#2463A7', width=barWidth2/2, edgecolor='#ff6815', label='Panne')
    for i, bar in enumerate(bars2):
        plot.text(i / 8 - 0.015, bar + 1, bar, fontsize=7)
    plot.set_xticks(x_range, minor=False)
    plot.set_facecolor('#456975')
    plot.set_xticklabels(xticks, fontdict=None, minor=False,color="grey")
    plot.tick_params(axis='y', colors='grey')
    plot.tick_params(axis='x', colors='grey')
    plot.spines['left'].set_color('grey')       
    plot.spines['top'].set_color('#456975')
    plot.spines['bottom'].set_color('grey')  
    plot.spines['right'].set_color('#456975')  
    figure.patch.set_facecolor('#456975')
    return figure

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

left_frame = tk.Frame(root, borderwidth=1, bg="white",
                              relief="solid")
left_frame.pack(side="left", expand=False, fill="y")
container = tk.Frame(left_frame,
                             bg="white", relief="solid")
container.pack(expand=True, fill="both", padx=5, pady=5)
ButtonFont = tkinter.font.Font(
            family='HIND Light', size=16)
MyFont = tkinter.font.Font(
            family="HIND Light", size=30)
btn_H = tk.Button(container, text="Home", font=ButtonFont,bg = 'blue',borderwidth=0, fg="#F76515")
btn_H.pack(padx=20, fill="x", pady=20)
btn_1 = tk.Button(container, text="Logistics",borderwidth=0,
                          font=ButtonFont,relief="flat")
btn_1.pack(padx=20, fill="x", pady=20)
btn_2 = tk.Button(container, text="Traitement",
                          font=ButtonFont, highlightbackground="white")
btn_2.pack(padx=20, fill="x", pady=20)
btn_LogOut = tk.Button(container, text="Log Out", font=ButtonFont, highlightbackground="white", foreground="red")
btn_LogOut.pack(padx=20, side='bottom', fill="x", pady=20)

image = Image.open(
            "/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/logo02.jpg")

        # Reszie the image using resize() method
resize_image=image.resize((116, 101))

img=ImageTk.PhotoImage(resize_image)

        # create label and add resize image
label1=Label(left_frame, image = img, bd = 0, background = "white")
label1.image=img
label1.pack(side = "bottom")

right_frame=tk.Frame(
            root, borderwidth = 0, bg = "white")
right_frame.pack(side = "right", expand = True, fill = "both")
label_top=tk.Label(
            right_frame, text = "Gestion Logistique", bg = "white", foreground = "grey")
label_top.configure(font = MyFont)
label_top.pack()

bottom_box=tk.Frame(right_frame, borderwidth = 0,
                              bg = "white", relief = "solid")

Global_Frame01=tk.Frame(bottom_box,borderwidth = 0,
                              bg = "white", relief = "flat")
Card01=tk.Frame(Global_Frame01,borderwidth = 0,
                              bg = "grey", relief = "flat")
canvas01= FigureCanvasTkAgg(figure_dispo_v(), master=Card01) 
canvas01.draw()
canvas01.get_tk_widget().pack()
Card01.pack(side=LEFT,expand=True,fill = "both", padx = 10, pady = 10)
Card01.pack_propagate(0)
Card02=tk.Frame(Global_Frame01,borderwidth = 0,
                              bg = "grey", relief = "flat")
canvas02= FigureCanvasTkAgg(figure_dispo_R(), master=Card02) 
canvas02.draw()
canvas02.get_tk_widget().pack()
Card02.pack(side=LEFT,expand = True, fill = "both", padx = 10, pady = 10)
Card02.pack_propagate(0)
Card03=tk.Frame(Global_Frame01,borderwidth = 0,
                              bg = "grey", relief = "flat")
canvas03= FigureCanvasTkAgg(figure_dispo_E(), master=Card03) 
canvas03.draw()
canvas03.get_tk_widget().pack()
Card03.pack(side=LEFT,expand = True, fill = "both", padx = 10, pady = 10)
Card03.pack_propagate(0)
Global_Frame01.pack(side=TOP,expand = True, fill = "both")
Global_Frame02=tk.Frame(bottom_box,borderwidth = 0,
                              bg = "white", relief = "flat")
Card11=tk.Frame(Global_Frame02,borderwidth = 2, width=380,
                              bg = "grey", relief = "flat")
canvas = Canvas(
            Card11,
            width=300,
            height=1000,
            bg="#456975",
            bd=0,
            highlightthickness=0
        )
canvas.create_text(
            190,
            20,
            text="Latest ORDM",
            font=('HIND Light', 20),
            fill='grey',
        )
canvas.create_text(
            80,
            100,
            text="Chauffeur",
            fill='grey',
            font=('HIND', 18),
        )
canvas.create_text(
            300,
            100,
            text=get_latest_ORDM()[0][1],
            font=('HIND Light', 15),
        )
canvas.create_text(
            200,
            100,
            text=get_name_perso(get_latest_ORDM()[0][1])[0][0]+" "+get_name_perso(get_latest_ORDM()[0][1])[0][1]          ,
            font=('HIND Light', 15),
        )
canvas.create_text(
            80,
            140,
            text="Depart",
            fill='grey',
            font=('HIND', 18),
        )

canvas.create_text(
            200,
            140,
            text=get_latest_ORDM()[0][6]       ,
            font=('HIND Light', 15),
        )

canvas.create_text(
            300,
            140,
            text=get_latest_ORDM()[0][7]       ,
            font=('HIND Light', 15),
        )
canvas.create_text(
            80,
            180,
            text="Destination",
            fill='grey',
            font=('HIND', 18),
        )
canvas.create_text(
            255,
            180,
            text=get_latest_ORDM()[0][8]       ,
            font=('HIND Light', 15),
        )
if get_latest_ORDM()[0][3] == "aucune":
    imageV = Image.open("/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/vehiculeR.png")
else:
    imageV = Image.open("/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/vehicule.png")
resize_imagev = imageV.resize((50, 40)) 
canvas.create_text(
            75,
            280,
            text=get_latest_ORDM()[0][3]       ,
            font=('HIND Light', 15),
        )
photoV = ImageTk.PhotoImage(resize_imagev) 
canvas.create_image(50,220, anchor = 'nw', image=photoV)
if get_latest_ORDM()[0][5] == "aucune":
    imageR = Image.open("/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/remorqueR.png")
else:
    imageR = Image.open("/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/remorque.png")

resize_imageR = imageR.resize((70, 60)) 
canvas.create_text(
            185,
            280,
            text=get_latest_ORDM()[0][5]       ,
            font=('HIND Light', 15),
        )
photoR = ImageTk.PhotoImage(resize_imageR) 
canvas.create_image(150,210, anchor = 'nw', image=photoR)
if get_latest_ORDM()[0][4] == "aucune":
    imageE = Image.open("/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/enginRo.png")
else:
    imageE = Image.open("/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/engin.png")

resize_imageE = imageE.resize((70, 60)) 
canvas.create_text(
            295,
            280,
            text=get_latest_ORDM()[0][4]       ,
            font=('HIND Light', 15),
        )
photoE = ImageTk.PhotoImage(resize_imageE) 
canvas.create_image(260,210, anchor = 'nw', image=photoE)
canvas.pack(fill='both', expand=True)


        # creat

Card11.pack(side=RIGHT,expand = True, fill = 'y', padx=10,pady = 10) 
Card11.pack_propagate(0)   
Card12=tk.Frame(Global_Frame02,borderwidth = 0, width=700,
                              bg = "black", relief = "flat")
canvas = FigureCanvasTkAgg(Figure_Globale(), master=Card12) 
canvas.draw()
canvas.get_tk_widget().pack(side=BOTTOM,expand = True,fill="both")
Card12.pack(side=RIGHT,expand = True, fill = 'y',padx=10, pady = 10)  


Card12.pack_propagate(0)
Global_Frame02.pack(side=BOTTOM,expand = True, fill = "both")                               
bottom_box.pack(expand = True, fill = "both", padx = 10, pady = 10)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()-50

root.geometry("%dx%d" % (width, height))
root.mainloop()
