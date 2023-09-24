i = False
while i == False:
    try:
        nome = input("escreva seu nome: ")
        data = int(input("digite seu ano de nascimento (entre 1922 e 2021): "))

        if (data < 2021) and (data > 1922):
            print("nome: ", nome)
            print("idade: ", 2023-data)
            i = True
        else:
            print("ano invalido")
    except Exception as erro:
        print("um ou mais dados estao invalidos", erro)