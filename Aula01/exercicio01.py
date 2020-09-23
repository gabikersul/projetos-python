nome_produtos = ["banana", "maçã", "melão"]
preço_produtos = [3.8, 2.5, 6.9]
qtd_produtos = [8, 4, 2]

def imprimeProduto(num_produto):
    if(num_produto < len(nome_produtos)):
        print(nome_produtos[num_produto])
    else:
        print("num do produto inválido!")

def retiraProduto(num_produto):
    print(nome_produtos)
    if(num_produto < len(nome_produtos)):
        nome_produtos.pop(num_produto)
        print(nome_produtos)
    else:
        print("num produto inválido")


imprimeProduto(0)
retiraProduto(0)

