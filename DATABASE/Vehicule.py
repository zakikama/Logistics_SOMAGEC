import sqlite3
import matplotlib.pyplot as plt
class vehicule:
    def __init__(self):
        
        self.designationVehicule = "init"
        self.immatriculationVehicule = "init"
        self.typeVehicule = "init"
        self.ptcVehicule = 0.0
        self.ptvVehicule = 0.0
        self.statut = "libre"
    def show_Vehicule(self):
        print("Designation "+ self.designationVehicule+" matricule " + self.immatriculationVehicule + " type " + self.typeVehicule+" ptc "+str(self.ptcVehicule)+" ptv "+str(self.ptvVehicule))


    def sauvgarde_Vehicule(self):
        donnees = [ self.designationVehicule, self.immatriculationVehicule, self.typeVehicule, self.ptcVehicule, self.ptvVehicule,self.statut]
        connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
        curseur = connexion.cursor()

        
        curseur.execute('''
            INSERT INTO Parc_Vehicule(designation, immatriculation, type, ptc, ptv,status ) VALUES (?,?,?,?,?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde Vehicule reussi")
def modifier_vehicule(designationnM, typeM, ptcM,ptvM,Mat):
    don = [designationnM,typeM,ptcM,ptvM,Mat]
    connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
    curseur = connexion.cursor()
    sql = '''UPDATE Parc_Vehicule SET designation = ?, type = ?,ptc = ?,ptv = ? WHERE immatriculation = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("modification Vehicule reussi")

def delete_Vehicule(matricule):
    don = [matricule]
    connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
    curseur = connexion.cursor()
    sql = '''DELETE FROM Parc_Vehicule  WHERE  immatriculation = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("SUPPRESSION Vehicule reussi")


def get_table_Parc_Vehicule():
        data = ()
        with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Parc_Vehicule")
            data = (row for row in cursor.fetchall())
        return data
def get_matricule_Parc_Vehicule():
    data = ()
    with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute("SELECT immatriculation FROM Parc_Vehicule")]
    return data
def get_matricule_Parc_Vehicule_statut(statut):
    don = [statut]
    sql = '''SELECT immatriculation FROM Parc_Vehicule  WHERE status = ?'''
    data = ()
    with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute(sql, don)]
    return data
def figure_dispo_v():
    labels = 'Stock', 'Occupé','Indispo'
    sizes = [len(get_matricule_Parc_Vehicule_statut("Libre")),
                len(get_matricule_Parc_Vehicule()),len(get_matricule_Parc_Vehicule_statut("Panne")),]
    colors = ['#F8F8F8', '#C1C1C1','#FF5E14']
    fig1, ax1 = plt.subplots()
    
    patches, texts, pcts = ax1.pie(sizes, labels=labels, wedgeprops={'linewidth': 3.0, 'edgecolor': '#456975'}, autopct='%1.1f%%', colors=colors, pctdistance=0.47,
            startangle=90)
    plt.setp(pcts, color='white', fontweight='bold')
    ax1.axis('equal') 
    centre_circle = plt.Circle((0, 0), 0.70, fc='#456975')
    for i, patch in enumerate(patches):
         texts[i].set_color("white")
    fig = plt.gcf()
    ax1.set_facecolor('#456975')
    ax1.set_title('Vehicules', fontsize=15, fontweight='bold',color="white",loc='left')
    fig.patch.set_facecolor('#456975')
    fig.gca().add_artist(centre_circle)
    
    return fig