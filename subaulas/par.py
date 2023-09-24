par = False
while par == False:
    try:
        numero = int(input("digite um numero para verificar: "))

        if numero % 2 == 0:
            print("este numero é par")
            par = True
        else:
            print("este numero nao é par")
            numero = int(input("tente outro: "))
    except:
        print("voce nao digitou um numero")