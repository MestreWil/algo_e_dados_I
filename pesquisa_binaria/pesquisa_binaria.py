nums = [0, 1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
            
        else:
            baixo = meio + 1
            
    return None

print(pesquisa_binaria(nums, 21))

# Exemplo de pesquisa binaria, onde o algoritmo mira no meio da lista ordenada (precisa estar ordenada para o algoritmo funcionar)
# e se o alvo for menor que o meio, ele vai para esquedar depois do meio e analisa apartir dali, e assim por diante
# se nao ele vai para a direita depois do meio e analisa dali por diante. big O(logn)