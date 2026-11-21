def verifica_nome(nome)-> str:
    while True:
        if nome != "":
            return nome
        print("nome Invalido!!!!! - Digite outro")
        nome = input("Digite o Nome: ").strip()   
def verifica_peso(peso) -> float:
    while True:
        try:
            peso = float(peso.replace(",","."))

            if not 1<=peso<=600:
                print ("[Erro] peso invalido - Digite novamente")
                peso = input("Digite um Peso: ").strip()
            else:
                return peso
        except ValueError as e:
            print ("[Erro] peso invalido - Digite novamente") 
            peso = input("Digite um Peso: ").strip()
def verifica_altura(altura) -> float:
    while True:
        try:
            altura = float(altura.replace(",","."))
            if not 0.54 <altura<=2.52:
                print('[Erro] altura invalida - Digite a altura novamente')   
                altura = input("Digite  altura: ").strip()  
            else:
                return altura   
        except ValueError as e:
            print('[Erro] altura invalida - Digite a altura novamente')   
            altura = input("Digite  altura: ").strip()  