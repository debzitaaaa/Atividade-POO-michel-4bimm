# EXERCÍCIO 3

class Funcionario: #classe base
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self): #método
        return self.salario_base

class Gerente(Funcionario): #classe filha 
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus 

    def calcular_salario(self): #classe filha 
        super().calcular_salario()
        return self.salario_base + self.bonus

class Programador(Funcionario):
    def __init__(self, nome, salario_base, horas_extras, valor_hora_extra):
        super().__init__(nome, salario_base)
        self.horas_extras = horas_extras #atributo adicional 
        self.valor_hora_extra = valor_hora_extra
        
    def calcular_salario(self):
        super().calcular_salario()
        return self.salario_base + (self.valor_hora_extra * self.horas_extras)

#testando e criando a lista
funcionarios = [
    Gerente("Nicoly", 5000, 1500),
    Gerente("Isabelly", 6000, 20000),
    Programador("Lucas", 3500, 20, 50),
    Programador("Débora", 4000, 15, 60)
]

#iterando sobre a lista 
for f in funcionarios:
    print(f"Funcionário: {f.nome}, Salário Calculado: R${f.calcular_salario():.2f}")
