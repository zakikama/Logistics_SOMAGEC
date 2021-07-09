import sqlite3

class chauf_grais:
    def __init__(self):
        self.matricule="XXXXX"
        self.nom = "init"
        self.prenom="init"
        self.fonction="init"

    def show_chauf_grais(self):
        print("matricule "+ self.matricule+" nom "+self.nom+" prenom "+self.prenom+" fonction "+ self.fonction)


    def sauvgarde_chauf_grais(self):
        donnees = [ self.matricule, self.nom,self.prenom,self.fonction]
        connexion = sqlite3.connect("my_database.db")
        curseur = connexion.cursor()

        
        curseur.execute('''
            INSERT INTO Chauffeurs_Graisseurs(matricule,nom,prenom,fonction) VALUES (?,?,?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde chauf_grais reussi")
def modifier_chauf_grais(fonctionM, Mat):
    don = [fonctionM,Mat]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''UPDATE Chauffeurs_Graisseurs SET fonction = ? WHERE matricule = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("modification Chauffeurs_Graisseurs reussi")
def delete_Chauffeurs_Graisseurs(matricule):
    don = [matricule]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''DELETE FROM Chauffeurs_Graisseurs  WHERE matricule = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("SUPPRESSION Chauffeurs_Graisseurs reussi")

def get_table_Chauffeurs_Graisseurs():
        data = ()
        with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Chauffeurs_Graisseurs")
            data = (row for row in cursor.fetchall())
        return data