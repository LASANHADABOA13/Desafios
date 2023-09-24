def mostrarNumero():
    print("escreva um numero maior ou igual a 100:")
    numero_valido = False

    while(numero_valido == False):
        try:
            numero = int(input())
            if (numero <= 100):
                if numero % 2 == 0:                    
                    print("O numero que voce escolheu foi: " + str(numero))
                    numero_valido = True
                elif numero % 3 == 0:
                    print("o numero que voce escolheu é divisivel por 3")
                    numero_valido = True
                else:
                    print("o numero que voce escolheu nao é par nem divisivel por 3")
            elif (numero <= 0):
                ("numero menor que 0")
            else:
                print("Numero nao é menor que 100")
        except:
            print("numero invalido")

mostrarNumero()