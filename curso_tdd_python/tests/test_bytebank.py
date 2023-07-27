from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_07_08_1995_deve_retornar_28(self):
        #Given
        esperado = 28
        entrada = '07/08/1995'
        funcionario_teste = Funcionario('Teste', entrada, 8000)
        
        #When
        resultado = funcionario_teste.idade()
        
        #Then
        assert resultado == esperado