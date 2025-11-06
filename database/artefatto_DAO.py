from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO è Classe che si occupa dell'interazione con il database secondo il pattern DAO, gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
    Leggo le informazioni relative ai musei dal db, le trasformo in oggetti DTO e li appendo alla lista risultati
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    #RICHIESTA 1: query che si occupa della lettura di tutti gli artefatti
    @staticmethod
    def read_artifacts():
        print(" lettura tutti artefatti da database utilizzando la query eseguita")
        risultati = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("CONNESSIONE AL DATABASE FALLITA")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM artefatto")
            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                risultati.append(artefatto)
                print(artefatto.id, artefatto.nome)
            cursor.close()
            cnx.close()
            return risultati

    #RICHIESTA 2: query che si occupa della lettura degli artefatti presenti in uno specifico museo
    @staticmethod
    def artifacts_for_museum(museum):
        risultati = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("CONNESSIONE AL DATABASE FALLITA")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM artefatto WHERE id_museo = %s",(museum,)) #per fargli capire che è una riga
            for row in cursor:
                artefatto=Artefatto(row["id"],row["nome"],row["tipologia"],row["epoca"], row["id_museo"])
                risultati.append(artefatto)
            cursor.close()
            cnx.close()
            return risultati

    #
    @staticmethod
    def artifacts_for_era(epoca):
        risultati = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("CONNESSIONE AL DATABASE FALLITA")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM artefatto WHERE epoca = %s",(epoca,))
            for row in cursor:
                artefatto= Artefatto (row["id"],row["nome"],row["tipologia"],row["epoca"],row["id_museo"])
                risultati.append(artefatto)
            cursor.close()
            cnx.close()
            return risultati

    @staticmethod
    def read_artifacts_for_museum_and_era (museum, era):
        risultati = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("CONNESSIONE AL DATABASE FALLITA")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM artefatto WHERE id_museo = %s AND epoca = %s",(museum,era))
            for row in cursor:
                artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
                risultati.append(artefatto)
            cursor.close()
            cnx.close()
            return risultati

    @staticmethod
    def read_era():
        risultati = []
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("CONNESSIONE AL DATABASE FALLITA")
            return None
        else:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT DISTINCT epoca FROM artefatto")
            for row in cursor:
                era= row["epoca"]
                risultati.append(era)
            cursor.close()
            cnx.close()
            return risultati




