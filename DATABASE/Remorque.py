import sqlite3
import matplotlib.pyplot as plt
class remorque:
    def __init__(self):
        
        self.designationRemorque = "init"
        self.immatriculationRemorque = "init"
        self.typeRemorque = "init"
        self.ptcRemorque = 0.0
        self.ptvRemorque = 0.0
        self.statut="libre"
    def show_Remorque(self):
        print("Designation "+ self.designationRemorque+" matricule " + self.immatriculationRemorque + " type " + self.typeRemorque+" ptc "+str(self.ptcRemorque)+" ptv "+str(self.ptvRemorque))


    def sauvgarde_Remorque(self):
        donnees = [ self.designationRemorque, self.immatriculationRemorque, self.typeRemorque, self.ptcRemorque, self.ptvRemorque,self.statut]
        connexion = sqlite3.connect("my_database.db")
        curseur = connexion.cursor()

        
        curseur.execute('''
            INSERT INTO Parc_Remorque(designation, immatriculation, type, ptc, ptv ,status) VALUES (?,?,?,?,?,?)
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

def delete_Remorque(matricule):
    don = [matricule]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''DELETE FROM Parc_Remorque WHERE immatriculation = ?'''
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
def get_matricule_Parc_Remorque_statut(statut):
    don = [statut]
    sql = '''SELECT immatriculation FROM Parc_Remorque  WHERE status = ?'''
    data = ()
    with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute(sql, don)]
    return data
def figure_dispo_R():
    labels = 'Stock', 'Occupé','Indispo'
    sizes = [len(get_matricule_Parc_Remorque_statut("Libre")),
                len(get_matricule_Parc_Remorque()),len(get_matricule_Parc_Remorque_statut("Panne")),]
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
    ax1.set_title('Remorques', fontsize=15, fontweight='bold',color="white",loc='left')
    fig.patch.set_facecolor('#456975')
    fig.gca().add_artist(centre_circle)
    
    return fig