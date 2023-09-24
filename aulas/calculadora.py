def soma(num1,num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def divisao(num1,num2):
    return num1 / num2

def multiplicacao(num1,num2):
    return num1 * num2

print("operaçoes: 1 - soma")
print("operaçoes: 2 - subtração")
print("operaçoes: 3 - divisão")
print("operaçoes: 4 - multiplicaçao")

operacao = int(input("digite a operação: "))

num1 = float(input("digite um numero: "))
num2 = float(input("digite outro numero: "))

match operacao:
    case 1:
        res = soma(num1,num2)
        print(res)
    case 2:
        res = subtracao(num1,num2)
        print(res)
    case 3:
        res = divisao(num1,num2)
        print(res)
    case 4:
        res = multiplicacao(num1,num2)
        print(res)
    case _:
        "operação invalida"