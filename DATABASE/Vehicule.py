import sqlite3

class vehicule:
    def __init__(self):
        
        self.designationVehicule = "init"
        self.immatriculationVehicule = "init"
        self.typeVehicule = "init"
        self.ptcVehicule = 0.0
        self.ptvVehicule = 0.0

    def show_Vehicule(self):
        print("Designation "+ self.designationVehicule+" matricule " + self.immatriculationVehicule + " type " + self.typeVehicule+" ptc "+str(self.ptcVehicule)+" ptv "+str(self.ptvVehicule))


    def sauvgarde_Vehicule(self):
        donnees = [ self.designationVehicule, self.immatriculationVehicule, self.typeVehicule, self.ptcVehicule, self.ptvVehicule]
        connexion = sqlite3.connect("my_database.db")
        curseur = connexion.cursor()

        
        curseur.execute('''
            INSERT INTO Parc_Vehicule(designation, immatriculation, type, ptc, ptv ) VALUES (?,?,?,?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde Vehicule reussi")
def modifier_vehicule(designationnM, typeM, ptcM,ptvM,code,Mat):
    don = [designationnM,typeM,ptcM,ptvM,code,Mat]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''UPDATE Parc_Vehicule SET designation = ?, type = ?,ptc = ?,ptv = ? WHERE code = ? or immatriculation = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("modification Vehicule reussi")

def delete_Vehicule(code,matricule):
    don = [code,matricule]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''DELETE FROM Parc_Vehicule  WHERE code = ? OR immatriculation = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("SUPPRESSION Vehicule reussi")


def get_table_Parc_Vehicule():
        data = ()
        with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Parc_Vehicule")
            data = (row for row in cursor.fetchall())
        return data