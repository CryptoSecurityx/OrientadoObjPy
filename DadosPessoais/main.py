from cliente import Cliente

Sistema = Cliente('crypto','henrique',123943,16997979975,495011844888,23)

def dados():

    print("---------------------------")
    print("- Seus Dados Cadastrados --")
    print("---------------------------")
    print ("Usuario ",Sistema.usuario)
    print("Nome ",Sistema.nome)
    print ("Senha ",Sistema.senha)
    print("cpf ",Sistema.cpf)
    print ("idade ",Sistema.idade)
    print("celular ",Sistema.celular)
    print("----------------------------\n")

dados()

RetornoUsuario = input("Deseja alterar a senha? S/N ")

if RetornoUsuario.lower() == 's':
    novasenha = input("Agora Digite sua nova senha: ")
    Sistema.alterarSenha(novasenha)

    print("Senha Alterada para", novasenha)
else:
    print("a senha nao foi alterada.")


