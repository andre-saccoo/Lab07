from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
ARTEFATTO DAO 
è una Classe che si occupa dell'interazione con il database secondo il pattern DAO,
 gestisce le operazioni di accesso al database relative agli artefatti, effettua le Query
 per la lettura degli artefatti, le trasforma in oggetti DTO e li appende alla lista
 di dizionari dei risultati .
"""

class ArtefattoDAO:
    def __init__(self):
        pass


    '''
    RICHIESTA 1: query che si occupa della lettura di tutti gli artefatti, se la connessione fallisce viene comunicato, 
    se la connessione va a buon fine, leggiamo i dati, li metto in dizionari e li appendo alla lista
    '''
    @staticmethod
    def read_artifacts():
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
            cursor.close()
            cnx.close()
            return risultati


    '''
    RICHIESTA 2: query che si occupa della lettura di tutti gli artefatti presenti in uno specifico museo, 
    se la connessione fallisce viene comunicato, se la connessione va a buon fine, leggiamo i dati, li metto 
    in dizionari e li appendo alla lista
    '''
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


    '''
    RICHIESTA 3: query che si occupa della lettura di tutti gli artefatti di una specifica epoca, 
    se la connessione fallisce viene comunicato, se la connessione va a buon fine, leggiamo i dati, li metto 
    in dizionari e li appendo alla lista
    '''
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

    '''
    RICHIESTA 4: query che si occupa della lettura di tutti gli artefatti presenti in uno specifico museoe una specifica epoca, 
    se la connessione fallisce viene comunicato, se la connessione va a buon fine, leggiamo i dati, li metto 
    in dizionari e li appendo alla lista
    '''
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

    '''
    funzione che si occupa della lettura delle epoche per creare l'elenco da passare alla droplist, aggiungo anche l'elemento "Qualunque"
    nel caso non sia necessario filtrare per epoche
    '''
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

        '''funzione che converte i numeri romani in interi per ordinare l'elenco di epoche, alla funzione sorted viene passato 0/1 e un numero per ordinare'''
        def key(epoca):
            # creo un dizionario per ordinare la lista di epoche cercando di inserire prima le epoche a.C in ordine decrescente e le altre in ordine crescente
            roman_to_int = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
                                 'X': 10,
                                 'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15, 'XVI': 16, 'XVII': 17,
                                 'XVIII': 18,
                                 'XIX': 19, 'XX': 20, 'XXI': 21, 'XXII': 22, 'XXIII': 23, 'XXIV': 24, 'XXV': 25,
                                 'XXVI': 26,
                                 'XXVII': 27}
            parti = epoca.split()  # ogni epoca è formata da tre parti: NUMERO ROMANO-> parti[0],
            numero_romano = parti[0]  # che attraverso il dizionario definito sopra
            valore = roman_to_int[numero_romano]  # gli diamo la chiave in numero romano chiedendo il valore
            is_ac = 'a.C.' in epoca  # se l'epoca è a.C. va ordinata al contrario
                # Ordine: prima a.C. (0), poi d.C. (1)
                # Per a.C. mettiamo valore negativo per ordine decrescente
            if is_ac:
                return (0, -valore)  # restituiamo una tupla di valori: 0 se a.C 1 se d.C
            else:  # e il valore per permettere alla funzione sorte di ordinare correttamente
                return (1, valore)

        epoche_ordinate = sorted(risultati, key=key)
        epoche_ordinate.insert(0,"Qualunque")
        cursor.close()
        cnx.close()
        return epoche_ordinate



