produtos = ["Sabao", "bolacha", "pao", "arroz"]
print("produtos disponiveis: ", produtos)

def substituir_item(produtos):
    prod_substituicao = input("produto a ser substituido: ")

    for i in produtos:
        if i == prod_substituicao:
            produtos.pop(prod_substituicao)
            prod_novo = input("produto a ser adicionado: ")
            produtos.append(prod_novo)

substituir_item(produtos)