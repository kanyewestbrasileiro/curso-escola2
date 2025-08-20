nome_produto = input("nome do produto: ")
preco_produto = input("valor do produto: ")
codigo_produto = input("digite o codigo do produto: ")
continuar = int(input("quer continuar? [1]sim [0]não: "))

lista_produto = {
    "nome":nome_produto,
    "preço":preco_produto,
    "codigo":codigo_produto
}
while continuar == 1:
    print(lista_produto,continuar)

