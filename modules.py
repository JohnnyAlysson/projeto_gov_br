from base_de_dados import *
from usuarios import *



def cadastrarUsuario(nome : str,cpf: str , idade : int, genero: str, endereco : str , email : str,nome_mae:str):
    infos = {
        "nome_completo":nome,
        "cpf":cpf,
        "idade": idade,
        "genero": genero,
        "endereco": endereco,
        "email":email,
        "nome_mae": nome_mae 
            }
    dados_usuarios.append(infos)
    print("Dados Cadastrados com Sucesso!")
    
def cadastrarSenha(email:str,senha:str):
    credenciais = {
        "email":email ,  
        "senha":senha
    }
    credenciais_usuarios.append(credenciais)
    print("Credenciais cadastradas com Sucesso!")