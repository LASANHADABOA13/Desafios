elemento = input("Digite um elemento da lista: ")

lista = ["jose", "gabriel", "manoel", "vitor"]

def achar_elemento(elem,arr):
    achar = False

    for i in range(len(arr)):
        if arr[i] == elem:
            achar = True
        
    if achar == False:
        print("Nao foi possivel achar: " + elem)
    else:
        print("O elemento foi achado: " + elem)

achar_elemento(elemento,lista)