from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    @staticmethod
    def  read_museum(): #essendo static method non è necesario il self
        print ( " lettura musei da database utilizzando la query" )
        risultati = []
        cnx = ConnessioneDB.get_connection()
        if cnx in None:
            print ("CONNESSIONE AL DATABASE FALLITA")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM museo")
            for row in cursor:
                museo=Museo(row["id"],row["nome"],row["tipologia"])
                risultati.append(museo)
            cursor.close()
            cnx.close()
            return risultati

    @staticmethod
    def read_artifacts():
        print ( " lettura artefatti da database utilizzando la query" )
        risultati = []
        cnx = ConnessioneDB.get_connection()
        if cnx in None:
            print("CONNESSIONE AL DATABASE FALLITA")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM artefatto")
            for row in cursor:
                artefatto=Artefatto(row["id"],row["nome"],row["tipologia"], row["epoca"],row["id_museo"])
                risultati.append(artefatto)
            cursor.close()
            cnx.close()
            return risultati





