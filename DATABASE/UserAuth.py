#import modules
from sqlite3.dbapi2 import PARSE_COLNAMES
from main import *
import bcrypt
from tkinter import *
from datetime import datetime
import json
import sqlite3
from sqlite3 import Error


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


def verify_password(password, hash_from_database):
    password_bytes = password.encode()
    hash_bytes = hash_from_database.encode()

    # this will automatically retrieve the salt from the hash,
    # then combine it with the password (parameter 1)
    # and then hash that, and compare it to the user's hash
    does_match = bcrypt.checkpw(password_bytes, hash_bytes)

    return does_match


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

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
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    type_liste = OptionMenu(register_screen, type_account, *OPTIONS)
    type_liste.config(highlightbackground='#0E4ED6')
    type_liste.pack()
    nom_lable = Label(register_screen, text="Nom* ")
    nom_lable.pack()
    nom_entry = Entry(register_screen, textvariable=nom)
    nom_entry.pack()
    prenom_lable = Label(register_screen, text="Prenom* ")
    prenom_lable.pack()
    prenom_entry = Entry(register_screen, textvariable=prenom)
    prenom_entry.pack()
    matricule_lable = Label(register_screen, text="Matricule * ")
    matricule_lable.pack()
    matricule_entry = Entry(register_screen, textvariable=matricule)
    matricule_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1,
           highlightbackground='#0E4ED6', command=register_user).pack()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global matricule_verify
    global password_verify

    matricule_verify = StringVar()
    password_verify = StringVar()

    global password_login_entry
    global matricule_login_entry

    Label(login_screen, text="Matricule * ").pack()
    matricule_login_entry = Entry(login_screen, textvariable=matricule_verify)
    matricule_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1,
           highlightbackground='#0E4ED6', command=login_verify).pack()


def register_user():
    nom_info = nom.get()
    prenom_info = prenom.get()
    matricule_info = matricule.get()
    password_info = password.get()
    type_info = type_account.get()

    donnees = [nom_info, prenom_info, type_info,
               matricule_info, create_bcrypt_hash(password_info)]
    connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
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


def login_verify(M,P):
    matricule1 = M
    password1 = P
    matricule_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
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
        login_sucess()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        aDict = {"user": result[0], "time C": dt_string}
        jsonString = json.dumps(aDict)
        jsonFile = open("User_Log.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    else:
        password_not_recognised()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK",
           highlightbackground='#0E4ED6', command=delete_login_success).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password or Matricule").pack()
    Button(password_not_recog_screen, text="OK", highlightbackground='#0E4ED6',
           command=delete_password_not_recognised).pack()


def LogOut():
    f = open('User_Log.json',)
    data = json.load(f)
    print(data["user"])
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    aDict = {"user": data["user"], "time D": dt_string}
    jsonString = json.dumps(aDict)
    jsonFile = open("User_Log.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", highlightbackground='#0E4ED6',
           command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    intialiser_DATABASE()
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300",
          height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30",
           highlightbackground='#0E4ED6', command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30",
           highlightbackground='#0E4ED6', command=register).pack()

    main_screen.mainloop()



LogOut()