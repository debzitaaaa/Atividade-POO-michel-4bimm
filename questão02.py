# EXERCICIO 2

class Veiculo: #classe base 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def exibir_info(self): #método
        print(f"Marca:{self.marca}, Modelo:{self.modelo}")

class Carro(Veiculo): #classe filha 
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas #atributo específico 

    def exibir_info(self):
        super().exibir_info() #sobrescrevendo método da classe mãe 
        print(f"Número de Portas:{self.numero_portas}") 

class Moto(Veiculo): #classe filha 
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas #atributo específico

    def exibir_info(self):
        super().exibir_info() #sobrescrevendo método da classe mãe 
        print(f"Cilindradas: {self.cilindradas}") 
