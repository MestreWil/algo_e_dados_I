lista = [76, 56, 99, 22, 21, 20, 34, 65]

def indiceMenor(lista):
    menor = lista[0]
    menor_indice = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_indice = i
    return menor_indice
    
print(indiceMenor(lista))

def ordenacaoporSelecao(lista):
    novaLista = []
    for i in range(len(lista)):
        menor = indiceMenor(lista)
        novaLista.append(lista.pop(menor))
    return novaLista
    
print(ordenacaoporSelecao(lista))
