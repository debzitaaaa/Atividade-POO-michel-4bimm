#EXERCÍCIO 04

class Conta: #classe base 
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self._saldo = saldo

    def extrato(self): #lendo extrato
        return f"Extrato: R${self._saldo:.2f}"
    
    def depositar(self, valor): #método de depósito 
        if valor <= 0:
            print("Não é possível realizar esse depósito.")
        else:
            self._saldo += valor   # <-- corrigido (era __saldo)
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}")

    def sacar(self, valor): #método de saque 
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self._saldo:.2f}")
        elif valor <= 0:
            print("Valor de saque inválido. O valor deve ser positivo.")
        else:
            print(f"Saldo insuficiente. Saldo atual: R${self._saldo:.2f}, Tentativa de saque: R${valor:.2f}")


class ContaPoupanca(Conta): #classe filha 
    def render_juros(self, taxa): #método adicional 
        if taxa < 0:
            print("Taxa inválida")
            return
        
        rendimento = self._saldo * (taxa / 100) #cáluclo do rendimento 
        self._saldo += rendimento
        print(f"Juros de {taxa}% aplicados. Rendimento: R${rendimento:.2f}. Novo saldo: R${self._saldo:.2f}")

    def sacar(self, valor): #método para saque 
        if valor > 0 and valor <= self._saldo: #verificação para que não haja valores negativos
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self._saldo:.2f}")
        else:
            print("Saque negado.")

class ContaCorrente(Conta): #classe filha 
    def __init__(self, titular, numero_conta, saldo, limite_cheque_especial):
        super().__init__(titular, numero_conta, saldo)
        self.limite_cheque_especial = limite_cheque_especial 

    def sacar(self, valor): #método saque 
        if valor <= 0:
            print("Valor inválido.")
            return
        
        if self._saldo - valor >= -self.limite_cheque_especial:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self._saldo:.2f}")
        else:
            print(f"Saque negado! Limite do cheque especial ultrapassado."
                  f"Saldo atual: R${self._saldo:.2f}, Limite: -R${self.limite_cheque_especial:.2f}")

#teste poupança
p = ContaPoupanca("Débora", 123, 1000)
p.sacar(1200)      
p.render_juros(10)  
p.sacar(500)        
print(p.extrato())

#teste corrente
c = ContaCorrente("Ana", 999, 500, 1000)
c.sacar(1200)      
c.sacar(900)       
print(c.extrato())
