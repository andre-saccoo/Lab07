from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    @staticmethod
    def read_artifacts():
        print(" lettura artefatti da database utilizzando la query")
        risultati = []
        cnx = ConnessioneDB.get_connection()
        if cnx in None:
            print("CONNESSIONE AL DATABASE FALLITA")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM artefatto")
            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                risultati.append(artefatto)
            cursor.close()
            cnx.close()
            return risultati

    @staticmethod
    def artidacts_for_museum():
        pass
    @staticmethod
