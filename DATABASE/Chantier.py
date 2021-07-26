import sqlite3


class chantier:
    def __init__(self):

        self.intituleChantier = "init"
        self.adresseChantier = "init"
        self.villeChantier = "init"
        self.nomRespChantier = "init"

    def show_Chantier(self):
        print("libelle " + self.intituleChantier+" adresse " + self.adresseChantier +
              " ville " + self.villeChantier+" Nom Responsable "+self.nomRespChantier)

    def sauvgarde_Chantier(self):
        donnees = [self.intituleChantier, self.adresseChantier,
                   self.villeChantier, self.nomRespChantier]
        connexion = sqlite3.connect("my_database.db")
        curseur = connexion.cursor()

        curseur.execute('''
            INSERT INTO Chantier(intitule, adresse, ville, nom_responsable) VALUES (?,?,?,?)
            ''', donnees)
        connexion.commit()
        print("sauvgarde Chantier reussi")


def modifier_chantier(intituleChantierM, adresseChantierM, villeChantierM, nomRespChantierM, codeChantier):
    don = [intituleChantierM, adresseChantierM,
           villeChantierM, nomRespChantierM, codeChantier]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''UPDATE Chantier SET intitule = ? , adresse = ? ,ville = ?,nom_responsable = ? WHERE code = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("modification chantier reussi")
def delete_chantier(codeChantierS):
    don = [codeChantierS]
    connexion = sqlite3.connect("my_database.db")
    curseur = connexion.cursor()
    sql = '''DELETE FROM Chantier  WHERE code = ?'''
    curseur.execute(sql, don)
    connexion.commit()
    print("SUPPRESSION Chantier reussi")

def get_table_Chantier():
        data = ()
        with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Chantier")
            data = (row for row in cursor.fetchall())
        return data
def get_intitule_Chantier():
    data = ()
    with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute("SELECT intitule FROM Chantier")]
    return data
def get_code_Chantier():
    data = ()
    with sqlite3.connect('my_database.db') as connection:
            cursor = connection.cursor()
            data = [data[0] for data in cursor.execute("SELECT code FROM Chantier")]
    return data

