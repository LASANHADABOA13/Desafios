peso = int(input("coloque seu peso: "))
altura = float(input("coloque sua altura: "))

def calcular_imc(peso, altura):
    imc = peso/(altura*altura)
    return imc

imc = calcular_imc(peso, altura)
print(imc)