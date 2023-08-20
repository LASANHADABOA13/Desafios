qtd_rodas = int(input("digite a quantidade de rodas: "))
peso = int(input("digite o peso bruto em KG: "))
qtd_pessoas = int(input("digite a quantidade de pessoas: "))

if (qtd_rodas <= 3):
    print("Categoria A")
elif (qtd_rodas <= 8) and (peso <= 3500):
    print("categoria B")
elif (peso >= 3500) and (peso <= 6000):
    print("categoria C")
elif (qtd_rodas >= 4) and (qtd_pessoas >= 8):
    print("categoria D")
else:
    print("categoria E")