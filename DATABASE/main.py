
import sqlite3
from sqlite3 import Error

import tkinter as tk
from tkinter import Listbox, ttk

from Table import Table
from Vehicule import *
from Remorque import *
from Chantier import *
from Engin import *
from Chauf_Grais import *

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

    # connection a la BDD
    conn = create_connection(database)

    # creation des differentes tables de la bases de donnees
    if conn is not None:
        create_table(conn, sql_create_Parc_Vehicule_table)
        create_table(conn, sql_create_Parc_Remorque_table)
        create_table(conn, sql_create_Chantier_table)
        create_table(conn, sql_create_Parc_Engin_table)
        create_table(conn, sql_create_Parc_Vehicule_table)
        create_table(conn, sql_create_Chauffeurs_Graisseurs_table)

    else:
        print("---------Error! connection a la base de donnes impossible!!!------------")

    

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('600x400+0+0')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    tabs = ttk.Notebook()
    tabs.grid(row=0, column=0, sticky='nsew')

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
 
    table = Table(tab1, headings=('code', 'intitule', 'adresse','ville','nom responsable'), rows=get_table_Chantier())
    table.pack(expand=tk.YES, fill=tk.BOTH)
    table = Table(tab2, headings=('code', 'designation', 'immatriculation','type','ptc','ptv'), rows=get_table_Parc_Vehicule())
    table.pack(expand=tk.YES, fill=tk.BOTH)
    table = Table(tab3, headings=('code', 'designation', 'immatriculation','type','ptc','ptv'), rows=get_table_Parc_Remorque())
    table.pack(expand=tk.YES, fill=tk.BOTH)
    table = Table(tab4, headings=('code', 'designation', 'poids'), rows=get_table_Parc_Engin())
    table.pack(expand=tk.YES, fill=tk.BOTH)
    table = Table(tab5, headings=('matricule', 'nom', 'prenom','fonction'), rows=get_table_Chauffeurs_Graisseurs())
    table.pack(expand=tk.YES, fill=tk.BOTH)

   
    

    root.mainloop()




    