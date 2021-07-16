import sqlite3

class remorque:
    def __init__(self):
        
        self.designationRemorque = "init"
        self.immatriculationRemorque = "init"
        self.typeRemorque = "init"
        self.ptcRemorque = 0.0
        self.ptvRemorque = 0.0

    def show_Remorque(self):
        print("Designation "+ self.designationRemorque+" matricule " + self.immatriculationRemorque + " type " + self.typeRemorque+" ptc "+str(self.ptcRemorque)+" ptv "+str(self.ptvRemorque))


    def sauvgarde_Remorque(self):
        donnees = [ self.designationRemorque, self.immatriculationRemorque, self.typeRemorque, self.ptcRemorque, self.ptvRemorque]
        connexion = sqlite3.connect("my_database.db")
        curseur = connexion.cursor()

        
        curseur.execute('''
            INSERT INTO Parc_Remorque(designation, immatriculation, type, ptc, ptv ) VALUES (?,?,?,?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde Remorque reussi")
def modifier_remorque(designationnM, typeM, ptcM,ptvM,Mat):
    don = [designationnM,typeM,ptcM,ptvM,Mat]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''UPDATE Parc_Remorque SET designation = ?, type = ?,ptc = ?,ptv = ? WHERE immatriculation = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("modification Remorque reussi")

def delete_Remorque(code,matricule):
    don = [code,matricule]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''DELETE FROM Parc_Remorque  WHERE code = ? OR immatriculation = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("SUPPRESSION Remorque reussi")

def get_table_Parc_Remorque():
        data = ()
        with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Parc_Remorque")
            data = (row for row in cursor.fetchall())
        return data
def get_matricule_Parc_Remorque(): 
    data = ()
    with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute("SELECT immatriculation FROM Parc_Remorque")]
    return data