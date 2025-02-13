class Usuario:

    def __init__(self, Login , Senha, Logado):
        self.Login = Login
        self.Senha = Senha
        self.Logado = Logado


    def Verificar(self):
        if self.Senha and self.Login == "":
            return print("Login invalido.")


    def alterarDados(self,Alterar):
        self.Senha = Alterar


