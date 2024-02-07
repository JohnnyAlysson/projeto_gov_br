

from modules import *


print("*"*20," Inicio do programa ","*"*20)

print("*"*20," Cadastro do usuario ","*"*10)

nome_completo = input("Digite seu nome completo: ").title()
cpf = input("Digite seu cpf (apenas numeros):")
idade = int(input("Digite sua idade: ")) #  Escolha do byte de devido sua quantidade limitada de 256
genero = input("Digite seu genero: ")
endereco = input("Qual seu endereco:")
email = input("Digite seu email:")
nome_mae = input("Digite o nome da sua mae:")

while True:
    senha = input("Cadastre uma senha:")
    confirmacao_senha= input("Digite a confirmacao da sua senha:")
    if senha == confirmacao_senha:
        break
    else:
        print("Senha e confirmacao de senha diferentes, tente novamente. ")

cadastrarUsuario(nome_completo,idade,genero,endereco,cpf,email,nome_mae)
cadastrarSenha(email,senha)








if __name__ == "__main__":
    print("Testando")

    print(dados_usuarios)
    print(credenciais_usuarios)