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
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---

        '''inserire la lista delle epoche e dei musei, sistemare poi gli attributi on chanhe forse non serve perchè c'è il bottone, cerca di capire dove è la lista dei dati'''
        self.dropdown_museo = ft.Dropdown(label="Museo",
                                          options=[ft.dropdown.Option("id", "nome") for item in model.Model._museo_dao], width=200,
                                          hint_text="seleziona il museo")  # , on_change = print("ciao")
        self.dropdown_epoca = ft.Dropdown(label="Epoca",
                                          options=[ft.dropdown.Option("1", "*"), ft.dropdown.Option("2", "**"),
                                                   ft.dropdown.Option("5", "*****")], width=200,
                                          hint_text="seleziona il museo")
        self.row = ft.Row(controls=[self.dropdown_museo, self.dropdown_epoca], alignment=ft.MainAxisAlignment.CENTER)

        # Sezione 3: Artefatti

        '''collegare il bottone alla funzione di ricerca'''
        self.button= ft.ElevatedButton (text="Mostra Artefatti",width= 200, on_click= print("fatto"))

        self.risultati= ft.ListView

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            self.row,
            ft.Divider(),

            # Sezione 3: Artefatti
            self.button,

            #lista risultati da completare
            #self.risultati
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
