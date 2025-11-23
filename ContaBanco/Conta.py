class Conta:
    def __init__(self,titular,numero):
        self._saldo = 0
        self.titular = titular
        self.numero = numero

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,saldo):
        if saldo <0:
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self,valor):
        if valor <= self._saldo:
            self._saldo-=valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo Insuficiente")

    def deposita(self,valor):
        self.saldo+=valor

    def extrato(self):
        print(f"Cliente: ,self.titular, Saldo: R${self.saldo:.2f}")