class Atributos:

    def __init__(self, ataque,inteligencia,vitalidade):
        self.ataque = ataque
        self.inteligencia = inteligencia
        self.vitalidade = vitalidade


    def aumentarAtributos(self, aumentar):
        self.ataque += aumentar
        self.inteligencia += aumentar
        self.vitalidade += aumentar


    def diminuirAtributos(self, diminuir):
        self.ataque -= diminuir
        self.inteligencia -= diminuir
        self.vitalidade += diminuir


    def alterarAtributos(self, alterar):
        self.ataque = alterar
        self.inteligencia = alterar
        self.vitalidade = alterar