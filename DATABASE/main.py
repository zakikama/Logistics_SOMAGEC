
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
            family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
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


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        left_frame = tk.Frame(self, borderwidth=1, bg="white",
                              relief="solid", highlightthickness=2)
        left_frame.pack(side="left", expand=False, fill="y")
        container = tk.Frame(left_frame, borderwidth=1,
                             bg="white", relief="solid")
        container.pack(expand=True, fill="both", padx=5, pady=5)
        btn_1 = tk.Button(container, text="Logistics",
                          command=lambda: controller.show_frame("PageOne"))
        btn_1.pack(padx=20, pady=20)

        btn_2 = tk.Button(container, text="Traitement")
        btn_2.pack(padx=20, pady=20)

        # TOP
        right_frame = tk.Frame(
            self, borderwidth=1, bg="white", relief="solid", highlightthickness=2)
        right_frame.pack(side="right", expand=True, fill="both")

        label_top = tk.Label(right_frame, text="Title Logo", bg="white")
        label_top.pack()

        bottom_box = tk.Frame(right_frame, borderwidth=1,
                              bg="white", relief="solid")
        bottom_box.pack(expand=True, fill="both", padx=10, pady=10)
        label = tk.Label(self, text="This is the start page",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


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

        button_Ajouter = tk.Button(
            tab1, text="Ajouter", highlightbackground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab1, text="Modifier", highlightbackground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab1, text="Supprimer", highlightbackground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_retour = tk.Button(tab1, text="retour",
                                  command=lambda: controller.show_frame("StartPage"))
        button_retour.pack(padx=10, pady=10, side=tk.RIGHT)

        table = Table(tab2, headings=('code', 'designation', 'immatriculation',
                                      'type', 'ptc', 'ptv'), rows=get_table_Parc_Vehicule())
        table.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab2, text="Ajouter", highlightbackground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab2, text="Modifier", highlightbackground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab2, text="Supprimer", highlightbackground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_retour = tk.Button(tab2, text="retour",
                                  command=lambda: controller.show_frame("StartPage"))
        button_retour.pack(padx=10, pady=10, side=tk.RIGHT)

        table = Table(tab3, headings=('code', 'designation', 'immatriculation',
                                      'type', 'ptc', 'ptv'), rows=get_table_Parc_Remorque())
        table.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab3, text="Ajouter", highlightbackground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab3, text="Modifier", highlightbackground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab3, text="Supprimer", highlightbackground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_retour = tk.Button(tab3, text="retour",
                                  command=lambda: controller.show_frame("StartPage"))
        button_retour.pack(padx=10, pady=10, side=tk.RIGHT)

        table = Table(tab4, headings=('code', 'designation',
                                      'poids'), rows=get_table_Parc_Engin())
        table.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab4, text="Ajouter", highlightbackground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab4, text="Modifier", highlightbackground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab4, text="Supprimer", highlightbackground='#D60A0A', command=lambda: [delete_engin(1)])
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_retour = tk.Button(tab4, text="retour",
                                  command=lambda: controller.show_frame("StartPage"))
        button_retour.pack(padx=10, pady=10, side=tk.RIGHT)

        table = Table(tab5, headings=('matricule', 'nom', 'prenom',
                                      'fonction'), rows=get_table_Chauffeurs_Graisseurs())
        table.pack(expand=tk.YES, fill=tk.BOTH)

        button_Ajouter = tk.Button(
            tab5, text="Ajouter", highlightbackground='#189E11')
        button_Ajouter.pack(padx=10, pady=10, side=tk.LEFT)
        button_Modifier = tk.Button(
            tab5, text="Modifier", highlightbackground='#0E4ED6')
        button_Modifier.pack(padx=10, pady=10, side=tk.LEFT)
        button_Supprimer = tk.Button(
            tab5, text="Supprimer", highlightbackground='#D60A0A')
        button_Supprimer.pack(padx=10, pady=10, side=tk.LEFT)
        button_retour = tk.Button(tab5, text="retour",
                                  command=lambda: controller.show_frame("StartPage"))
        button_retour.pack(padx=10, pady=10, side=tk.RIGHT)
        # add frames to notebook

        # label = tk.Label(self, text="This is page 1", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)

        tabs.pack(pady=10, fill="both", expand=True)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is page 2",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    intialiser_DATABASE()
    app = SampleApp()
    app.mainloop()
