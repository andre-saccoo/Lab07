from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
MUSEO DAO
 è Classe che si occupa dell'interazione con il database secondo il pattern DAO, 
gestisce le operazioni di accesso al database relative ai musei, effettua la Query
per la lettura dei musei, le trasforma in oggetti DTO e li appende alla lista
 di dizionari dei risultati .
"""

class MuseoDAO:
    def __init__(self):
        pass

    @staticmethod
    def  read_museum(): #essendo static method non è necessario il self
        #print (" lettura musei da database utilizzando la query")
        risultati = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print ("CONNESSIONE AL DATABASE FALLITA")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM museo")
            for row in cursor:
                museo=Museo(row["id"],row["nome"],row["tipologia"])
                risultati.append(museo)
            risultati.insert(0,'Qualunque')
            cursor.close()
            cnx.close()
            return risultati

