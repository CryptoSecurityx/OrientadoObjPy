class Personagem:

    def __init__(self,nome_personagem,cor_cabelo,cor_roupa,classe_personagem,vida,stamina):

        self.nome_personagem = nome_personagem
        self.cor_cabelo = cor_cabelo
        self.cor_roupa = cor_roupa
        self.classe_personagem = classe_personagem
        self.vida = vida
        self.stamina = stamina


    def EncherHP(self, quantidadeHP):
        self.vida += quantidadeHP
        return self.vida

    def EncherSP(self, quantidadeSP):
        self.stamina += quantidadeSP
        return self.stamina




