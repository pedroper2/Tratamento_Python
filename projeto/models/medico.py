from projeto.enums.sexo import Sexo
from projeto.enums.unidadefederativa import UnidadeFederativa
from projeto.models.endereco import Endereco

class Medico():
    def __init__(self,crm:str,nome:str,idade:int,endereco:Endereco,sexo:Sexo) -> None:
        self.crm = crm
        self.nome = nome
        self.idade = idade 
        self.endereco = endereco
        sexo = sexo
    def __str__(self) -> str:
        return (f"\nCrm{self.crm}\nNome{self.nome}\nIdade{self.idade}\nEndereço{self.endereco}")
    
    def verifica_nome(self,nome):
        if not isinstance(nome,str):
            raise TypeError ("O nome deve ser um texto")
    

        
