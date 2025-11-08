from dataclasses import dataclass

'''
    DTO (Data Transfer Object) dell'entità Artefatto, è una dataclass, si specifica cosa si vuole ottenere e viene implementata 
    in automatico nel pattern dao servono a trasferire le informazioni per il codice, dopo averle lette da database
'''

@dataclass()
class Artefatto:
    id: int
    nome: str
    tipologia: str
    epoca: str
    id_museo: str

    def __eq__(self, other):
        return isinstance(other, Artefatto) and self.id == other.id

    def __str__(self):
        return f"{self.id} | {self.nome} | Tipologia: {self.tipologia} | Epoca: {self.epoca} | Museo: {self.id_museo}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | Tipologia: {self.tipologia} | Epoca: {self.epoca} | Museo: {self.id_museo}"
