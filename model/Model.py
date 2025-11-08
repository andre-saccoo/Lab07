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

    # liste da passare alla funzione che popola la droplist
    def get_epoche(self):
        """Restituisce la lista di tutte le epoche, la funzione key ha il compito di prendere la lista epoche restituita da artefatto dao"""
        lista_epoche = ArtefattoDAO.read_era()
        return lista_epoche

    def get_musei(self):
        lista_musei = MuseoDAO.read_museum()
        return lista_musei

    # --- ARTEFATTI ---
    # a seconda dei valori passati alla funzione eseguo la query corrispondente
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        '''sono liste di dizionari'''

        if museo == 'Qualunque' and epoca == 'Qualunque':
            lista_artefatti=ArtefattoDAO.read_artifacts() #se entrambe le dropdown sono impostate su qualunque stampa tutti
            return lista_artefatti

        elif museo=='Qualunque' and epoca != 'Qualunque':
            lista_artefatti_per_epoca = ArtefattoDAO.artifacts_for_era(epoca)
            return lista_artefatti_per_epoca

        elif museo != 'Qualunque' and epoca =='Qualunque':
            lista_artefatti_per_museo=ArtefattoDAO.artifacts_for_museum(museo)
            return lista_artefatti_per_museo

        else:
            lista_artefatti_per_museo_e_per_epoca=ArtefattoDAO.read_artifacts_for_museum_and_era(museo,epoca)
            return lista_artefatti_per_museo_e_per_epoca



