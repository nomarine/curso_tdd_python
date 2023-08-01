from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano)
    
    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        sobrenome = nome_quebrado[-1]
        return sobrenome

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor
    
    def _eh_socio(self):
        sobrenomes = ['Narukami', 'Hanamura', 'Amagi', 'Satonaka', 'Fijos']
        return (self._salario >= 100000) and (self.sobrenome() in sobrenomes)
    
    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self._salario * 0.1
            self._salario -= decrescimo
        return self._salario
        

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'