class Televisor:
    def __init__(self, fab, modelo):
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 20

    def aumentaVolume(self, valor):
        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100

    def diminuiVolume(self, valor):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocaCanal(self, canal):
        if canal in self.lista_de_canais:
            self.canal_atual = canal

    def sintonizaCanal(self, canal):
        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)


# Exemplo de uso
tv = Televisor("Samsung", "SmartTV")

# Sintonizando canais
tv.sintonizaCanal(5)
tv.sintonizaCanal(7)
tv.sintonizaCanal(13)

# Trocando de canal
tv.trocaCanal(7)

# Ajustando volume
tv.aumentaVolume(15)
tv.diminuiVolume(10)

# Mostrando informações
print("Fabricante:", tv.fabricante)
print("Modelo:", tv.modelo)
print("Canal Atual:", tv.canal_atual)
print("Lista de Canais:", tv.lista_de_canais)
print("Volume:", tv.volume)