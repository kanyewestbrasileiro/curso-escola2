nome = input("nome: ")
preço = input("preço: ")
continuar = int(input("quer continuar? [1]sim [2]nao: "))
while continuar == 1:
    input("nome: ")
    input("preço: ")

lista_produtos = {
    "nome":nome,
    "preço":preço
}
if continuar == 0:
    print(lista_produtos)