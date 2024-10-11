import pytest
from projeto.models.medico import Medico
from projeto.enums.sexo import Sexo
from projeto.enums.unidadefederativa import UnidadeFederativa
from projeto.models.endereco import Endereco

@pytest.fixture
def cria_medico():
    medico01 = Medico ("554","Pedro",20,Endereco("Rua A",54,"Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO)
    return medico01

def nome_tipo_errado():
    with pytest.raises (TypeError,match= "O nome deve ser um texto"):
        Medico("554",15,20,Endereco("Rua A",54,"Salvador",UnidadeFederativa.BAHIA),Sexo.MASCULINO)

def test_verifica_Crm(cria_medico):
    assert cria_medico.crm == "554"
def test_verifica_nome(cria_medico):
    assert cria_medico.nome == "Pedro"
def test_verifica_idade(cria_medico):
    assert cria_medico.idade == 20
def test_verifica_logradouro(cria_medico):
    assert cria_medico.endereco.logradouro == "Rua A"
def test_verifica_numero(cria_medico):
    assert cria_medico.endereco.numero == 54
def test_verifica_cidade(cria_medico):
    assert cria_medico.endereco.cidade == "salvador"
def test_verifica_UnidadeFederativa(cria_medico);
    

    
        
    