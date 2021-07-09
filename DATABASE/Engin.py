import sqlite3

class engin:
    def __init__(self):
        
        self.designationEngin = "init"
        self.poidsEngin = 0.0

    def show_Remorque(self):
        print("Designation "+ self.designationEngin+" poids " +str( self.poidsEngin))


    def sauvgarde_Remorque(self):
        donnees = [ self.designationEngin, self.poidsEngin]
        connexion = sqlite3.connect("my_database.db")
        curseur = connexion.cursor()

        
        curseur.execute('''
            INSERT INTO Parc_Engin(designation, poids) VALUES (?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde Engin reussi")
def modifier_engin(designationnM, poidsM,code):
    don = [designationnM,poidsM,code]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''UPDATE Parc_Engin SET designation = ?, poids = ? WHERE code = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("modification Engin reussi")
def delete_engin(code):
    don = [code]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''DELETE FROM Parc_Engin  WHERE code = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("SUPPRESSION Engin reussi")

def get_table_Parc_Engin():
        data = ()
        with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Parc_Engin")
            data = (row for row in cursor.fetchall())
        return data