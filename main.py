import conexion 
import funcoes
fun = funcoes
con = conexion.Conexion()
con.criar_banco()
def escolha_usuario(escolha):
    try: 
        escolha = int(escolha)
        if not 1<= escolha <= 5 :
            print(f"[Erro] Você digitou um numero ({escolha})porem fora das opções")
            input('Aperte ENTER Para tentar novamente...')
            return None
        return escolha
    except ValueError:
        print(f"[Erro] Você nao digitou um numero ")
        input('Aperte ENTER Para tentar novamente...')
        return None
   
while True:
    print("/-------------------Menu-------------------")
    print("|1 - Cadastrar pessoas                    |")
    print("|2 - Ver cadastros                        |")
    print("|3 - Encerrar                             |")
    print("------------------------------------------/")

    escolha = input("Digite a opção que deseja: ").strip()
    escolha = escolha_usuario(escolha)
    if escolha is None:
        continue
    elif escolha == 3:
        break
    elif escolha == 1:
        nome = input("Digite um nome: ").strip()
        nome = fun.verifica_nome(nome)
        peso = input("Digite o peso: ").strip()
        peso = fun.verifica_peso(peso)
        altura = input("Digite a altura: ").strip()
        altura = fun.verifica_altura(altura)
        con.cadastrar_pessoas(nome,peso,altura)
    elif escolha == 2:
        print("/------------------Cadastros------------------------")
        print("")
        print(f"| {'CODIGO':^8} | {'NOME':^13} | {'ALTURA':^8} | {'PESO':^8} |")
        con.ver_pessoas()
        print("")
        print("---------------------------------------------------/")
        input("Pressione ENTER para voltar ao menu...")
    else:
        pass