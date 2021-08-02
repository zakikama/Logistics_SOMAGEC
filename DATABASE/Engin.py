import sqlite3
import matplotlib.pyplot as plt
class engin:
    def __init__(self):
        
        self.designationEngin = "init"
        self.poidsEngin = 0.0
        self.statut="libre"
    def show_Remorque(self):
        print("Designation "+ self.designationEngin+" poids " +str( self.poidsEngin))


    def sauvgarde_Engin(self):
        donnees = [ self.designationEngin, self.poidsEngin,self.statut]
        connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
        curseur = connexion.cursor()

        
        curseur.execute('''
            INSERT INTO Parc_Engin(designation, poids,status) VALUES (?,?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde Engin reussi")
def modifier_engin(designationnM, poidsM,code):
    don = [designationnM,poidsM,code]
    connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
    curseur = connexion.cursor()
    sql = '''UPDATE Parc_Engin SET designation = ?, poids = ? WHERE code = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("modification Engin reussi")
def delete_engin(code):
    don = [code]
    connexion = sqlite3.connect("DATABASE/Assets/my_database.db")
    curseur = connexion.cursor()
    sql = '''DELETE FROM Parc_Engin  WHERE code = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("SUPPRESSION Engin reussi")

def get_table_Parc_Engin():
        data = ()
        with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Parc_Engin")
            data = (row for row in cursor.fetchall())
        return data
def get_designation_Parc_Engin():
    data = ()
    with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute("SELECT designation FROM Parc_Engin")]
    return data
def get_code_Parc_Engin():
    data = ()
    with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute("SELECT code FROM Parc_Engin")]
    return data
def get_code_Parc_Engin_statut(statut):
    don = [statut]
    sql = '''SELECT code FROM Parc_Vehicule  WHERE status = ?'''
    data = ()
    with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute(sql, don)]
    return data
def get_designation_Parc_Engin_statut(statut):
    don = [statut]
    sql = '''SELECT designation FROM Parc_Vehicule  WHERE status = ?'''
    data = ()
    with sqlite3.connect('DATABASE/Assets/my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute(sql, don)]
    return data
def figure_dispo_E():
    labels = 'Stock', 'Occupé','Indispo'
    sizes = [len(get_designation_Parc_Engin_statut("Libre")),
                len(get_designation_Parc_Engin()),len(get_designation_Parc_Engin_statut("Panne")),]
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
    ax1.set_title('Engins', fontsize=15, fontweight='bold',color="white",loc='left')
    fig.patch.set_facecolor('#456975')
    fig.gca().add_artist(centre_circle)
    
    return fig