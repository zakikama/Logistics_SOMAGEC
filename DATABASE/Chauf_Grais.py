import sqlite3

class chauf_grais:
    def __init__(self):
        self.matricule="XXXXX"
        self.nom = "init"
        self.prenom="init"
        self.fonction="init"
        self.statut="libre"
    def show_chauf_grais(self):
        print("matricule "+ self.matricule+" nom "+self.nom+" prenom "+self.prenom+" fonction "+ self.fonction)


    def sauvgarde_chauf_grais(self):
        donnees = [ self.matricule, self.nom,self.prenom,self.fonction,self.statut]
        connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
        curseur = connexion.cursor()

        
        curseur.execute('''
            INSERT INTO Chauffeurs_Graisseurs(matricule,nom,prenom,fonction,status) VALUES (?,?,?,?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde chauf_grais reussi")
def modifier_chauf_grais(fonctionM, Mat):
    don = [fonctionM,Mat]
    connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
    curseur = connexion.cursor()
    sql = '''UPDATE Chauffeurs_Graisseurs SET fonction = ? WHERE matricule = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("modification Chauffeurs_Graisseurs reussi")
def delete_Chauffeurs_Graisseurs(matricule):
    don = [matricule]
    connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
    curseur = connexion.cursor()
    sql = '''DELETE FROM Chauffeurs_Graisseurs  WHERE matricule = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("SUPPRESSION Chauffeurs_Graisseurs reussi")

def get_table_Chauffeurs_Graisseurs():
        data = ()
        with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Chauffeurs_Graisseurs")
            data = (row for row in cursor.fetchall())
            cursor.close()
        return data
def get_matricule_Chauffeurs_Graisseurs_statut(statut):
    don = [statut]
    sql = '''SELECT matricule FROM Chauffeurs_Graisseurs  WHERE status = ?'''
    data = ()
    with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute(sql, don)]
    return data

def get_matricule_Chauffeurs_Graisseurs():
    data = ()
    with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute("SELECT matricule FROM Chauffeurs_Graisseurs")]
    return data
def get_name_perso(mat):
    don = [mat]
    sql = '''SELECT nom,prenom FROM Chauffeurs_Graisseurs  WHERE matricule = ?'''
    data = ()
    with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(sql, don)
            data = (row for row in cursor.fetchall())
            cursor.close()
    return list(data)
   
