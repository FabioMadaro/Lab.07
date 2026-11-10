import flet as ft
from UI.view import View
from model.model import Model

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
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def load_initial_data(self):
        self._view.dd_biblioteca.options.clear()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for b in self._model.get_biblioteche():
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(b.nome))

        self._view.dd_genere.options.clear()
        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for g in self._model.get_generi():
            if g:
                self._view.dd_genere.options.append(ft.dropdown.Option(str(g)))
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def read_biblioteca(self, e):
        self.biblioteca_selezionata = self._view.dd_biblioteca.value

    def read_genere(self, e):
        self.genere_selezionato = self._view.dd_genere.value

    # AZIONE: MOSTRA LIBRI
    # TODO
    def handle_mostra_libri(self, e):
        bib = self._view.dd_biblioteca.value
        gen = self._view.dd_genere.value
        if not bib: bib = "Nessun filtro"
        if not gen: gen = "Nessun filtro"

        libri = self._model.get_libri_filtrati(bib, gen)
        self._view.list_view.controls.clear()

        if not libri:
            self._view.show_alert("Nessun libro soddisfa i criteri di filtraggio indicati.")
        else:
            for libro in libri:
                info = f"Titolo: {getattr(libro, 'titolo', 'N/D')} | Autore: {getattr(libro, 'autore', 'N/D')} | Genere: {getattr(libro, 'genere', 'N/D')}"
                self._view.list_view.controls.append(ft.Text(info))
        self._view.update()
