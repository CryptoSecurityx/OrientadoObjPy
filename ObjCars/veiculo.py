class Veiculo:

    def __init__(self, marca,modelo,cor,preco,tanque):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.tanque = tanque


    def abastecer(self, litros):
        self.tanque += litros

        return self.tanque

