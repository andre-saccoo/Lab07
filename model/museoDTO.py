from dataclasses import dataclass

'''
    DTO (Data Transfer Object) dell'entità Museo
    dataclass per creare in automatico l'oggetto museo
    è una dataclass, si specifica cosa si vuole ottenere e viene implementata in automatico
    nel pattern dao servono a trasferire le informazioni per il codice, dopo averle lette da database
'''

@dataclass()
class Museo:
    id: int
    nome: str
    tipologia: str
    def __eq__(self, other):
        return isinstance(other, Museo) and self.id == other.id

    def __str__(self):
        return f"{self.id} | {self.nome} | Tipologia: {self.tipologia}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | Tipologia: {self.tipologia}"
