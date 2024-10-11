from projeto.enums.unidadefederativa import UnidadeFederativa
class Endereco():
    def __init__(self,logradouro:str,numero:int,cidade:str,unidadefederativa:UnidadeFederativa) -> None:
        self.logradouro= logradouro
        self.numero = numero
        self.cidade =  cidade
        self.unidadefederativa= unidadefederativa
    def __str__(self) -> str:
        return (f"\nLogradouro{self.logradouro}\nnumero {self.numero} \nCidade{self.cidade}\nUnidadeFederativa{self.unidadefederativa}")

