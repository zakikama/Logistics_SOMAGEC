from PIL import Image, ImageTk
import PIL.Image
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from main import *
from tkinter import font as tkfont
from OrdreMission import *
from tkcalendar import *
def save_Ordre():
    NewOrdre=OrdreDeMission()
    NewOrdre.get


class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
 
         
        ###MENU FRAME
        left_frame = tk.Frame(root, borderwidth=1, bg= "white", relief="solid", highlightthickness=2)
        left_frame.pack(side="left", expand=False, fill="y")
        container = tk.Frame(left_frame, borderwidth=1, bg= "white", relief="solid")
        container.pack(expand=True, fill="both", padx=5, pady=5)
        btn_1 = tk.Button(container, text="Home")
        btn_1.pack(padx=20, pady=20)
        btn_2 = tk.Button(container, text="Page One")
        btn_2.pack(padx=20,pady=20)
        ###TOP
        right_frame = tk.Frame(
            self, borderwidth=1, bg="green", relief="solid", highlightthickness=2)
        right_frame.pack(side="right", expand=True, fill="both")
        label_top = tk.Label(right_frame, text="Title Logo", bg="white")
        label_top.pack()
        ###BOTTOM

        ChafeurD = StringVar()
        GraisseursD = StringVar()
        OPTIONSC = get_matricule_Chauffeurs_Graisseurs()
        OPTIONSG = get_matricule_Chauffeurs_Graisseurs()
   
        ChafeurD.set(OPTIONSC[0])

        bottom_box = tk.Frame(right_frame, borderwidth=1, bg= "white", relief="solid")

        labelChauffeur=StringVar()
        labelChauffeur.set("Designez le Chauffeur")
        labelDir=Label(bottom_box, textvariable=labelChauffeur, height=4)
        labelDir.pack()
        Chauffeurs_liste = OptionMenu(bottom_box, ChafeurD, *OPTIONSC)
        Chauffeurs_liste.config(highlightbackground='#0E4ED6')
        Chauffeurs_liste.pack()

        labelGraisseur=StringVar()
        labelGraisseur.set("Designez le Graisseur")
        labelDir=Label(bottom_box, textvariable=labelGraisseur, height=4)
        labelDir.pack()
        Graisseur = OptionMenu(bottom_box, ChafeurD, *OPTIONSG)
        Graisseur.config(highlightbackground='#0E4ED6')
        Graisseur.pack()
 
        cal= Calendar(bottom_box,background="black", disabledbackground="black", bordercolor="black", 
               headersbackground="black", normalbackground="grey", foreground='black', 
               normalforeground='grey', headersforeground='grey', selectmode="day",year= 2021, month=3, day=3)

        cal.pack(pady=20)


        # directory=StringVar(None)
        # dirname=Entry(bottom_box,textvariable=directory,width=50)
        # dirname.pack(side="left")

        bottom_box.pack(expand=True, fill="both", padx=10, pady=10)
 
         
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x650")
    MainApp(root).pack(side="top", fill="both", expand=True)
    root.mainloop()