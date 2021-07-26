import tkinter as tk
from main import *
import time


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
        c = Chantier()
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
        tabs.add(tab5, text='Graisseurs')

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
            tab1, text="Supprimer", highlightbackground="#2d5b6b", font=ButtonFont, foreground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_refresh = tk.Button(tab1, text="refresh", font=ButtonFont,
                                   highlightbackground="#2d5b6b", command=lambda: self.refresh_table(self.parents))
        button_refresh.pack(padx=10, pady=10, side=tk.RIGHT)

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
            tab2, text="Supprimer", highlightbackground="#2d5b6b", font=ButtonFont, foreground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_refresh = tk.Button(
            tab2, text="refresh", highlightbackground="#2d5b6b", font=ButtonFont, command=lambda: self.refresh_table(self.parents))
        button_refresh.pack(padx=10, pady=10, side=tk.RIGHT)

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
            tab3, text="Supprimer", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_refresh = tk.Button(tab3, text="refresh", font=ButtonFont,
                                   highlightbackground="#2d5b6b", command=lambda: self.refresh_table(self.parents))
        button_refresh.pack(padx=10, pady=10, side=tk.RIGHT)

        table4 = Table(tab4, headings=('code', 'designation',
                                       'poids'), rows=get_table_Parc_Engin())
        table4.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab4, text="Ajouter", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab4, text="Modifier", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#0E4ED6', command=lambda: Formulaire_MEngin(table4.GetSelected()))
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab4, text="Supprimer", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#D60A0A', command=lambda: [delete_engin(1)])
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_refresh = tk.Button(tab4, text="refresh", font=ButtonFont,
                                   highlightbackground="#2d5b6b", command=lambda: self.refresh_table(self.parents))
        button_refresh.pack(padx=10, pady=10, side=tk.RIGHT)

        table5 = Table(tab5, headings=('matricule', 'nom', 'prenom',
                                       'fonction'), rows=get_table_Chauffeurs_Graisseurs())
        table5.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab5, text="Ajouter", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#189E11', command=lambda: Formulaire_Personnels())
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab5, text="Modifier", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab5, text="Supprimer", font=ButtonFont, highlightbackground="#2d5b6b", foreground='#D60A0A')
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


if __name__ == "__main__":
    root = Tk()
    print("original")
    my_gui = Tableau_Donnees(root)
    my_gui.pack(pady=10, fill="both", expand=True)

    btn = Button(root, text="refresh",
                 command=lambda: my_gui.refresh_table(root))
    btn.pack(side='bottom')

    root.mainloop()
