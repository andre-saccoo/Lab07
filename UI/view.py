from tkinter.constants import CENTER
import flet as ft
from UI.alert import AlertManager

'''
VIEW:
- Rappresenta l'interfaccia utente
- Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.alert = AlertManager(page)
        self.controller = None

    '''funzione per mostrare i messaggi di errore'''
    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    '''funzione che imposta il controller'''
    def set_controller(self, controller):
        self.controller = controller

    '''funzione che aggiorna la pagina'''
    def update(self):
        self.page.update()

    '''funzione che crea l'interfaccia e la aggiorna'''
    def load_interface(self):
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        '''creazione delle dropdown, viene passato dal controller gli option per popolare e colleghiamo i bottoni per aggiornare il valore letto nella dropdown al cambio'''
        self.dd_Musei=ft.Dropdown(label="Museo", options=self.controller.Popola_drop_down_museo(), on_change=self.controller.Aggiorna_musei, width=400,hint_text="seleziona il museo")
        self.dd_Epoca = ft.Dropdown(label="Epoca", options=self.controller.Popola_drop_down_epoche(),on_change=self.controller.Aggiorna_epoca, width=400, hint_text="seleziona l'epoca")

        '''inserisco in una riga che verrà poi aggiunta alla pagina'''
        self.row = ft.Row(controls=[self.dd_Musei, self.dd_Epoca], alignment=ft.MainAxisAlignment.CENTER)

        '''collegare il bottone alla funzione di ricerca'''
        self.button= ft.ElevatedButton (text="Mostra Artefatti",width= 200, on_click= self.controller.mostra_artefatti)
        self.risultati= ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,
            self.txt_titolo,
            ft.Divider(),
            self.row,
            ft.Divider(),
            self.button,
            self.risultati
        )

        self.page.scroll = "adaptive"
        self.page.update()

    '''funzione per cambiare tema della pagina'''
    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()