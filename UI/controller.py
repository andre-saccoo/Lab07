import flet as ft
from UI.view import View
from model.Model import Model

'''
CONTROLLER:
- Funziona da intermediario tra MODELLO e VIEW
- Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = 'Qualunque'
        self.epoca_selezionata = 'Qualunque'

    # POPOLA DROPDOWN
    # TODO inserire le cose da passare alla drop down
    # è necessario restituire oggetti option alla drop down
    def Popola_drop_down_epoche(self):
        lista_epoche_dd = self._model.get_epoche()
        lista_opzioni = []  # creo lista vuota
        for epoca in lista_epoche_dd:  # ciclo su tutte le epoche
            lista_opzioni.append(ft.dropdown.Option(epoca))
        return lista_opzioni  # ritorno la lista completa

    def Popola_drop_down_museo(self):
        lista_musei_dd = self._model.get_musei()
        lista_opzioni = []
        for museo in lista_musei_dd:
            lista_opzioni.append(ft.dropdown.Option(museo))
        return lista_opzioni

    # CALLBACKS DROPDOWN da passargli il valore selezionato nelle dd
    def Aggiorna_musei(self,e):
        self.museo_selezionato = self._view.dd_Musei.value
        return str(self.museo_selezionato)

    def Aggiorna_epoca(self,e):
        self.epoca_selezionata = self._view.dd_Epoca.value
        return str(self.epoca_selezionata)

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self,e):
        self._view.risultati.controls.clear()
        museo=self.museo_selezionato
        epoca=self.epoca_selezionata
        risultati=self._model.get_artefatti_filtrati(museo,epoca) # viene restituita una lista di
        if len(risultati) == 0:
            self._view.risultati.controls.append(ft.Text("Non sono presenti nei musei artefatti con le caratteristiche richieste"))
            self._view.update()
        else:
            for risultato in risultati:                               # dizionari generati con le interrogazioni
                self._view.risultati.controls.append(ft.Text(risultato)) #delle query
            self._view.update()
        return
