from codigo.bytebank import Funcionario
import pytest

class TestClass:
    @pytest.fixture
    def funcionario(self):
        return Funcionario('Teste', '01/01/1970', 9999.99)
    
    def test_quando_idade_recebe_07_08_1995_deve_retornar_28(self, nome='Teste', data_nascimento='01/01/1970', salario=9999.99):
        #Given
        esperado = 28
        entrada = '07/08/1995'
        funcionario = Funcionario(nome, entrada, salario)
        
        #When
        resultado = funcionario.idade()
        
        #Then
        assert resultado == esperado
        
    def test_quando_nome_recebe_Rafael_Fijos_deve_retornar_Fijos(self, nome='Teste', data_nascimento='01/01/1970', salario=9999.99):
        esperado = 'Aquino'
        entrada = 'Rafael Martins Fijos Aquino'
        funcionario = Funcionario(entrada, data_nascimento, salario)
        
        resultado = funcionario.sobrenome()
        
        assert resultado == esperado
        
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self, nome='Teste', data_nascimento='01/01/1970', salario=9999.99):
        entrada_salario = 100000
        entrada_nome = 'Rafael Fijos'
        
        esperado = 90000
        
        funcionario_teste = Funcionario(entrada_nome, data_nascimento, entrada_salario)
        
        resultado = funcionario_teste.decrescimo_salario()
        
        assert resultado == esperado