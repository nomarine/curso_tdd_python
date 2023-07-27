from codigo.bytebank import Funcionario

def teste_idade():
    funcionario = Funcionario('Teste', '07/08/1995', 8000)
    print(f'Teste idade: {funcionario.idade()}')