from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TesteClass:
    @pytest.fixture
    def funcionario(self):
        return Funcionario('Teste', '01/01/1970', 9999.99)
    
    def teste_quando_idade_recebe_07_08_1995_deve_retornar_28(self, nome='Teste', data_nascimento='01/01/1970', salario=9999.99):
        #Given
        esperado = 28
        entrada = '07/08/1995'
        funcionario = Funcionario(nome, entrada, salario)
        
        #When
        resultado = funcionario.idade()
        
        #Then
        assert resultado == esperado
        
    def teste_quando_nome_recebe_Rafael_Fijos_deve_retornar_Fijos(self, nome='Teste', data_nascimento='01/01/1970', salario=9999.99):
        esperado = 'Aquino'
        entrada = 'Rafael Martins Fijos Aquino'
        funcionario = Funcionario(entrada, data_nascimento, salario)
        
        resultado = funcionario.sobrenome()
        
        assert resultado == esperado
        
    #@mark.skip
    def teste_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self, nome='Teste', data_nascimento='01/01/1970', salario=9999.99):
        entrada_salario = 100000
        entrada_nome = 'Rafael Fijos'
        
        esperado = 90000
        
        funcionario_teste = Funcionario(entrada_nome, data_nascimento, entrada_salario)
        
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario
        
        assert resultado == esperado
        
    @mark.calcular_bonus
    def teste_quando_calcular_bonus_recebe_1000_deve_retornar_100(self, nome='Teste', data_nascimento='01/01/1970', salario=9999.99):
        entrada = 1000
        
        esperado = 100
        
        funcionario_teste = Funcionario(nome, data_nascimento, entrada)
        
        resultado = funcionario_teste.calcular_bonus()
        
        assert resultado == esperado
                
    @mark.calcular_bonus
    # @mark.xfail
    def teste_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self, nome='Teste', data_nascimento='01/01/1970', salario=9999.99):
        with pytest.raises(Exception): 
            entrada = 1000000
        
            funcionario_teste = Funcionario(nome, data_nascimento, entrada)
        
            resultado = funcionario_teste.calcular_bonus()
        
            assert resultado
            
    # def teste_quando_str_recebe_funcionario_deve_retornar_funcionario(self, nome='Teste', data_nascimento='01/01/1970', salario=9999.99):
    #     esperado = 'Funcionario(Teste, 01/01/1970, 9999.99)'
        
    #     funcionario_teste = Funcionario(nome, data_nascimento, salario)
        
    #     resultado = funcionario_teste.__str__()
        
    #     assert resultado == esperado