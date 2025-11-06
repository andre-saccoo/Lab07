from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()
        #creo un dizionario per ordinare la lista di epoche cercando di inserire prima le epoche a.C in ordine dcrescente e le altre in ordine crescente
        self.roman_to_int = { 'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,  'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20, 'XXI': 21, 'XXII': 22, 'XXIII': 23, 'XXIV': 24, 'XXV': 25, 'XXVI': 26, 'XXVII': 27}

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca
        (filtri opzionali)."""
        # TODO

    # da passare alla droplist
    def get_epoche(self):
        """Restituisce la lista di tutte le epoche, la funzione key ha il compito di
        prendere la lista epoche restituita da artefatto dao"""
        lista_epoche=ArtefattoDAO.read_era()
        def key(epoca):
            parti = epoca.split() #ogni epoca è formata da tre parti: NUMERO ROMANO-> parti[0],
            numero_romano = parti[0] #che attraverso il dizionario definito sopra
            valore = self.roman_to_int[numero_romano] #gli diamo la chiave in numero romano chiedendo il valore
            is_ac = 'a.C.' in epoca #se l'epoca è a.C. va ordinata al contrario
            # Ordine: prima a.C. (0), poi d.C. (1)
            # Per a.C. mettiamo valore negativo per ordine decrescente
            if is_ac:
                return (0, -valore)
            else:
                return (1, valore)
        self.epoche_ordinate = sorted(lista_epoche, key=key) # utilizzo per ordinare la funzione definita sopra
        return self.epoche_ordinate

    #DA PASSARE ALLA PRIMA DROP LIST
    # --- MUSEI ---
    def get_musei(self):
        lista_musei=MuseoDAO.read_museum()
        return lista_musei



