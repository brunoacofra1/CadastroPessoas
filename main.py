import conexion 
con = conexion.Conexion()
con.criar_banco()
def escolha_usuario(escolha):
    try: 
        escolha = int(escolha)
        if not 1<= escolha <= 5 :
            print(f"[Erro] Você digitou um numero porem fora das opções")
            input('Aperte ENTER Para tentar novamente...')
            return None
        return escolha
    except ValueError:
        print(f"[Erro] Você nao digitou um numero ")
        input('Aperte ENTER Para tentar novamente...')
        return None
def verifica_nome(nome)-> str:
    while True:
        if nome != "":
            return nome
        print("nome Invalido!!!!! - Digite outro")
        nome = input("Digite o Nome: ").strip()     
        
while True:
    print("/------------------------------------------")
    print("|1 - Cadastrar pessoas                    |")
    print("|2 - Ver cadastros                        |")
    print("|3 - Excluir cadastros                    |")
    print("|4 - Editar cadastros                     |")
    print("|5 - Encerrar                             |")
    print("------------------------------------------/")

    escolha = input("Digite a opção que deseja: ").strip()
    escolha = escolha_usuario(escolha)
    if escolha is None:
        continue
    elif escolha == 5:
        break
    elif escolha == 1:
        nome = input("Digite um nome: ").strip()
        nome = verifica_nome(nome)
        peso = input("Digite o peso: ").strip()
        altura = input("Digite a altura: ").strip()
    elif escolha == 2:
        pass
    elif escolha == 3:
        pass 
    else:
        pass