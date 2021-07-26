from OrdreMission import OrdreDeMission
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
from cryptography.fernet import Fernet

##############################
#    Formulaire D'ajout      #
##############################
def Formulaire_Personnels():
    root = tk.Toplevel(app)
    root.title("Ajouter personnels")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 750))

    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            save()

    def enter_Tapped(event):
        save()

    def save():
        c = chauf_grais()
        c.nom = nom_entry.get()
        c.matricule = matricule_entry.get()
        c.prenom = prenom_entry.get()
        c.fonction = fonction.get()
        c.sauvgarde_chauf_grais()
        messagebox.showinfo("showinfo", "Sauvgarde de " +
                            matricule_entry.get()+" Reussis ")

    root.img = ImageTk.PhotoImage(resize_image)
    global nom
    global prenom
    global fonction
    global matricule

    global nom_entry
    global prenom_entry
    global matricule_entry
    global fonction_entry
    OPTIONS = ["Chauffeur", "Graisseur"]

    nom = StringVar()
    prenom = StringVar()
    matricule = StringVar()
    fonction = StringVar()
    fonction.set(OPTIONS[0])
    canvas = Canvas(
        root,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    canvas.create_text(
        80,
        190,
        text='Matricule :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        240,
        text='Nom :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        290,
        text='Prenom :',
        font=('HIND Light', 20),
    )

    canvas.create_text(
        80,
        340,
        text='Fonction :',
        font=('HIND Light', 20),
    )

    matricule_entry = Entry(root, textvariable=matricule)
    matricule_entry.config(highlightbackground='#eeeeee',
                           foreground="#ff6815", background='#eeeeee')
    matricule_entry_canvas = canvas.create_window(
        200,
        170,
        anchor="nw",
        window=matricule_entry,
    )
    nom_entry = Entry(root, textvariable=nom)
    nom_entry.config(highlightbackground='#eeeeee',
                     foreground="#ff6815", background='#eeeeee')
    nom_entry_canvas = canvas.create_window(
        200,
        220,
        anchor="nw",
        window=nom_entry,
    )
    prenom_entry = Entry(root, textvariable=prenom)
    prenom_entry.config(highlightbackground='#eeeeee',
                        foreground="#ff6815", background='#eeeeee')
    prenom_entry_canvas = canvas.create_window(
        200,
        270,
        anchor="nw",
        window=prenom_entry,
    )

    fonction_entry = OptionMenu(root, fonction, *OPTIONS)
    fonction_entry.config(highlightbackground='#eeeeee',
                          foreground="#ff6815", background='#eeeeee')
    fonction_entry_canvas = canvas.create_window(
        200,
        320,
        anchor="nw",
        window=fonction_entry,
    )
    root.bind("<Button 1>", triangleClicked)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_Chantier():
    root = tk.Toplevel(app)
    root.title("Ajouter Chantier")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 750))

    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            save()

    def enter_Tapped(event):
        save()

    def save():
        c = chantier()
        c.intituleChantier = intituleChantier_entry.get()
        c.villeChantier = villeChantier_entry.get()
        c.adresseChantier = adresseChantier_entry.get()
        c.nomRespChantier = nomRespChantier.get()
        c.sauvgarde_Chantier()
        messagebox.showinfo("showinfo", "Sauvgarde de " +
                            intituleChantier_entry.get()+" Reussis ")

    root.img = ImageTk.PhotoImage(resize_image)
    global intituleChantier
    global adresseChantier
    global nomRespChantier
    global villeChantier

    global intituleChantier_entry
    global adresseChantier_entry
    global villeChantier_entry
    global nomRespChantier_entry

    intituleChantier = StringVar()
    adresseChantier = StringVar()
    villeChantier = StringVar()
    nomRespChantier = StringVar()

    canvas = Canvas(
        root,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    canvas.create_text(
        80,
        190,
        text='Ville :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        240,
        text='Libellé :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        290,
        text='Adresse :',
        font=('HIND Light', 20),
    )

    canvas.create_text(
        80,
        340,
        text='Responsable :',
        font=('HIND Light', 20),
    )

    villeChantier_entry = Entry(root, textvariable=villeChantier)
    villeChantier_entry.config(highlightbackground='#eeeeee',
                               foreground="#ff6815", background='#eeeeee')
    villeChantier_entry_canvas = canvas.create_window(
        200,
        170,
        anchor="nw",
        window=villeChantier_entry,
    )
    intituleChantier_entry = Entry(root, textvariable=intituleChantier)
    intituleChantier_entry.config(highlightbackground='#eeeeee',
                                  foreground="#ff6815", background='#eeeeee')
    intituleChantier_entry_canvas = canvas.create_window(
        200,
        220,
        anchor="nw",
        window=intituleChantier_entry,
    )
    adresseChantier_entry = Entry(root, textvariable=adresseChantier)
    adresseChantier_entry.config(highlightbackground='#eeeeee',
                                 foreground="#ff6815", background='#eeeeee')
    adresseChantier_entry_canvas = canvas.create_window(
        200,
        270,
        anchor="nw",
        window=adresseChantier_entry,
    )

    nomRespChantier_entry = Entry(root, textvariable=nomRespChantier)
    nomRespChantier_entry.config(highlightbackground='#eeeeee',
                                 foreground="#ff6815", background='#eeeeee')
    nomRespChantier_entry_canvas = canvas.create_window(
        200,
        320,
        anchor="nw",
        window=nomRespChantier_entry,
    )

    root.bind("<Button 1>", triangleClicked)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_Vehicule():
    root = tk.Toplevel(app)
    root.title("Ajouter Vehicule")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 750))
    global designationVehicule
    global typeVehicule
    global ptcVehicule
    global ptvVehicule
    global immatriculationVehicule

    global designationVehicule_entry
    global typeVehicule_entry
    global immatriculationVehicule_entry
    global ptcVehicule_entry
    global ptvVehicule_entry
    designationVehicule = StringVar()
    typeVehicule = StringVar()
    immatriculationVehicule = StringVar()
    ptcVehicule = StringVar()
    ptvVehicule = StringVar()

    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            save()

    def enter_Tapped(event):
        save()

    def save():
        c = vehicule()
        c.designationVehicule = designationVehicule_entry.get()
        c.immatriculationVehicule = immatriculationVehicule_entry.get()
        c.typeVehicule = typeVehicule_entry.get()
        c.ptcVehicule = float(ptcVehicule.get())
        c.ptvVehicule = float(ptvVehicule.get())
        c.sauvgarde_Vehicule()
        messagebox.showinfo("showinfo", "Sauvgarde de " +
                            designationVehicule_entry.get()+" Reussis ")

    root.img = ImageTk.PhotoImage(resize_image)

    canvas = Canvas(
        root,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    canvas.create_text(
        80,
        190,
        text='Immatriculation :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        240,
        text='Libellé :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        290,
        text='Type:',
        font=('HIND Light', 20),
    )

    canvas.create_text(
        80,
        340,
        text='PTC(kg) :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        390,
        text='PTV(kg) :',
        font=('HIND Light', 20),
    )
    immatriculationVehicule_entry = Entry(
        root, textvariable=immatriculationVehicule)
    immatriculationVehicule_entry.config(highlightbackground='#eeeeee',
                                         foreground="#ff6815", background='#eeeeee')
    immatriculationVehicule_entry_canvas = canvas.create_window(
        200,
        170,
        anchor="nw",
        window=immatriculationVehicule_entry,
    )
    designationVehicule_entry = Entry(root, textvariable=designationVehicule)
    designationVehicule_entry.config(highlightbackground='#eeeeee',
                                     foreground="#ff6815", background='#eeeeee')
    designationVehicule_entry_canvas = canvas.create_window(
        200,
        220,
        anchor="nw",
        window=designationVehicule_entry,
    )
    typeVehicule_entry = Entry(root, textvariable=typeVehicule)
    typeVehicule_entry.config(highlightbackground='#eeeeee',
                              foreground="#ff6815", background='#eeeeee')
    typeVehicule_entry_canvas = canvas.create_window(
        200,
        270,
        anchor="nw",
        window=typeVehicule_entry,
    )

    ptcVehicule_entry = Entry(root, textvariable=ptcVehicule)
    ptcVehicule_entry.config(highlightbackground='#eeeeee',
                             foreground="#ff6815", background='#eeeeee')
    ptcVehicule_entry_canvas = canvas.create_window(
        200,
        320,
        anchor="nw",
        window=ptcVehicule_entry,
    )
    ptvVehicule_entry = Entry(root, textvariable=ptvVehicule)
    ptvVehicule_entry.config(highlightbackground='#eeeeee',
                             foreground="#ff6815", background='#eeeeee')
    ptvVehicule_entry_canvas = canvas.create_window(
        200,
        370,
        anchor="nw",
        window=ptvVehicule_entry,
    )
    root.bind("<Button 1>", triangleClicked)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_Remorque():
    root = tk.Toplevel(app)
    root.title("Ajouter Remorque")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 750))

    def enter_Tapped(event):
        save()

    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            save()

    def save():
        c = remorque()
        c.designationRemorque = designationRemorque_entry.get()
        c.immatriculationRemorque = immatriculationRemorque_entry.get()
        c.typeRemorque = typeRemorque_entry.get()
        c.ptcRemorque = float(ptcRemorque.get())
        c.ptvRemorque = float(ptvRemorque.get())
        c.sauvgarde_Remorque()
        messagebox.showinfo("showinfo", "Sauvgarde de " +
                            designationRemorque_entry.get()+" Reussis ")

    root.img = ImageTk.PhotoImage(resize_image)
    global designationRemorque
    global typeRemorque
    global ptcRemorque
    global ptvRemorque
    global immatriculationRemorque

    global designationRemorque_entry
    global typeRemorque_entry
    global immatriculationRemorque_entry
    global ptcRemorque_entry
    global ptvRemorque_entry

    designationRemorque = StringVar()
    typeRemorque = StringVar()
    immatriculationRemorque = StringVar()
    ptcRemorque = StringVar()
    ptvRemorque = StringVar()

    canvas = Canvas(
        root,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    canvas.create_text(
        80,
        190,
        text='Immatriculation :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        240,
        text='Libellé :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        290,
        text='Type:',
        font=('HIND Light', 20),
    )

    canvas.create_text(
        80,
        340,
        text='PTC(kg) :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        390,
        text='PTV(kg) :',
        font=('HIND Light', 20),
    )

    immatriculationRemorque_entry = Entry(
        root, textvariable=immatriculationRemorque)
    immatriculationRemorque_entry.config(highlightbackground='#eeeeee',
                                         foreground="#ff6815", background='#eeeeee')
    immatriculationRemorque_entry_canvas = canvas.create_window(
        200,
        170,
        anchor="nw",
        window=immatriculationRemorque_entry,
    )
    designationRemorque_entry = Entry(root, textvariable=designationRemorque)
    designationRemorque_entry.config(highlightbackground='#eeeeee',
                                     foreground="#ff6815", background='#eeeeee')
    designationRemorque_entry_canvas = canvas.create_window(
        200,
        220,
        anchor="nw",
        window=designationRemorque_entry,
    )
    typeRemorque_entry = Entry(root, textvariable=typeRemorque)
    typeRemorque_entry.config(highlightbackground='#eeeeee',
                              foreground="#ff6815", background='#eeeeee')
    typeRemorque_entry_canvas = canvas.create_window(
        200,
        270,
        anchor="nw",
        window=typeRemorque_entry,
    )

    ptcRemorque_entry = Entry(root, textvariable=ptcRemorque)
    ptcRemorque_entry.config(highlightbackground='#eeeeee',
                             foreground="#ff6815", background='#eeeeee')
    ptcRemorque_entry_canvas = canvas.create_window(
        200,
        320,
        anchor="nw",
        window=ptcRemorque_entry,
    )
    ptvRemorque_entry = Entry(root, textvariable=ptvRemorque)
    ptvRemorque_entry.config(highlightbackground='#eeeeee',
                             foreground="#ff6815", background='#eeeeee')
    ptvRemorque_entry_canvas = canvas.create_window(
        200,
        370,
        anchor="nw",
        window=ptvRemorque_entry,
    )

    root.bind("<Button 1>", triangleClicked)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_Engin():
    root = tk.Toplevel(app)
    root.title("Ajouter Engin")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 750))

    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            save()

    def enter_Tapped(event):
        save()

    def save():
        c = engin()
        c.designationEngin = designationEngin_entry.get()
        c.poidsEngin = float(poidsEngin.get())
        c.sauvgarde_Engin()
        messagebox.showinfo("showinfo", "Sauvgarde de " +
                            designationEngin_entry.get()+" Reussis ")

    root.img = ImageTk.PhotoImage(resize_image)
    global designationEngin
    global poidsEngin

    global designationEngin_entry
    global poidsEngin_entry

    designationEngin = StringVar()
    poidsEngin = StringVar()

    canvas = Canvas(
        root,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    canvas.create_text(
        80,
        240,
        text='designation :',
        font=('HIND Light', 20),
    )
    canvas.create_text(
        80,
        290,
        text='Poids :',
        font=('HIND Light', 20),
    )

    designationEngin_entry = Entry(root, textvariable=designationEngin)
    designationEngin_entry.config(highlightbackground='#eeeeee',
                                  foreground="#ff6815", background='#eeeeee')
    designationEngin_entry_canvas = canvas.create_window(
        200,
        220,
        anchor="nw",
        window=designationEngin_entry,
    )

    poidsEngin_entry = Entry(root, textvariable=poidsEngin)
    poidsEngin_entry.config(highlightbackground='#eeeeee',
                            foreground="#ff6815", background='#eeeeee')
    poidsEngin_entry_canvas = canvas.create_window(
        200,
        270,
        anchor="nw",
        window=poidsEngin_entry,
    )

    root.bind("<Button 1>", triangleClicked)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()

##############################
# Formulaire De modification #
##############################
def Formulaire_MChantier(Chantier):
    root = tk.Toplevel(app)
    root.title("Modifier Chantier")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 750))

    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            edit()

    def enter_Tapped(event):
        edit()

    def edit():

        modifier_chantier(intituleChantier_entry.get(), adresseChantier_entry.get(
        ), villeChantier_entry.get(), nomRespChantier.get(), codeChantier.get())

        messagebox.showinfo("showinfo", "modification de " +
                            intituleChantier_entry.get()+" Reussis ")

    root.img = ImageTk.PhotoImage(resize_image)
    global intituleChantier
    global adresseChantier
    global nomRespChantier
    global villeChantier
    global codeChantier
    global codeChantier_entry
    global intituleChantier_entry
    global adresseChantier_entry
    global villeChantier_entry
    global nomRespChantier_entry
    codeChantier = StringVar()
    intituleChantier = StringVar()
    adresseChantier = StringVar()
    villeChantier = StringVar()
    nomRespChantier = StringVar()
    canvas = Canvas(
        root,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    if Chantier != []:

        canvas.create_text(
            80,
            140,
            text='code :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            190,
            text='Ville :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Libellé :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            290,
            text='Adresse :',
            font=('HIND Light', 20),
        )

        canvas.create_text(
            80,
            340,
            text='Responsable :',
            font=('HIND Light', 20),
        )
        codeChantier_entry = Entry(root, textvariable=codeChantier)
        codeChantier_entry.insert(END, Chantier[0])
        codeChantier_entry.config(highlightbackground='#eeeeee',
                                  foreground="#ff6815", background='#eeeeee')
        codeChantier_entry_canvas = canvas.create_window(
            200,
            120,
            anchor="nw",
            window=codeChantier_entry,
        )
        villeChantier_entry = Entry(root, textvariable=villeChantier)
        villeChantier_entry.insert(END, Chantier[3])
        villeChantier_entry.config(highlightbackground='#eeeeee',
                                   foreground="#ff6815", background='#eeeeee')
        villeChantier_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=villeChantier_entry,
        )
        intituleChantier_entry = Entry(root, textvariable=intituleChantier)
        intituleChantier_entry.insert(END, Chantier[1])
        intituleChantier_entry.config(highlightbackground='#eeeeee',
                                      foreground="#ff6815", background='#eeeeee')
        intituleChantier_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=intituleChantier_entry,
        )
        adresseChantier_entry = Entry(root, textvariable=adresseChantier)
        adresseChantier_entry.insert(END, Chantier[2])
        adresseChantier_entry.config(highlightbackground='#eeeeee',
                                     foreground="#ff6815", background='#eeeeee')
        adresseChantier_entry_canvas = canvas.create_window(
            200,
            270,
            anchor="nw",
            window=adresseChantier_entry,
        )

        nomRespChantier_entry = Entry(root, textvariable=nomRespChantier)
        nomRespChantier_entry.insert(END, Chantier[4])
        nomRespChantier_entry.config(highlightbackground='#eeeeee',
                                     foreground="#ff6815", background='#eeeeee')
        nomRespChantier_entry_canvas = canvas.create_window(
            200,
            320,
            anchor="nw",
            window=nomRespChantier_entry,
        )
    else:

        canvas.create_text(
            80,
            140,
            text='code :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            190,
            text='Ville :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Libellé :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            290,
            text='Adresse :',
            font=('HIND Light', 20),
        )

        canvas.create_text(
            80,
            340,
            text='Responsable :',
            font=('HIND Light', 20),
        )
        codeChantier_entry = Entry(root, textvariable=codeChantier)
        codeChantier_entry.config(highlightbackground='#eeeeee',
                                  foreground="#ff6815", background='#eeeeee')
        codeChantier_entry_canvas = canvas.create_window(
            200,
            120,
            anchor="nw",
            window=codeChantier_entry,
        )
        villeChantier_entry = Entry(root, textvariable=villeChantier)
        villeChantier_entry.config(highlightbackground='#eeeeee',
                                   foreground="#ff6815", background='#eeeeee')
        villeChantier_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=villeChantier_entry,
        )
        intituleChantier_entry = Entry(root, textvariable=intituleChantier)
        intituleChantier_entry.config(highlightbackground='#eeeeee',
                                      foreground="#ff6815", background='#eeeeee')
        intituleChantier_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=intituleChantier_entry,
        )
        adresseChantier_entry = Entry(root, textvariable=adresseChantier)
        adresseChantier_entry.config(highlightbackground='#eeeeee',
                                     foreground="#ff6815", background='#eeeeee')
        adresseChantier_entry_canvas = canvas.create_window(
            200,
            270,
            anchor="nw",
            window=adresseChantier_entry,
        )

        nomRespChantier_entry = Entry(root, textvariable=nomRespChantier)
        nomRespChantier_entry.config(highlightbackground='#eeeeee',
                                     foreground="#ff6815", background='#eeeeee')
        nomRespChantier_entry_canvas = canvas.create_window(
            200,
            320,
            anchor="nw",
            window=nomRespChantier_entry,)
    root.bind("<Button 1>", triangleClicked)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_MVehicule(Vehicule):
    root = tk.Toplevel(app)
    root.title("Modifier Vehicule")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 750))

    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            print("CLICK")
            edit()

    def enter_Tapped(event):
        print("enter")
        edit()

    def edit():

        modifier_vehicule(designationVehicule_entry.get(), typeVehicule_entry.get(
        ), ptcVehicule_entry.get(), ptvVehicule_entry.get(), immatriculationVehicule_entry.get())

        messagebox.showinfo("showinfo", "modification de " +
                            designationVehicule_entry.get()+" Reussis ")

    root.img = ImageTk.PhotoImage(resize_image)
    global designationVehicule
    global typeVehicule
    global ptcVehicule
    global ptvVehicule
    global immatriculationVehicule

    global designationVehicule_entry
    global typeVehicule_entry
    global immatriculationVehicule_entry
    global ptcVehicule_entry
    global ptvVehicule_entry

    designationVehicule = StringVar()
    typeVehicule = StringVar()
    immatriculationVehicule = StringVar()
    ptcVehicule = StringVar()
    ptvVehicule = StringVar()

    canvas = Canvas(
        root,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    if Vehicule != []:
        canvas.create_text(
            80,
            190,
            text='Immatriculation :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Libellé :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            290,
            text='Type:',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            340,
            text='PTC(kg) :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            390,
            text='PTV(kg) :',
            font=('HIND Light', 20),
        )
        immatriculationVehicule_entry = Entry(
            root, textvariable=immatriculationVehicule)
        immatriculationVehicule_entry.insert(END, Vehicule[2])
        immatriculationVehicule_entry.config(highlightbackground='#eeeeee',
                                             foreground="#ff6815", background='#eeeeee')
        immatriculationVehicule_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=immatriculationVehicule_entry,
        )
        designationVehicule_entry = Entry(
            root, textvariable=designationVehicule)
        designationVehicule_entry.insert(END, Vehicule[1])
        designationVehicule_entry.config(highlightbackground='#eeeeee',
                                         foreground="#ff6815", background='#eeeeee')
        designationVehicule_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=designationVehicule_entry,
        )
        typeVehicule_entry = Entry(root, textvariable=typeVehicule)
        typeVehicule_entry.insert(END, Vehicule[3])
        typeVehicule_entry.config(highlightbackground='#eeeeee',
                                  foreground="#ff6815", background='#eeeeee')
        typeVehicule_entry_canvas = canvas.create_window(
            200,
            270,
            anchor="nw",
            window=typeVehicule_entry,
        )

        ptcVehicule_entry = Entry(root, textvariable=ptcVehicule)
        ptcVehicule_entry.insert(END, Vehicule[4])
        ptcVehicule_entry.config(highlightbackground='#eeeeee',
                                 foreground="#ff6815", background='#eeeeee')
        ptcVehicule_entry_canvas = canvas.create_window(
            200,
            320,
            anchor="nw",
            window=ptcVehicule_entry,
        )
        ptvVehicule_entry = Entry(root, textvariable=ptvVehicule)
        ptvVehicule_entry.insert(END, Vehicule[5])
        ptvVehicule_entry.config(highlightbackground='#eeeeee',
                                 foreground="#ff6815", background='#eeeeee')
        ptvVehicule_entry_canvas = canvas.create_window(
            200,
            370,
            anchor="nw",
            window=ptvVehicule_entry,
        )

    else:

        canvas.create_text(
            80,
            190,
            text='Immatriculation :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Libellé :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            290,
            text='Type:',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            340,
            text='PTC(kg) :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            390,
            text='PTV(kg) :',
            font=('HIND Light', 20),
        )
        immatriculationVehicule_entry = Entry(
            root, textvariable=immatriculationVehicule)
        immatriculationVehicule_entry.config(highlightbackground='#eeeeee',
                                             foreground="#ff6815", background='#eeeeee')
        immatriculationVehicule_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=immatriculationVehicule_entry,
        )
        designationVehicule_entry = Entry(
            root, textvariable=designationVehicule)
        designationVehicule_entry.config(highlightbackground='#eeeeee',
                                         foreground="#ff6815", background='#eeeeee')
        designationVehicule_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=designationVehicule_entry,
        )
        typeVehicule_entry = Entry(root, textvariable=typeVehicule)
        typeVehicule_entry.config(highlightbackground='#eeeeee',
                                  foreground="#ff6815", background='#eeeeee')
        typeVehicule_entry_canvas = canvas.create_window(
            200,
            270,
            anchor="nw",
            window=typeVehicule_entry,
        )

        ptcVehicule_entry = Entry(root, textvariable=ptcVehicule)
        ptcVehicule_entry.config(highlightbackground='#eeeeee',
                                 foreground="#ff6815", background='#eeeeee')
        ptcVehicule_entry_canvas = canvas.create_window(
            200,
            320,
            anchor="nw",
            window=ptcVehicule_entry,
        )
        ptvVehicule_entry = Entry(root, textvariable=ptvVehicule)
        ptvVehicule_entry.config(highlightbackground='#eeeeee',
                                 foreground="#ff6815", background='#eeeeee')
        ptvVehicule_entry_canvas = canvas.create_window(
            200,
            370,
            anchor="nw",
            window=ptvVehicule_entry,
        )

    root.bind("<Button 1>", triangleClicked)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_MRemorque(Remorque):
    root = tk.Toplevel(app)
    root.title("Modifier Remorque")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 750))

    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            print("CLICK")
            edit()

    def enter_Tapped(event):
        print("enter")
        edit()

    def edit():

        modifier_remorque(designationRemorque_entry.get(), typeRemorque_entry.get(
        ), ptcRemorque_entry.get(), ptvRemorque_entry.get(), immatriculationRemorque_entry.get())

        messagebox.showinfo("showinfo", "modification de " +
                            designationRemorque_entry.get()+" Reussis ")

    root.img = ImageTk.PhotoImage(resize_image)
    global designationRemorque
    global typeRemorque
    global ptcRemorque
    global ptvRemorque
    global immatriculationRemorque

    global designationRemorque_entry
    global typeRemorque_entry
    global immatriculationRemorque_entry
    global ptcRemorque_entry
    global ptvRemorque_entry

    designationRemorque = StringVar()
    typeRemorque = StringVar()
    immatriculationRemorque = StringVar()
    ptcRemorque = StringVar()
    ptvRemorque = StringVar()

    canvas = Canvas(
        root,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    if Remorque != []:
        canvas.create_text(
            80,
            190,
            text='Immatriculation :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Libellé :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            290,
            text='Type:',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            340,
            text='PTC(kg) :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            390,
            text='PTV(kg) :',
            font=('HIND Light', 20),
        )
        immatriculationRemorque_entry = Entry(
            root, textvariable=immatriculationRemorque)
        immatriculationRemorque_entry.insert(END, Remorque[2])
        immatriculationRemorque_entry.config(highlightbackground='#eeeeee',
                                             foreground="#ff6815", background='#eeeeee')
        immatriculationRemorque_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=immatriculationRemorque_entry,
        )
        designationRemorque_entry = Entry(
            root, textvariable=designationRemorque)
        designationRemorque_entry.insert(END, Remorque[1])
        designationRemorque_entry.config(highlightbackground='#eeeeee',
                                         foreground="#ff6815", background='#eeeeee')
        designationRemorque_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=designationRemorque_entry,
        )
        typeRemorque_entry = Entry(root, textvariable=typeRemorque)
        typeRemorque_entry.insert(END, Remorque[3])
        typeRemorque_entry.config(highlightbackground='#eeeeee',
                                  foreground="#ff6815", background='#eeeeee')
        typeRemorque_entry_canvas = canvas.create_window(
            200,
            270,
            anchor="nw",
            window=typeRemorque_entry,
        )

        ptcRemorque_entry = Entry(root, textvariable=ptcRemorque)
        ptcRemorque_entry.insert(END, Remorque[4])
        ptcRemorque_entry.config(highlightbackground='#eeeeee',
                                 foreground="#ff6815", background='#eeeeee')
        ptcRemorque_entry_canvas = canvas.create_window(
            200,
            320,
            anchor="nw",
            window=ptcRemorque_entry,
        )
        ptvRemorque_entry = Entry(root, textvariable=ptvRemorque)
        ptvRemorque_entry.insert(END, Remorque[5])
        ptvRemorque_entry.config(highlightbackground='#eeeeee',
                                 foreground="#ff6815", background='#eeeeee')
        ptvRemorque_entry_canvas = canvas.create_window(
            200,
            370,
            anchor="nw",
            window=ptvRemorque_entry,
        )

    else:

        canvas.create_text(
            80,
            190,
            text='Immatriculation :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Libellé :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            290,
            text='Type:',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            340,
            text='PTC(kg) :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            390,
            text='PTV(kg) :',
            font=('HIND Light', 20),
        )
        immatriculationRemorque_entry = Entry(
            root, textvariable=immatriculationRemorque)
        immatriculationRemorque_entry.config(highlightbackground='#eeeeee',
                                             foreground="#ff6815", background='#eeeeee')
        immatriculationRemorque_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=immatriculationRemorque_entry,
        )
        designationRemorque_entry = Entry(
            root, textvariable=designationRemorque)
        designationRemorque_entry.config(highlightbackground='#eeeeee',
                                         foreground="#ff6815", background='#eeeeee')
        designationRemorque_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=designationRemorque_entry,
        )
        typeRemorque_entry = Entry(root, textvariable=typeRemorque)
        typeRemorque_entry.config(highlightbackground='#eeeeee',
                                  foreground="#ff6815", background='#eeeeee')
        typeRemorque_entry_canvas = canvas.create_window(
            200,
            270,
            anchor="nw",
            window=typeRemorque_entry,
        )

        ptcRemorque_entry = Entry(root, textvariable=ptcRemorque)
        ptcRemorque_entry.config(highlightbackground='#eeeeee',
                                 foreground="#ff6815", background='#eeeeee')
        ptcRemorque_entry_canvas = canvas.create_window(
            200,
            320,
            anchor="nw",
            window=ptcRemorque_entry,
        )
        ptvRemorque_entry = Entry(root, textvariable=ptvRemorque)
        ptvRemorque_entry.config(highlightbackground='#eeeeee',
                                 foreground="#ff6815", background='#eeeeee')
        ptvRemorque_entry_canvas = canvas.create_window(
            200,
            370,
            anchor="nw",
            window=ptvRemorque_entry,
        )

    root.bind("<Button 1>", triangleClicked)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_MEngin(Engin):
    root = tk.Toplevel(app)
    root.title("Modifier Engin")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 750))

    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            print("CLICK")
            edit()

    def enter_Tapped(event):
        print("enter")
        edit()

    def edit():

        modifier_engin(designationEngin_entry.get(), poidsEngin_entry.get(
        ), codeEngin_entry.get())

        messagebox.showinfo("showinfo", "modification de " +
                            designationEngin_entry.get()+" Reussis ")

    root.img = ImageTk.PhotoImage(resize_image)
    global designationEngin
    global poidsEngin
    global codeEngin

    global designationEngin_entry
    global poidsEngin_entry
    global codeEngin_entry

    designationEngin = StringVar()
    poidsEngin = StringVar()
    codeEngin = StringVar()

    canvas = Canvas(
        root,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    if Engin != []:
        canvas.create_text(
            80,
            190,
            text='Code :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Libellé :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            290,
            text='Poids (Kg):',
            font=('HIND Light', 20),
        )

        codeEngin_entry = Entry(
            root, textvariable=codeEngin)
        codeEngin_entry.insert(END, Engin[0])
        codeEngin_entry.config(highlightbackground='#eeeeee',
                               foreground="#ff6815", background='#eeeeee')
        codeEngin_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=codeEngin_entry,
        )
        designationEngin_entry = Entry(root, textvariable=designationEngin)
        designationEngin_entry.insert(END, Engin[1])
        designationEngin_entry.config(highlightbackground='#eeeeee',
                                      foreground="#ff6815", background='#eeeeee')
        designationEngin_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=designationEngin_entry,
        )
        poidsEngin_entry = Entry(root, textvariable=poidsEngin)
        poidsEngin_entry.insert(END, Engin[2])
        poidsEngin_entry.config(highlightbackground='#eeeeee',
                                foreground="#ff6815", background='#eeeeee')
        typeRemorque_entry_canvas = canvas.create_window(
            200,
            270,
            anchor="nw",
            window=poidsEngin_entry,
        )

    else:

        canvas.create_text(
            80,
            190,
            text='Code :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Libellé :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            290,
            text='Poids (Kg):',
            font=('HIND Light', 20),
        )

        codeEngin_entry = Entry(
            root, textvariable=codeEngin)

        codeEngin_entry.config(highlightbackground='#eeeeee',
                               foreground="#ff6815", background='#eeeeee')
        codeEngin_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=codeEngin_entry,
        )
        designationEngin_entry = Entry(root, textvariable=designationEngin)

        designationEngin_entry.config(highlightbackground='#eeeeee',
                                      foreground="#ff6815", background='#eeeeee')
        designationEngin_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=designationEngin_entry,
        )
        poidsEngin_entry = Entry(root, textvariable=poidsEngin)

        poidsEngin_entry.config(highlightbackground='#eeeeee',
                                foreground="#ff6815", background='#eeeeee')
        typeRemorque_entry_canvas = canvas.create_window(
            200,
            270,
            anchor="nw",
            window=poidsEngin_entry,
        )

    root.bind("<Button 1>", triangleClicked)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_MPersonnel(Personelle):
    root = tk.Toplevel(app)
    root.title("Modifier Personnel")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')
    resize_image = image.resize((500, 750))
    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            print("CLICK")
            edit()
    def enter_Tapped(event):
        print("enter")
        edit()

    def edit():

        modifier_chauf_grais(fonctionPersonnel_entry.get(), MatriculePersonnel_entry.get())

        messagebox.showinfo("showinfo", "modification de " +
                            MatriculePersonnel_entry.get()+" Reussis ")

    root.img = ImageTk.PhotoImage(resize_image)
    global fonctionPersonnel
    global MatriculePersonnel

    global fonctionPersonnel_entry
    global MatriculePersonnel_entry


    fonctionPersonnel = StringVar()
    MatriculePersonnel = StringVar()


    canvas = Canvas(
        root,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    if Personelle != []:
        canvas.create_text(
            80,
            190,
            text='Matricule :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Fonctions * :',
            font=('HIND Light', 20),
        )

        MatriculePersonnel_entry = Entry(
            root, textvariable=MatriculePersonnel)
        MatriculePersonnel_entry.insert(END, Personelle[0])
        MatriculePersonnel_entry.config(highlightbackground='#eeeeee',
                               foreground="#ff6815", background='#eeeeee')
        MatriculePersonnel_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=MatriculePersonnel_entry,
        )
        fonctionPersonnel_entry = Entry(root, textvariable=fonctionPersonnel)
        fonctionPersonnel_entry.insert(END, Personelle[3])
        fonctionPersonnel_entry.config(highlightbackground='#eeeeee',
                                      foreground="#ff6815", background='#eeeeee')
        fonctionPersonnel_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=fonctionPersonnel_entry,
        )
    else:

        canvas.create_text(
            80,
            190,
            text='Matricule :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Fonctions *  :',
            font=('HIND Light', 20),
        )
        

        MatriculePersonnel_entry = Entry(
            root, textvariable=MatriculePersonnel)

        MatriculePersonnel_entry.config(highlightbackground='#eeeeee',
                               foreground="#ff6815", background='#eeeeee')
        MatriculePersonnel_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=MatriculePersonnel_entry,
        )
        fonctionPersonnel_entry = Entry(root, textvariable=fonctionPersonnel)

        fonctionPersonnel_entry.config(highlightbackground='#eeeeee',
                                      foreground="#ff6815", background='#eeeeee')
        fonctionPersonnel_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=fonctionPersonnel_entry,
        )

    root.bind("<Button 1>", triangleClicked)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
##############################
# Formulaire De modification #
##############################
def Formulaire_supp_Chantier():
    root = tk.Toplevel(app)
    root.title("supprimer Chantier")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/SmallForm.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 200))

    def enter_Tapped(event):
        save()

    def save():
        MsgBox = tk.messagebox.askquestion ('Suppression','Are you sure ?',icon = 'warning')
        if MsgBox == 'yes':
            code_ = code_entry.get()
            delete_chantier(code_)
            messagebox.showinfo("showinfo", "suppression Reussis ")
            root.destroy()
        else:
            tk.messagebox.showinfo('Return','You will now return to the application screen')
        

    root.img = ImageTk.PhotoImage(resize_image)
    code = StringVar()
    canvas = Canvas(
        root,
        width=500,
        height=200,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    canvas.create_text(
        120,
        100,
        text='Code :',
        font=('HIND Light', 20),
    )

    code_Liste=get_code_Chantier()
    code_entry =ttk.Combobox(root, textvariable=code)
    code_entry['values'] = code_Liste
    code_entry['state'] = 'normal'  # normal

    code_entry_canvas = canvas.create_window(
        170,
        90,
        anchor="nw",
        window=code_entry,
    )
    btn_LogIn = Button(
                root,
                text='SUPPRIMER',
                command=lambda: save(),
                width=10,
                height=1,
                highlightthickness=0,
                borderwidth=0,
                bd=0,
                highlightbackground="#eeeeee",
                foreground="#FF5733",
                font=('HIND Light', 18)
            )
    btn_LogIn_canvas = canvas.create_window(
                390,
                160,
                anchor="nw",
                window=btn_LogIn,
            )
    # code_entry.bind('<<ComboboxSelected>>',enter_Tapped)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_supp_Vehicule():
    root = tk.Toplevel(app)
    root.title("supprimer vehicule")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/SmallForm.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 200))

    def enter_Tapped(event):
        save()

    def save():
        MsgBox = tk.messagebox.askquestion ('Suppression','Are you sure ?',icon = 'warning')
        if MsgBox == 'yes':
            matricule_ = matricule_entry.get()
            delete_Vehicule(matricule_)
            messagebox.showinfo("showinfo", "suppression Reussis ")
            root.destroy()
        else:
            tk.messagebox.showinfo('Return','You will now return to the application screen')
        

    root.img = ImageTk.PhotoImage(resize_image)
    matricule = StringVar()
    canvas = Canvas(
        root,
        width=500,
        height=200,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    canvas.create_text(
        120,
        100,
        text='Matricule :',
        font=('HIND Light', 20),
    )

    matricule_Liste=get_matricule_Parc_Vehicule()
    matricule_entry =ttk.Combobox(root, textvariable=matricule)
    matricule_entry['values'] = matricule_Liste
    matricule_entry['state'] = 'normal'  # normal

    matricule_entry_canvas = canvas.create_window(
        170,
        90,
        anchor="nw",
        window=matricule_entry,
    )
    btn_LogIn = Button(
                root,
                text='SUPPRIMER',
                command=lambda: save(),
                width=10,
                height=1,
                highlightthickness=0,
                borderwidth=0,
                bd=0,
                highlightbackground="#eeeeee",
                foreground="#FF5733",
                font=('HIND Light', 18)
            )
    btn_LogIn_canvas = canvas.create_window(
                390,
                160,
                anchor="nw",
                window=btn_LogIn,
            )

    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_supp_Remorque():
    root = tk.Toplevel(app)
    root.title("supprimer Remorque")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/SmallForm.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 200))

    def enter_Tapped(event):
        save()

    def save():
        MsgBox = tk.messagebox.askquestion ('Suppression','Are you sure ?',icon = 'warning')
        if MsgBox == 'yes':
            matricule_ = matricule_entry.get()
            delete_Remorque(matricule_)
            messagebox.showinfo("showinfo", "suppression Reussis ")
            root.destroy()
        else:
            tk.messagebox.showinfo('Return','You will now return to the application screen')
        

    root.img = ImageTk.PhotoImage(resize_image)
    matricule = StringVar()
    canvas = Canvas(
        root,
        width=500,
        height=200,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    canvas.create_text(
        120,
        100,
        text='Matricule :',
        font=('HIND Light', 20),
    )

    matricule_Liste=get_matricule_Parc_Remorque()
    matricule_entry =ttk.Combobox(root, textvariable=matricule)
    matricule_entry['values'] = matricule_Liste
    matricule_entry['state'] = 'normal'  # normal

    matricule_entry_canvas = canvas.create_window(
        170,
        90,
        anchor="nw",
        window=matricule_entry,
    )
    btn_LogIn = Button(
                root,
                text='SUPPRIMER',
                command=lambda: save(),
                width=10,
                height=1,
                highlightthickness=0,
                borderwidth=0,
                bd=0,
                highlightbackground="#eeeeee",
                foreground="#FF5733",
                font=('HIND Light', 18)
            )
    btn_LogIn_canvas = canvas.create_window(
                390,
                160,
                anchor="nw",
                window=btn_LogIn,
            )

    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_supp_Engin():
    root = tk.Toplevel(app)
    root.title("supprimer Engin")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/SmallForm.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 200))
    def enter_Tapped(event):
        save()
    def save():
        MsgBox = tk.messagebox.askquestion(
            'Suppression', 'Are you sure ?', icon='warning')
        if MsgBox == 'yes':
            code_ = code_entry.get()
            delete_engin(code_)
            messagebox.showinfo("showinfo", "suppression Reussis ")
            root.destroy()
        else:
            tk.messagebox.showinfo(
                'Return', 'You will now return to the application screen')


    root.img = ImageTk.PhotoImage(resize_image)
    code = StringVar()
    canvas = Canvas(
        root,
        width=500,
        height=200,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    canvas.create_text(
        120,
        100,
        text='Code :',
        font=('HIND Light', 20),
    )

    code_Liste = get_code_Parc_Engin()
    code_entry = ttk.Combobox(root, textvariable=code)
    code_entry['values'] = code_Liste
    code_entry['state'] = 'normal'  # normal

    code_entry_canvas = canvas.create_window(
        170,
        90,
        anchor="nw",
        window=code_entry,
    )
    btn_LogIn = Button(
        root,
        text='SUPPRIMER',
        command=lambda: save(),
        width=10,
        height=1,
        highlightthickness=0,
        borderwidth=0,
        bd=0,
        highlightbackground="#eeeeee",
        foreground="#FF5733",
        font=('HIND Light', 18)
    )
    btn_LogIn_canvas = canvas.create_window(
        390,
        160,
        anchor="nw",
        window=btn_LogIn,
    )
    # code_entry.bind('<<ComboboxSelected>>',enter_Tapped)
    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
def Formulaire_supp_Perso():
    root = tk.Toplevel(app)
    root.title("supprimer Personnel")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/SmallForm.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 200))

    def enter_Tapped(event):
        save()

    def save():
        MsgBox = tk.messagebox.askquestion ('Suppression','Are you sure ?',icon = 'warning')
        if MsgBox == 'yes':
            matricule_ = matricule_entry.get()
            delete_Chauffeurs_Graisseurs(matricule_)
            messagebox.showinfo("showinfo", "suppression Reussis ")
            root.destroy()
        else:
            tk.messagebox.showinfo('Return','You will now return to the application screen')
        

    root.img = ImageTk.PhotoImage(resize_image)
    matricule = StringVar()
    canvas = Canvas(
        root,
        width=500,
        height=200,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root.img,
        anchor="nw"

    )
    canvas.create_text(
        120,
        100,
        text='Matricule :',
        font=('HIND Light', 20),
    )

    matricule_Liste=get_matricule_Chauffeurs_Graisseurs()
    matricule_entry =ttk.Combobox(root, textvariable=matricule)
    matricule_entry['values'] = matricule_Liste
    matricule_entry['state'] = 'normal'  # normal

    matricule_entry_canvas = canvas.create_window(
        170,
        90,
        anchor="nw",
        window=matricule_entry,
    )
    btn_LogIn = Button(
                root,
                text='SUPPRIMER',
                command=lambda: save(),
                width=10,
                height=1,
                highlightthickness=0,
                borderwidth=0,
                bd=0,
                highlightbackground="#eeeeee",
                foreground="#FF5733",
                font=('HIND Light', 18)
            )
    btn_LogIn_canvas = canvas.create_window(
                390,
                160,
                anchor="nw",
                window=btn_LogIn,
            )

    root.bind("<Return>", enter_Tapped)
    root.bind('<KP_Enter>', enter_Tapped)
    root.resizable(0, 0)
    root.mainloop()
##############################
#   Gestion d'utilisateur    #
##############################
def LogOut():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    f = open('User_Log.json',)
    data = json.load(f)
    print(data["user"])
    if data["Status"]=="C":
        print("test Status")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        aDict = {"user": data["user"], "time ": dt_string, "Status":"D"}
        jsonString = json.dumps(aDict)
        jsonFile = open("User_Log.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        with open('User_Log.json','rb') as f:
            data_cry = f.read()
        fernet = Fernet(key)
        encrypted=fernet.encrypt(data_cry)
        with open('User_Log.json','wb') as f:
            f.write(encrypted)
        print("encryption succes")
        messagebox.showinfo("showinfo", "Déconnexion")

        

##############################
#  initialisation de la BDD  #
##############################


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("connection SUCCES")
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def intialiser_DATABASE():
    database = "my_database.db"
    sql_create_User = """ CREATE TABLE IF NOT EXISTS Users(
                                        code integer PRIMARY KEY,
                                        nom text NOT NULL,
                                        prenom text NOT NULL ,
                                        type_user text NOT NULL,
                                        matricule text NOT NULL,
                                        hash_pass text NOT NULL,
                                        CONSTRAINT mat_unique UNIQUE(matricule)
                                    ); """
    sql_create_Parc_Vehicule_table = """ CREATE TABLE IF NOT EXISTS Parc_Vehicule(
                                        code integer PRIMARY KEY,
                                        designation text NOT NULL,
                                        immatriculation text NOT NULL ,
                                        type text NOT NULL,
                                        ptc real,
                                        ptv real,
                                        CONSTRAINT mat_unique UNIQUE(immatriculation)
                                    ); """
    sql_create_Parc_Remorque_table = """ CREATE TABLE IF NOT EXISTS Parc_Remorque(
                                        code integer PRIMARY KEY,
                                        designation text NOT NULL,
                                        immatriculation text NOT NULL ,
                                        type text NOT NULL,
                                        ptc real,
                                        ptv real,
                                        CONSTRAINT mat_unique UNIQUE(immatriculation)
                                    ); """
    sql_create_Chantier_table = """ CREATE TABLE IF NOT EXISTS Chantier(
                                        code integer PRIMARY KEY,
                                        intitule text NOT NULL,
                                        adresse text NOT NULL,
                                        ville text NOT NULL,
                                        nom_responsable text NOT NULL
                                    ); """
    sql_create_Parc_Engin_table = """ CREATE TABLE IF NOT EXISTS Parc_Engin(
                                        code integer PRIMARY KEY,
                                        designation text NOT NULL,
                                        poids real
                                    ); """
    sql_create_Chauffeurs_Graisseurs_table = """ CREATE TABLE IF NOT EXISTS Chauffeurs_Graisseurs(
                                        matricule text PRIMARY KEY,
                                        nom text NOT NULL,
                                        prenom text NOT NULL,
                                        fonction text NOT NULL,
                                        CONSTRAINT matricule_unique UNIQUE(matricule)
                                    ); """
    sql_create_Ordre_de_Mission_table = """ CREATE TABLE IF NOT EXISTS Ordres_Mission(
                                        code integer PRIMARY KEY,
                                        Chauffeur text NOT NULL,
                                        Graisseur text NOT NULL,
                                        vehicule text NOT NULL,
                                        engin text NOT NULL,
                                        remorque text NOT NULL,
                                        DateDepart text NOT NULL,
                                        ChantierDepart text NOT NULL,
                                        ChantierArrivee text NOT NULL,
                                        NatureTrasport text NOT NULL
                                    ); """

    # connection a la BDD
    conn = create_connection(database)

    # creation des differentes tables de la bases de donnees
    if conn is not None:
        create_table(conn, sql_create_Parc_Vehicule_table)
        create_table(conn, sql_create_Parc_Remorque_table)
        create_table(conn, sql_create_User)
        create_table(conn, sql_create_Chantier_table)
        create_table(conn, sql_create_Parc_Engin_table)
        create_table(conn, sql_create_Parc_Vehicule_table)
        create_table(conn, sql_create_Ordre_de_Mission_table)
        create_table(conn, sql_create_Chauffeurs_Graisseurs_table)

    else:
        print("---------Error! connection a la base de donnes impossible!!!------------")

################################
# Declaration de l application #
################################


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='HIND Light', size=18)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, LogisticsPage, TraitmentPage, StartPage, RegisterPage, LogIn):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

######--------Dashboard-------########


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        left_frame = tk.Frame(self, borderwidth=1, bg="#2d5b6b",
                              relief="solid")
        left_frame.pack(side="left", expand=False, fill="y")
        container = tk.Frame(left_frame,
                             bg="#2d5b6b", relief="solid")
        container.pack(expand=True, fill="both", padx=5, pady=5)
        ButtonFont = tkinter.font.Font(
            family='HIND Light', size=16)
        MyFont = tkinter.font.Font(
            family="HIND Light", size=30)
        btn_H = tk.Button(container, text="Home", font=ButtonFont, highlightbackground="#2d5b6b", foreground="#F76515",
                          command=lambda: controller.show_frame("HomePage"))
        btn_H.pack(padx=20, fill="x", pady=20)
        btn_1 = tk.Button(container, text="Logistics", font=ButtonFont, highlightbackground="#2d5b6b",
                          command=lambda: controller.show_frame("LogisticsPage"))
        btn_1.pack(padx=20, fill="x", pady=20)

        btn_2 = tk.Button(container, text="Traitement", font=ButtonFont, highlightbackground="#2d5b6b",
                          command=lambda: controller.show_frame("TraitmentPage"))
        btn_2.pack(padx=20, fill="x", pady=20)
        btn_LogOut = tk.Button(container, text="Log Out", font=ButtonFont, highlightbackground="#2d5b6b", foreground="red",
                               command=lambda: [LogOut(), controller.show_frame("StartPage")])
        btn_LogOut.pack(padx=20, side='bottom', fill="x", pady=20)

        image = Image.open(
            "/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/logo02.jpg")

        # Reszie the image using resize() method
        resize_image = image.resize((116, 101))

        img = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
        label1 = Label(left_frame, image=img, bd=0, background="#2d5b6b")
        label1.image = img
        label1.pack(side="bottom")

        right_frame = tk.Frame(
            self, borderwidth=1, bg="#2d5b6b")
        right_frame.pack(side="right", expand=True, fill="both")
        label_top = tk.Label(
            right_frame, text="Gestion Logistique", bg="#2d5b6b", foreground="white")
        label_top.configure(font=MyFont)
        label_top.pack()

        bottom_box = tk.Frame(right_frame, borderwidth=1,
                              bg="white", relief="solid")
        bottom_box.pack(expand=True, fill="both", padx=10, pady=10)

######--------les donnees de la BDD-------########


class LogisticsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        left_frame = tk.Frame(self, borderwidth=1, bg="#2d5b6b",
                              relief="solid")
        left_frame.pack(side="left", expand=False, fill="y")
        container = tk.Frame(left_frame,
                             bg="#2d5b6b", relief="solid")
        container.pack(expand=True, fill="both", padx=5, pady=5)

        ButtonFont = tkinter.font.Font(
            family='HIND Light', size=16)
        MyFont = tkinter.font.Font(
            family="HIND Light", size=30)
        btn_H = tk.Button(container, text="Home", font=ButtonFont, highlightbackground="#2d5b6b",
                          command=lambda: controller.show_frame("HomePage"))
        btn_H.pack(padx=20, fill="x", pady=20)
        btn_1 = tk.Button(container, text="Logistics", font=ButtonFont, highlightbackground="#2d5b6b", foreground="#F76515",
                          command=lambda: controller.show_frame("LogisticsPage"))
        btn_1.pack(padx=20, fill="x", pady=20)

        btn_2 = tk.Button(container, text="Traitement", font=ButtonFont, highlightbackground="#2d5b6b",
                          command=lambda: controller.show_frame("TraitmentPage"))
        btn_2.pack(padx=20, fill="x", pady=20)
        btn_LogOut = tk.Button(container, text="Log Out", font=ButtonFont, highlightbackground="#2d5b6b", foreground="red",
                               command=lambda: [LogOut(), controller.show_frame("StartPage")])
        btn_LogOut.pack(padx=20, side='bottom', fill="x", pady=20)

        image = Image.open(
            "/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/logo02.jpg")

        # Reszie the image using resize() method
        resize_image = image.resize((116, 101))

        img = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
        label1 = Label(left_frame, image=img, bd=0, background="#2d5b6b")
        label1.image = img
        label1.pack(side="bottom")
        # TOP
        right_frame = tk.Frame(
            self, borderwidth=1, bg="#2d5b6b")
        right_frame.pack(side="right", expand=True, fill="both")
        MyFont = tkinter.font.Font(family="",
                                   size=30)

        label_top = tk.Label(
            right_frame, text="Gestion Logistique", bg="#2d5b6b", foreground="white")
        label_top.configure(font=MyFont)
        label_top.pack()
        bottom_box = tk.Frame(right_frame,
                              bg="#2d5b6b", relief="solid")
        my_gui = Tableau_Donnees(bottom_box)
        my_gui.pack(pady=10, fill="both", expand=True)
        bottom_box.pack(expand=True, fill="both", padx=10, pady=10)

######--------Gestion Des Ordres de Mission-------########


class TraitmentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MyFont = tkinter.font.Font(
            family="HIND Light", size=30)
        left_frame = tk.Frame(self, borderwidth=1, bg="#2d5b6b",
                              relief="solid")
        left_frame.pack(side="left", expand=False, fill="y")
        container = tk.Frame(left_frame, bg="#2d5b6b", relief="solid")
        container.pack(expand=True, fill="both", padx=5, pady=5)
        ButtonFont = tkinter.font.Font(
            family='HIND Light', size=16)
        MyFont = tkinter.font.Font(
            family="", size=30)
        MyFontS = tkinter.font.Font(family="HIND Light", size=15)
        btn_H = tk.Button(container, text="Home", font=ButtonFont, highlightbackground="#2d5b6b",
                          command=lambda: controller.show_frame("HomePage"))
        btn_H.pack(padx=20, fill="x", pady=20)
        btn_1 = tk.Button(container, text="Logistics", font=ButtonFont, highlightbackground="#2d5b6b",
                          command=lambda: controller.show_frame("LogisticsPage"))
        btn_1.pack(padx=20, fill="x", pady=20)

        btn_2 = tk.Button(container, text="Traitement", font=ButtonFont, highlightbackground="#2d5b6b", foreground="#F76515",
                          command=lambda: controller.show_frame("TraitmentPage"))
        btn_2.pack(padx=20, fill="x", pady=20)
        btn_LogOut = tk.Button(container, text="Log Out", font=ButtonFont, highlightbackground="#2d5b6b", foreground="red",
                               command=lambda: [LogOut(), controller.show_frame("StartPage")])
        btn_LogOut.pack(padx=20, side='bottom', fill="x", pady=20)
        image = Image.open(
            "/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/logo02.jpg")

        # Reszie the image using resize() method
        resize_image = image.resize((116, 101))

        img = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
        label1 = Label(left_frame, image=img, bd=0, background="#2d5b6b")
        label1.image = img
        label1.pack(side="bottom")
        right_frame = tk.Frame(
            self, borderwidth=1, bg="#2d5b6b")
        right_frame.pack(side="right", expand=True, fill="both")
        label_top = tk.Label(right_frame, text="Formulaire ODM",
                             bg="#2d5b6b", foreground="white")
        label_top.configure(font=MyFont)
        label_top.pack()
        # BOTTOM
        ChafeurD = StringVar()
        GraisseursD = StringVar()
        vehiculeD = StringVar()
        EnginD = StringVar()
        RemorqueD = StringVar()
        ChantierDD = StringVar()
        ChantierDA = StringVar()
        NatureTrD = StringVar()
        OPTIONSC = get_matricule_Chauffeurs_Graisseurs()
        OPTIONSG = get_matricule_Chauffeurs_Graisseurs()
        OPTIONSV = get_matricule_Parc_Vehicule()
        OPTIONSR = get_matricule_Parc_Remorque()
        OPTIONS_CHANTIER = get_intitule_Chantier()
        OPTIONSE = get_designation_Parc_Engin()
        OPTIONSN = ["Fer", "Voie navigable Maritime", "Routier", "Aérien"]
        ChafeurD.set("aucun")
        GraisseursD.set("aucun")
        vehiculeD.set("aucun")
        EnginD.set("aucun")
        RemorqueD.set("aucune")
        ChantierDD.set("aucun")
        ChantierDA.set("aucun")
        NatureTrD.set(OPTIONSN[2])

        def save_Ordre():
            print("CLICKED")
            Ord = OrdreDeMission()
            Ord.Chauffeur = ChafeurD.get()
            Ord.Graisseur = GraisseursD.get()
            Ord.vehicule = vehiculeD.get()
            Ord.engin = EnginD.get()
            Ord.remorque = RemorqueD.get()
            Ord.DateDepart = dateDepart_entry.get_date().strftime("%m/%d/%Y")
            Ord.ChantierDepart = ChantierDD.get()
            Ord.ChantierArrivee = ChantierDA.get()
            Ord.NatureTrasport = NatureTrD.get()
            Ord.sauvgarde_Ordre()
            Ord.print_Ordre()
        bottom_box = tk.Frame(right_frame,
                              bg="#2d5b6b", relief="solid")
        # FORMULAIRE Ordre de Mission
        Ligne1 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Chauffeur = Label(Ligne1, text="Designez le Chauffeur : ",
                                font=MyFontS, bg="#458093", foreground="white")
        label_Chauffeur.pack(side='left', padx=50, pady=10)
        Chauffeurs_list = OptionMenu(Ligne1, ChafeurD, *OPTIONSC)
        Chauffeurs_list.config(bg="#458093")
        Chauffeurs_list.pack(side='right', padx=50, pady=10)
        Ligne1.pack(expand=True, side='top', fill="both", pady=10)

        Ligne2 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Graisseur = Label(Ligne2, text="Designez le Graisseur : ",
                                font=MyFontS, bg="#458093", foreground="white")
        label_Graisseur.pack(side='left', padx=50, pady=10)
        Graisseur_list = OptionMenu(Ligne2, GraisseursD, *OPTIONSG)
        Graisseur_list.config(bg="#458093")
        Graisseur_list.pack(side='right', padx=50, pady=10)
        Ligne2.pack(expand=True, fill="both", pady=10)

        Ligne3 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Vehicule = Label(Ligne3, text="Designez le Vehicule : ",
                               font=MyFontS, bg="#458093", foreground="white")
        label_Vehicule.pack(side='left', padx=50, pady=10)
        vehicule_list = OptionMenu(Ligne3, vehiculeD, *OPTIONSV)
        vehicule_list.config(bg="#458093")
        vehicule_list.pack(side='right', padx=50, pady=10)
        Ligne3.pack(expand=True, fill="both", pady=10)

        Ligne4 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Engin = Label(Ligne4, text="Designez l'engin' : ",
                            font=MyFontS, bg="#458093", foreground="white")
        label_Engin.pack(side='left', padx=50, pady=10)
        engin_list = OptionMenu(Ligne4, EnginD, *OPTIONSE)
        engin_list.config(bg="#458093")
        engin_list.pack(side='right', padx=50, pady=10)
        Ligne4.pack(expand=True, fill="both", pady=10)

        Ligne5 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Remorque = Label(Ligne5, text="Designez la remorque : ",
                               font=MyFontS, bg="#458093", foreground="white")
        label_Remorque.pack(side='left', padx=50, pady=10)
        Remorque_list = OptionMenu(Ligne5, RemorqueD, *OPTIONSR)
        Remorque_list.config(bg="#458093")
        Remorque_list.pack(side='right', padx=50, pady=10)
        Ligne5.pack(expand=True, fill="both", pady=10)

        Ligne6 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_dateDepart = Label(
            Ligne6, text="Entrer la date de depart : ", font=MyFontS, bg="#458093", foreground="white")
        label_dateDepart.pack(side='left', padx=50, pady=10)
        dateDepart_entry = DateEntry(Ligne6, locale='de_DE')

        dateDepart_entry.pack(side='right', padx=50, pady=10)
        dateDepart_entry._top_cal.overrideredirect(False)
        Ligne6.pack(expand=True, fill="both", pady=10)

        Ligne7 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Chantiere = Label(
            Ligne7, text="Designez le chantier de depart : ", font=MyFontS, bg="#458093", foreground="white")
        label_Chantiere.pack(side='left', padx=50, pady=10)
        ChantierD_list = OptionMenu(Ligne7, ChantierDD, *OPTIONS_CHANTIER)
        ChantierD_list.config(bg="#458093")
        ChantierD_list.pack(side='right', padx=50, pady=10)
        Ligne7.pack(expand=True, fill="both", pady=10)

        Ligne8 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_ChantiereD = Label(
            Ligne8, text="Designez le chantier d'arrivee  : ", font=MyFontS, bg="#458093", foreground="white")
        label_ChantiereD.pack(side='left', padx=50, pady=10)
        ChantierA_list = OptionMenu(Ligne8, ChantierDA, *OPTIONS_CHANTIER)
        ChantierA_list.config(bg="#458093")
        ChantierA_list.pack(side='right', padx=50, pady=10)
        Ligne8.pack(expand=True, fill="both", pady=10)

        Ligne9 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_NatureTr = Label(
            Ligne9, text="Designez la nature du transport : ", font=MyFontS, bg="#458093", foreground="white")
        label_NatureTr.pack(side='left', padx=50, pady=10)
        NatureTr_list = OptionMenu(Ligne9, NatureTrD, *OPTIONSN)
        NatureTr_list.config(bg="#458093")
        NatureTr_list.pack(side='right', padx=50, pady=10)
        Ligne9.pack(expand=True, fill="both", pady=10)
        button_Save = tk.Button(
            bottom_box, text="Enregistrer", font=ButtonFont, highlightbackground="#2d5b6b", command=save_Ordre)
        button_Save.pack(padx=10, pady=10, fill='none', side='left')
        
        button_retour = tk.Button(bottom_box, text="<--", font=ButtonFont, highlightbackground="#2d5b6b", foreground="red",
                                  command=lambda: controller.show_frame("HomePage"))
        button_retour.pack(padx=10, pady=10, fill='none', side='right')
        bottom_box.pack(expand=True, fill="both")

######--------Page de Connexion-------########


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        image = Image.open(
            "/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/LoginBackground.png")

        # resize_image = image.resize((1079, 600))
        resize_image = image.resize((1079, 600))

        self.img = ImageTk.PhotoImage(resize_image)

        canvas = Canvas(
            self,
            width=1800,
            height=1000,
            bg="#2d5b6b",
            bd=0,
            highlightthickness=0
        )

        canvas.pack(fill='both', expand=True)

        canvas.create_image(
            100,
            65,
            image=self.img,
            anchor="nw"

        )
        bt_3 = Button(	self,
                       text='Mot de passe oublié',

                       width=20,
                       height=2,
                       highlightthickness=0,
                       borderwidth=0,
                       bd=0,
                       highlightbackground="#eeeeee",
                       foreground="blue",
                       font=('HIND Light', 10)
                       )

        btn = Button(
            self,
            text='SIGN UP',
            command=lambda: controller.show_frame("RegisterPage"),
            width=20,
            height=2,
            highlightthickness=0,
            borderwidth=0,
            bd=0,
            highlightbackground="#eeeeee",
            foreground="#ff6815",
            font=('HIND Light', 18)
        )
        btn1 = Button(
            self,
            text='SIGN IN',
            command=lambda: controller.show_frame("LogIn"),
            width=20,
            height=2,
            highlightthickness=0,
            bd=0,

            highlightbackground="#eeeeee",
            foreground="#ff6815",
            font=('HIND Light', 18)
        )

        btn_canvas = canvas.create_window(
            750,
            200,
            anchor="nw",
            window=btn,
        )
        btn_canvas1 = canvas.create_window(
            750,
            300,
            anchor="nw",
            window=btn1,
        )
        btn_canvas2 = canvas.create_window(
            1010,
            520,
            anchor="nw",
            window=bt_3,
        )

######--------Creer Compte-------########


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        global nom
        global prenom
        global type_account
        global matricule
        global password
        global nom_entry
        global prenom_entry
        global matricule_entry
        global password_entry
        OPTIONS = ["ADMIN", "LOGISTICIEN", "CAISSIER"]
        nom = StringVar()
        prenom = StringVar()
        matricule = StringVar()
        password = StringVar()
        type_account = StringVar()
        type_account.set(OPTIONS[0])

        def create_bcrypt_hash(password):
            # convert the string to bytes
            password_bytes = password.encode()
            # generate a salt
            salt = bcrypt.gensalt(14)
            # calculate a hash as bytes
            password_hash_bytes = bcrypt.hashpw(password_bytes, salt)
            # decode bytes to a string
            password_hash_str = password_hash_bytes.decode()

            # the password hash string should similar to:
            # $2b$10$//DXiVVE59p7G5k/4Klx/ezF7BI42QZKmoOD0NDvUuqxRE5bFFBLy
            return password_hash_str

        def register_user():
            nom_info = nom.get()
            prenom_info = prenom.get()
            matricule_info = matricule.get()
            password_info = password.get()
            type_info = type_account.get()
            if len(nom_info) == 0 or len(prenom_info) == 0 or len(password_info) == 0 or len(matricule_info) == 0:
                messagebox.showwarning(
                    "showwarning", "Veuillez remplir tout les champs avec *")
            else:
                donnees = [nom_info, prenom_info, type_info,
                           matricule_info, create_bcrypt_hash(password_info)]
                connexion = sqlite3.connect("my_database.db")
                curseur = connexion.cursor()
                curseur.execute('''
                    INSERT INTO Users(nom, prenom, type_user,  matricule, hash_pass) VALUES (?,?,?,?,?)
                    ''', donnees)
                connexion.commit()
                curseur.close()
                matricule_entry.delete(0, END)
                nom_entry.delete(0, END)
                prenom_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo("showinfo", "Compte creer avec succes")
                controller.show_frame("LogIn")

        tk.Frame.__init__(self, parent)
        image = Image.open(
            '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/LoginBackground.png')

        # Reszie the image using resize() method
        self.resize_image = image.resize((1079, 600))

        self.img = ImageTk.PhotoImage(self.resize_image)

        canvas = Canvas(
            self,
            width=1800,
            height=1000,
            bg="#2d5b6b",
            bd=0,
            highlightthickness=0
        )

        canvas.pack(fill='both', expand=True)

        canvas.create_image(
            100,
            65,
            image=self.img,
            anchor="nw"

        )
        canvas.create_text(
            720,
            220,
            text='fonction *',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            720,
            270,
            text='Matricule *',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            720,
            320,
            text='Nom *',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            720,
            370,
            text='Prenom *',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            720,
            420,
            text='Password *',
            font=('HIND Light', 20),
        )
        type_liste = OptionMenu(self, type_account, *OPTIONS)
        type_liste.config(highlightbackground='#eeeeee',
                          foreground="#ff6815", background='#eeeeee')
        type_liste_canvas = canvas.create_window(
            900,
            207,
            anchor="nw",
            window=type_liste,
        )
        matricule_entry = Entry(self, textvariable=matricule)
        matricule_entry.config(highlightbackground='#eeeeee',
                               foreground="#ff6815", background='#eeeeee')
        matricule_entry_canvas = canvas.create_window(
            825,
            255,
            anchor="nw",
            window=matricule_entry,
        )
        nom_entry = Entry(self, textvariable=nom)
        nom_entry.config(highlightbackground='#eeeeee',
                         foreground="#ff6815", background='#eeeeee')
        nom_entry_canvas = canvas.create_window(
            825,
            305,
            anchor="nw",
            window=nom_entry,
        )
        prenom_entry = Entry(self, textvariable=prenom)
        prenom_entry.config(highlightbackground='#eeeeee',
                            foreground="#ff6815", background='#eeeeee')
        prenom_entry_canvas = canvas.create_window(
            825,
            355,
            anchor="nw",
            window=prenom_entry,
        )
        password_entry = Entry(self, textvariable=password, show='*')
        password_entry.config(highlightbackground='#eeeeee',
                              foreground="#ff6815", background='#eeeeee')
        password_entry_canvas = canvas.create_window(
            825,
            405,
            anchor="nw",
            window=password_entry,
        )
        btn_Register = Button(
            self,
            text='SIGN UP',
            command=lambda: register_user(),
            width=20,
            height=2,
            highlightthickness=0,
            borderwidth=0,
            bd=0,
            highlightbackground="#eeeeee",
            foreground="#ff6815",
            font=('HIND Light', 18)
        )
        btn_Deja = Button(	self,
                           text='Already with an ACCOUNT ? SIGN IN ',
                           command=lambda: controller.show_frame("LogIn"),
                           width=40,
                           height=2,
                           highlightthickness=0,
                           borderwidth=0,
                           bd=0,
                           highlightbackground="#eeeeee",
                           foreground="blue",
                           font=('HIND Light', 10)
                           )
        btn_Register_canvas = canvas.create_window(
            750,
            450,
            anchor="nw",
            window=btn_Register,
        )
        btn_Deja_canvas2 = canvas.create_window(
            900,
            520,
            anchor="nw",
            window=btn_Deja,
        )
        # layout2
        # button1 = ttk.Button(self, text="StartPage",
        #                      command=lambda: controller.show_frame(StartPage))

        # # putting the button in its place
        # # by using grid
        # button1.grid(row=1, column=1, padx=10, pady=10)

        # # button to show frame 2 with text
        # # layout2
        # button2 = ttk.Button(self, text="Page 2",
        #                      command=lambda: controller.show_frame(LogIn))

        # # putting the button in its place by
        # # using grid
        # button2.grid(row=2, column=1, padx=10, pady=10)


class Tableau_Donnees(tk.Frame):
    def __init__(self, parent):
        self.parents = parent
        tk.Frame.__init__(self, parent)
        tabs = ttk.Notebook(self)
        tab1 = tk.Frame(tabs, background="#2d5b6b")
        tab2 = tk.Frame(tabs, background="#2d5b6b")
        tab3 = tk.Frame(tabs, background="#2d5b6b")
        tab4 = tk.Frame(tabs, background="#2d5b6b")
        tab5 = tk.Frame(tabs, background="#2d5b6b")

        tabs.add(tab1, text='Chantiers')
        tabs.add(tab2, text='Vehicules')
        tabs.add(tab3, text='Remorques')
        tabs.add(tab4, text='Engins')
        tabs.add(tab5, text='Personnel')
        ###################
        #    Chantiers    #
        ###################
        table1 = Table(tab1, headings=('code', 'intitule', 'adresse',
                                       'ville', 'nom responsable'), rows=get_table_Chantier())

        table1.pack(expand=tk.YES, fill=tk.BOTH)

        ButtonFont = tkinter.font.Font(
            family='HIND Light', size=16)

        button_Ajouter = tk.Button(
            tab1, text="Ajouter", highlightbackground="#2d5b6b", font=ButtonFont, foreground='#189E11', command=lambda: Formulaire_Chantier())
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab1, text="Modifier", highlightbackground="#2d5b6b", font=ButtonFont, foreground='#0E4ED6', command=lambda: Formulaire_MChantier(table1.GetSelected()))
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab1, text="Supprimer", highlightbackground="#2d5b6b", font=ButtonFont, foreground='#D60A0A',command=lambda:Formulaire_supp_Chantier())
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_refresh = tk.Button(tab1, text="refresh", font=ButtonFont,
                                   highlightbackground="#2d5b6b", command=lambda: self.refresh_table(self.parents))
        button_refresh.pack(padx=10, pady=10, side=tk.RIGHT)
        ###################
        #    Vehicules    #
        ###################
        table2 = Table(tab2, headings=('code', 'designation', 'immatriculation',
                                       'type', 'ptc', 'ptv'), rows=get_table_Parc_Vehicule())
        table2.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab2, text="Ajouter", highlightbackground="#2d5b6b", font=ButtonFont, foreground='#189E11', command=lambda: Formulaire_Vehicule())
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab2, text="Modifier", highlightbackground="#2d5b6b", font=ButtonFont, foreground='#0E4ED6', command=lambda: Formulaire_MVehicule(table2.GetSelected()))
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab2, text="Supprimer", highlightbackground="#2d5b6b", font=ButtonFont, foreground='#D60A0A',command=lambda:Formulaire_supp_Vehicule())
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_refresh = tk.Button(
            tab2, text="refresh", highlightbackground="#2d5b6b", font=ButtonFont, command=lambda: self.refresh_table(self.parents))
        button_refresh.pack(padx=10, pady=10, side=tk.RIGHT)
        ###################
        #    Remorques    #
        ###################
        table3 = Table(tab3, headings=('code', 'designation', 'immatriculation',
                                       'type', 'ptc', 'ptv'), rows=get_table_Parc_Remorque())
        table3.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab3, text="Ajouter", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#189E11', command=lambda: Formulaire_Remorque())
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab3, text="Modifier", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#0E4ED6', command=lambda: Formulaire_MRemorque(table3.GetSelected()))
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab3, text="Supprimer", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#D60A0A',command=lambda:Formulaire_supp_Remorque())
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_refresh = tk.Button(tab3, text="refresh", font=ButtonFont,
                                   highlightbackground="#2d5b6b", command=lambda: self.refresh_table(self.parents))
        button_refresh.pack(padx=10, pady=10, side=tk.RIGHT)
        ###################
        #      Engins     #
        ###################
        table4 = Table(tab4, headings=('code', 'designation',
                                       'poids'), rows=get_table_Parc_Engin())
        table4.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab4, text="Ajouter", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#189E11', command=lambda: Formulaire_Engin())
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab4, text="Modifier", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#0E4ED6', command=lambda: Formulaire_MEngin(table4.GetSelected()))
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab4, text="Supprimer", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#D60A0A', command=lambda:Formulaire_supp_Engin())
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_refresh = tk.Button(tab4, text="refresh", font=ButtonFont,
                                   highlightbackground="#2d5b6b", command=lambda: self.refresh_table(self.parents))
        button_refresh.pack(padx=10, pady=10, side=tk.RIGHT)
        ###################
        #    Personnel    #
        ###################
        table5 = Table(tab5, headings=('matricule', 'nom', 'prenom',
                                       'fonction'), rows=get_table_Chauffeurs_Graisseurs())
        table5.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab5, text="Ajouter", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#189E11', command=lambda: Formulaire_Personnels())
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab5, text="Modifier", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#0E4ED6', command=lambda:Formulaire_MPersonnel(table5.GetSelected()))
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab5, text="Supprimer", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#D60A0A',command=lambda:Formulaire_supp_Perso())
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_refresh = tk.Button(tab5, text="refresh", font=ButtonFont,
                                   highlightbackground="#2d5b6b", command=lambda: self.refresh_table(self.parents))
        button_refresh.pack(padx=10, pady=10, side=tk.RIGHT)
        tabs.pack(fill="both", expand=True)

    def refresh_table(self, rot):
        self.destroy()
        self.__init__(rot)
        self.pack(pady=10, fill="both", expand=True)
        print("Refreshed")

######--------Se connecter -------########


class LogIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global matricule_verify
        global password_verify

        matricule_verify = StringVar()
        password_verify = StringVar()

        global password_login_entry
        global matricule_login_entry

        def verify_password(password, hash_from_database):
            password_bytes = password.encode()
            hash_bytes = hash_from_database.encode()

            # this will automatically retrieve the salt from the hash,
            # then combine it with the password (parameter 1)
            # and then hash that, and compare it to the user's hash
            does_match = bcrypt.checkpw(password_bytes, hash_bytes)

            return does_match

        image = Image.open(
            '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/LoginBackground.png')

        # Reszie the image using resize() method
        resize_image = image.resize((1079, 600))

        self.img = ImageTk.PhotoImage(resize_image)

        canvas = Canvas(
            self,
            width=1800,
            height=1000,
            bg="#2d5b6b",
            bd=0,
            highlightthickness=0
        )

        canvas.pack(fill='both', expand=True)
        OPTIONS = ["ADMIN", "LOGISTICIEN", "CAISSIER"]
        type_account = StringVar()
        type_account.set(OPTIONS[0])
        canvas.create_image(
            100,
            65,
            image=self.img,
            anchor="nw"

        )

        canvas.create_text(
            720,
            270,
            text='Matricule *',
            font=('HIND Light', 20),
        )

        canvas.create_text(
            720,
            370,
            text='Password*',
            font=('HIND Light', 20),
        )

        matricule_login_entry = Entry(self, textvariable=matricule_verify)
        matricule_login_entry.config(highlightbackground='#eeeeee',
                                     foreground="#ff6815", background='#eeeeee')
        matricule_login_entry_canvas = canvas.create_window(
            825,
            255,
            anchor="nw",
            window=matricule_login_entry,
        )

        password_login_entry = Entry(
            self, textvariable=password_verify, show='*')
        password_login_entry.config(highlightbackground='#eeeeee',
                                    foreground="#ff6815", background='#eeeeee')
        password_login_entry_canvas = canvas.create_window(
            825,
            355,
            anchor="nw",
            window=password_login_entry,
        )
        btn_LogIn = Button(
            self,
            text='LOG IN',
            command=lambda: login_verify(),
            width=20,
            height=2,
            highlightthickness=0,
            borderwidth=0,
            bd=0,
            highlightbackground="#eeeeee",
            foreground="#ff6815",
            font=('HIND Light', 18)
        )
        btn_LogIn_canvas = canvas.create_window(
            750,
            450,
            anchor="nw",
            window=btn_LogIn,
        )
        btn_NoAcc = Button(	self,
                            text='New here ? SIGN UP ',
                            command=lambda: controller.show_frame(
                                "RegisterPage"),
                            width=40,
                            height=2,
                            highlightthickness=0,
                            borderwidth=0,
                            bd=0,
                            highlightbackground="#eeeeee",
                            foreground="blue",
                            font=('HIND Light', 10)
                            )
        btn_NoAcc_canvas2 = canvas.create_window(
            900,
            520,
            anchor="nw",
            window=btn_NoAcc,
        )

        def login_verify():
            matricule1 = matricule_verify.get()
            password1 = password_verify.get()
            connexion = sqlite3.connect("my_database.db")
            curseur = connexion.cursor()
            donnees = [matricule1]
            curseur.execute("""SELECT matricule
                                ,hash_pass
                        FROM Users
                        WHERE matricule=?
                            """,
                            donnees)
            result = curseur.fetchone()
            curseur.close()
            if result and verify_password(password1, result[1]):
                file = open('key.key','rb')
                key = file.read()
                file.close()
                with open('User_Log.json','rb') as f:
                    encrypted = f.read()
                fernet = Fernet(key)
                decrypted=fernet.decrypt(encrypted)
                with open('User_Log.json','wb') as f:
                    f.write(decrypted)
                    
                print("decryption success")
                print("LogIn succes")
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                aDict = {"user": result[0], "time ": dt_string, "Status": "C"}
                jsonString = json.dumps(aDict)
                jsonFile = open("User_Log.json", "w")
                jsonFile.write(jsonString)
                jsonFile.close()
                messagebox.showinfo("showinfo", "Connection Reussis")
                controller.show_frame("HomePage")
                print("succes")
                
            else:
                messagebox.showwarning(
                    "showwarning", "Matricule ou Mot de passe incorrecte")
                password_login_entry.delete(0, END)
                matricule_login_entry.delete(0, END)
                print("failed")


def on_closing():
    LogOut()
    app.destroy()


if __name__ == "__main__":

    intialiser_DATABASE()
    app = SampleApp()
    width = app.winfo_screenwidth()
    height = app.winfo_screenheight()-50

    app.geometry("%dx%d" % (width, height))
    # app.geometry("1800x1000")
    app.resizable(0, 0)
    ico = tk.Image(
        "photo", file="/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/ico.png")

    app.tk.call('wm', 'iconphoto', app._w, ico)
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
    