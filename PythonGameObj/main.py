from personagem import Personagem
from atributos import Atributos
from usuario import Usuario

Aplicacao = Usuario("Henrique","12345", True)

if Aplicacao.Verificar() == None:
    print("Bem-vindo ", Aplicacao.Login)
    print("Sua senha: ", Aplicacao.Senha)
    print("Logado: ", Aplicacao.Logado)

usuario = input("Digite o nome do seu Personagem: ")
cor_cabelo = input('Digite a cor do cabelo')
cor_roupa = input("Digite a cor da roupa")
classe = input("Escolha sua classe")

Caracteristicas = Personagem(usuario,cor_cabelo,cor_roupa,classe,50,50)

Caracteristicas.EncherHP(50)
Caracteristicas.EncherSP(50)

print("Nome do Personagem: ",Caracteristicas.nome_personagem)
print("Cor Cabelo: ",Caracteristicas.cor_cabelo)
print("Cor Roupa: ",Caracteristicas.cor_roupa)
print("Classe: ", Caracteristicas.classe_personagem)
print("HP Atual: ", Caracteristicas.vida)
print("SP Atual",Caracteristicas.stamina)
status_Personagem = Atributos(500,500,500)

print("ATK: ", status_Personagem.ataque)
print("INT: ", status_Personagem.inteligencia)
print("VIT: ", status_Personagem.vitalidade)

status_Personagem.aumentarAtributos(100)
print("ATK: ", status_Personagem.ataque)