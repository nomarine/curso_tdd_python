from codigo.bytebank import Funcionario

class TestClass:    
    def test_quando_idade_recebe_07_08_1995_deve_retornar_28(self, nome = 'Teste', dt_nascimento = '01/01/1970', salario = 1111.11):
        #Given
        esperado = 28
        entrada = '07/08/1995'
        funcionario_teste = Funcionario(nome, entrada, salario)
        
        #When
        resultado = funcionario_teste.idade()
        
        #Then
        assert resultado == esperado
        
    def test_quando_nome_recebe_Rafael_Fijos_deve_retornar_Fijos(self, nome = 'Teste', dt_nascimento = '01/01/1970', salario = 1111.11):
        esperado = 'Aquino'
        entrada = 'Rafael Martins Fijos Aquino'
        funcionario_teste = Funcionario(entrada, dt_nascimento, salario)
        
        resultado = funcionario_teste.sobrenome()
        
        assert resultado == esperado