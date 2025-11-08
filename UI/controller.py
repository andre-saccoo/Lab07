import flet as ft
from UI.view import View
from model.Model import Model
from model.museoDTO import Museo

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
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO inserire le cose da passare alla drop down

    def Popola_drop_down_epoche(self):
        lista_epoche_dd=Model.get_epoche()
        return lista_epoche_dd

    def Popola_drop_down_museo(self):
        lista_musei_dd=Model.get_musei()
        return lista_musei_dd


    # CALLBACKS DROPDOWN da passargli il valore selezionato nelle dd
    def Aggiorna_musei(self,e):
        self.museo_selezionato = view
        return self.museo_selezionato

    def Aggiorna_epoca(self):
        self.epoca_selezionata = view.
        pass

    #[ft.dropdown.Option(e) for e in self.controller.lista_epoche] popolare le epoche



    # AZIONE: MOSTRA ARTEFATTI
    # TODO'''
    def mostra_artefatti(self,e):
        museo=self.museo_selezionato
        epoca=self.epoca_selezionata
        self.view.lis

