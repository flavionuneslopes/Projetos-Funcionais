from televisor import Televisor


class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv

    def aumentaVolume(self):
        # Aumenta o volume da TV em 90 (ou até o máximo)
        self.tv.aumentaVolume(90)

    def diminuiVolume(self):
        # Diminui o volume da TV em 90 (ou até o mínimo)
        self.tv.diminuiVolume(90)

    def trocaCanal(self, canal):
        # Troca para um canal já sintonizado
        self.tv.trocaCanal(canal)

    def sintonizaCanal(self, canal):
        # Sintoniza um novo canal na TV
        self.tv.sintonizaCanal(canal)


# Exemplo de uso
tv = Televisor("LG", "OLED")
controle = ControleRemoto(tv)

# Sintonizando canais
controle.sintonizaCanal(3)
controle.sintonizaCanal(5)

# Trocando de canal
controle.trocaCanal(5)

# Ajustando volume
controle.aumentaVolume()
controle.diminuiVolume()

# Mostrando informações da TV
print("Canal Atual:", tv.canal_atual)
print("Lista de Canais:", tv.lista_de_canais)
print("Volume:", tv.volume)