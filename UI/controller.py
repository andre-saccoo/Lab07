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
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO inserire le cose da passare alla drop down

    #[ft.dropdown.Option(e) for e in self.controller.lista_epoche] popolare le epoche

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    # TODO

