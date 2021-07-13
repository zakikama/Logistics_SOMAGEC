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


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='Proxima Nova Condensed Thin', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


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
        ButtonFont = tkinter.font.Font(family='Proxima Nova Condensed ', size=16)
        MyFont = tkinter.font.Font( family = "Proxima Nova Condensed Thin", size = 40)
        btn_H = tk.Button(container, text="Home",font=ButtonFont,highlightbackground="#2d5b6b",foreground="#F76515",
                          command=lambda: controller.show_frame("HomePage"))
        btn_H.pack(padx=20, fill="x", pady=20)
        btn_1 = tk.Button(container, text="Logistics",font=ButtonFont,highlightbackground="#2d5b6b",
                          command=lambda: controller.show_frame("PageOne"))
        btn_1.pack(padx=20, fill="x", pady=20)

        btn_2 = tk.Button(container, text="Traitement",font=ButtonFont,highlightbackground="#2d5b6b",
                          command=lambda: controller.show_frame("PageTwo"))
        btn_2.pack(padx=20, fill="x", pady=20)

        # TOP
        right_frame = tk.Frame(
            self, borderwidth=1, bg="#2d5b6b")
        right_frame.pack(side="right", expand=True, fill="both")
        MyFont = tkinter.font.Font( family = "Proxima Nova Condensed Thin", 
                                 size = 40)

        label_top = tk.Label(right_frame, text="Gestion Logistique", bg="#2d5b6b",foreground="white")
        label_top.configure(font = MyFont)
        label_top.pack()

        bottom_box = tk.Frame(right_frame, borderwidth=1,
                              bg="white", relief="solid")
        bottom_box.pack(expand=True, fill="both", padx=10, pady=10)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tabs = ttk.Notebook(self)

        tab1 = tk.Frame(tabs)
        tab2 = tk.Frame(tabs)
        tab3 = tk.Frame(tabs)
        tab4 = tk.Frame(tabs)
        tab5 = tk.Frame(tabs)
        
        tabs.add(tab1, text='Chantiers')
        tabs.add(tab2, text='Vehicules')
        tabs.add(tab3, text='Remorques')
        tabs.add(tab4, text='Engins')
        tabs.add(tab5, text='Graisseurs')
        
        table = Table(tab1, headings=('code', 'intitule', 'adresse',
                                      'ville', 'nom responsable'), rows=get_table_Chantier())
        table.pack(expand=tk.YES, fill=tk.BOTH)
        
        ButtonFont = tkinter.font.Font(family='Proxima Nova Condensed ', size=16)
       


        button_Ajouter = tk.Button(
            tab1, text="Ajouter",font=ButtonFont, foreground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab1, text="Modifier",font=ButtonFont, foreground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab1, text="Supprimer",font=ButtonFont, foreground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_retour = tk.Button(tab1, text="retour",font=ButtonFont,
                                  command=lambda: controller.show_frame("HomePage"))
        button_retour.pack(padx=10, pady=10, side=tk.RIGHT)

        table = Table(tab2, headings=('code', 'designation', 'immatriculation',
                                      'type', 'ptc', 'ptv'), rows=get_table_Parc_Vehicule())
        table.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab2, text="Ajouter", font=ButtonFont,foreground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab2, text="Modifier",font=ButtonFont, foreground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab2, text="Supprimer",font=ButtonFont, foreground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_retour = tk.Button(tab2, text="retour",font=ButtonFont,
                                  command=lambda: controller.show_frame("HomePage"))
        button_retour.pack(padx=10, pady=10, side=tk.RIGHT)

        table = Table(tab3, headings=('code', 'designation', 'immatriculation',
                                      'type', 'ptc', 'ptv'), rows=get_table_Parc_Remorque())
        table.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab3, text="Ajouter",font=ButtonFont, foreground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab3, text="Modifier",font=ButtonFont, foreground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab3, text="Supprimer",font=ButtonFont, foreground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_retour = tk.Button(tab3, text="retour",font=ButtonFont,
                                  command=lambda: controller.show_frame("HomePage"))
        button_retour.pack(padx=10, pady=10, side=tk.RIGHT)

        table = Table(tab4, headings=('code', 'designation',
                                      'poids'), rows=get_table_Parc_Engin())
        table.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab4, text="Ajouter",font=ButtonFont, foreground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab4, text="Modifier",font=ButtonFont, foreground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab4, text="Supprimer",font=ButtonFont, foreground='#D60A0A', command=lambda: [delete_engin(1)])
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_retour = tk.Button(tab4, text="retour",font=ButtonFont,
                                  command=lambda: controller.show_frame("HomePage"))
        button_retour.pack(padx=10, pady=10, side=tk.RIGHT)

        table = Table(tab5, headings=('matricule', 'nom', 'prenom',
                                      'fonction'), rows=get_table_Chauffeurs_Graisseurs())
        table.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab5, text="Ajouter",font=ButtonFont, foreground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab5, text="Modifier", font=ButtonFont,foreground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab5, text="Supprimer",font=ButtonFont, foreground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_retour = tk.Button(tab5, text="retour",font=ButtonFont,
                                  command=lambda: controller.show_frame("HomePage"))
        button_retour.pack(padx=10, pady=10, side=tk.RIGHT)
        # add frames to notebook

        # label = tk.Label(self, text="This is page 1", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)

        tabs.pack(pady=10, fill="both", expand=True)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        MyFont = tkinter.font.Font( family = "Proxima Nova Condensed Thin", size = 40)
        left_frame = tk.Frame(self, borderwidth=1, bg="#2d5b6b",
                              relief="solid")
        left_frame.pack(side="left", expand=False, fill="y")
        container = tk.Frame(left_frame, bg="#2d5b6b", relief="solid")
        container.pack(expand=True, fill="both", padx=5, pady=5)
        ButtonFont = tkinter.font.Font(family='Proxima Nova Condensed ', size=16)
        MyFont = tkinter.font.Font( family = "Proxima Nova Condensed Thin", size = 40)
        MyFontS = tkinter.font.Font( family = "Proxima Nova Condensed ", size = 15)
        btn_H = tk.Button(container, text="Home",font=ButtonFont,highlightbackground="#2d5b6b",
                          command=lambda: controller.show_frame("HomePage"))
        btn_H.pack(padx=20, fill="x", pady=20)
        btn_1 = tk.Button(container, text="Logistics",font=ButtonFont,highlightbackground="#2d5b6b",
                          command=lambda: controller.show_frame("PageOne"))
        btn_1.pack(padx=20, fill="x", pady=20)

        btn_2 = tk.Button(container, text="Traitement",font=ButtonFont,highlightbackground="#2d5b6b",foreground="#F76515",
                          command=lambda: controller.show_frame("PageTwo"))
        btn_2.pack(padx=20, fill="x", pady=20)
        right_frame = tk.Frame(
            self, borderwidth=1, bg="#2d5b6b")
        right_frame.pack(side="right", expand=True, fill="both")
        label_top = tk.Label(right_frame, text="Formulaire ODM", bg="#2d5b6b",foreground="white")
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
        bottom_box = tk.Frame(right_frame,
                              bg="#2d5b6b", relief="solid")
        # FORMULAIRE Ordre de Mission
        Ligne1 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Chauffeur = Label(Ligne1, text="Designez le Chauffeur : ",font=MyFontS, bg="#458093",foreground="white")
        label_Chauffeur.pack(side='left' ,padx=50, pady=10)
        Chauffeurs_list = OptionMenu(Ligne1, ChafeurD, *OPTIONSC)
        Chauffeurs_list.config(bg="#458093")
        Chauffeurs_list.pack(side='right',padx=50, pady=10)
        Ligne1.pack(expand=True,side='top', fill="both", pady=10)

        Ligne2 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Graisseur = Label(Ligne2, text="Designez le Graisseur : ",font=MyFontS, bg="#458093",foreground="white")
        label_Graisseur.pack(side='left' ,padx=50, pady=10)
        Graisseur_list = OptionMenu(Ligne2, GraisseursD, *OPTIONSG)
        Graisseur_list.config(bg="#458093")
        Graisseur_list.pack(side='right' ,padx=50, pady=10)
        Ligne2.pack(expand=True, fill="both", pady=10)

        Ligne3 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Vehicule = Label(Ligne3, text="Designez le Vehicule : ",font=MyFontS, bg="#458093",foreground="white")
        label_Vehicule.pack(side='left' ,padx=50, pady=10)
        vehicule_list = OptionMenu(Ligne3, vehiculeD, *OPTIONSV)
        vehicule_list.config(bg="#458093")
        vehicule_list.pack(side='right' ,padx=50, pady=10)
        Ligne3.pack(expand=True, fill="both", pady=10)

        Ligne4 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Engin = Label(Ligne4, text="Designez l'engin' : ",font=MyFontS, bg="#458093",foreground="white")
        label_Engin.pack(side='left' ,padx=50, pady=10)
        engin_list = OptionMenu(Ligne4, EnginD, *OPTIONSE)
        engin_list.config(bg="#458093")
        engin_list.pack(side='right' ,padx=50, pady=10)
        Ligne4.pack(expand=True, fill="both", pady=10)

        Ligne5 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Remorque = Label(Ligne5, text="Designez la remorque : ",font=MyFontS, bg="#458093",foreground="white")
        label_Remorque.pack(side='left' ,padx=50, pady=10)
        Remorque_list = OptionMenu(Ligne5, RemorqueD, *OPTIONSR)
        Remorque_list.config(bg="#458093")
        Remorque_list.pack(side='right' ,padx=50, pady=10)
        Ligne5.pack(expand=True, fill="both", pady=10)

        Ligne6 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_dateDepart = Label(
            Ligne6, text="Entrer la date de depart : ",font=MyFontS, bg="#458093",foreground="white")
        label_dateDepart.pack(side='left' ,padx=50, pady=10)
        dateDepart_entry = DateEntry(Ligne6, locale='de_DE')        
        dateDepart_entry.configure(justify='center')

        dateDepart_entry.pack(side='right' ,padx=50, pady=10)
        dateDepart_entry._top_cal.overrideredirect(False)
        Ligne6.pack(expand=True, fill="both", pady=10)

        Ligne7 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_Chantiere = Label(
            Ligne7, text="Designez le chantier de depart : ",font=MyFontS, bg="#458093",foreground="white")
        label_Chantiere.pack(side='left' ,padx=50, pady=10)
        ChantierD_list = OptionMenu(Ligne7, ChantierDD, *OPTIONS_CHANTIER)
        ChantierD_list.config(bg="#458093")
        ChantierD_list.pack(side='right' ,padx=50, pady=10)
        Ligne7.pack(expand=True, fill="both", pady=10)

        Ligne8 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_ChantiereD = Label(
            Ligne8, text="Designez le chantier d'arrivee  : ",font=MyFontS, bg="#458093",foreground="white")
        label_ChantiereD.pack(side='left' ,padx=50, pady=10)
        ChantierA_list = OptionMenu(Ligne8, ChantierDA, *OPTIONS_CHANTIER)
        ChantierA_list.config(bg="#458093")
        ChantierA_list.pack(side='right' ,padx=50, pady=10)
        Ligne8.pack(expand=True, fill="both", pady=10)

        Ligne9 = tk.Frame(bottom_box, bg="#458093", relief="solid")
        label_NatureTr = Label(
            Ligne9, text="Designez la nature du transport : ",font=MyFontS, bg="#458093",foreground="white")
        label_NatureTr.pack(side='left' ,padx=50, pady=10)
        NatureTr_list = OptionMenu(Ligne9, NatureTrD, *OPTIONSN)
        NatureTr_list.config(bg="#458093")
        NatureTr_list.pack(side='right' ,padx=50, pady=10)
        Ligne9.pack(expand=True, fill="both", pady=10)
        button_Save = tk.Button(
            bottom_box, text="Enregistrer",font=ButtonFont,highlightbackground="#2d5b6b", command=save_Ordre)
        button_Save.pack(padx=10, pady=10,fill='none', side='left')
        button_retour = tk.Button(bottom_box, text="<--",font=ButtonFont,highlightbackground="#2d5b6b",foreground="red",
                                  command=lambda: controller.show_frame("HomePage"))
        button_retour.pack(padx=10, pady=10, fill='none',side='right')

        # directory=StringVar(None)
        # dirname=Entry(bottom_box,textvariable=directory,width=50)
        # dirname.pack(side="left")

        bottom_box.pack(expand=True, fill="both")


if __name__ == "__main__":
    intialiser_DATABASE()
    app = SampleApp()
    
    app.geometry("1800x1000")
    app.mainloop()
