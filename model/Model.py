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

    '''
    creo le due funzioni che si occupano dell'interrogazione del pattern DAO, chiamo le funzioni read_era e read_museum dai rispettivi
    file importati, vengono restituite due lista quando le funzioni vengono chiamate: una con le epoche, una con i musei; queste liste vengono 
    passate alle due droplist per popolarle attraverso le due funzioni popola droplist nel controller
    '''
    def get_epoche(self):
        """Restituisce la lista di tutte le epoche, la funzione key ha il compito di prendere la lista epoche restituita da artefatto dao"""
        lista_epoche = ArtefattoDAO.read_era()
        return lista_epoche

    def get_musei(self):
        lista_musei = MuseoDAO.read_museum()
        return lista_musei


    # --- ARTEFATTI ---
    ''' 
    creo una funzione per restituire i risultati dopo che l'utente ha selezionato ciò che desidera dalla droplist, vengono restituire
    liste di dizionari contenenti tutti gli artefatti filtrati. A seconda dei parametri passati viene eseguita una differente query 
    del file artefatto_DAO
    '''

    def get_artefatti_filtrati(self, museo:str, epoca:str):

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