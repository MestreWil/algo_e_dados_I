nums = [0, 1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def pesquisa_simples(lista, item):
    posicao = -1
    for items in lista:
        posicao +=1
        if items == item:
            return posicao
    return None

print(pesquisa_simples(nums,21))

# Exemplo de pesquisa simples, onde a funcao percorre item por item ate chegar no resultado