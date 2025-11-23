class Main:
    pass

print('Testando o Projeto')

from Cliente import Cliente
from Conta import Conta

c1= Cliente("Flávio", 11939362816)
conta = Conta(c1.get_nome(), 1222)

conta.deposita(100)
conta.saque(50)
conta.extrato()

