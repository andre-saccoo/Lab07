from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
Museo DAO è Classe che si occupa dell'interazione con il database secondo il pattern DAO, gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
Leggo le informazioni relative ai musei dal db, e le preparo per inserirle nella drop list
"""

class MuseoDAO:
    def __init__(self):
        pass

    @staticmethod
    def  read_museum(): #essendo static method non è necesario il self
        print ( " lettura musei da database utilizzando la query" )
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
            cursor.close()
            cnx.close()
            return risultati
