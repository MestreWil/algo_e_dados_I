# Cabeca (ponteiro) é o elemento que esta no indice 0, ele aponta para o primeiro elemento da lista, 
# ja a quantidade a quantidade de elementos da lista

# No são os elementos da nossa lista encadeada, nele temos o valor, e uma referencia do proximo (next) elemento, 
# onde ele sabe o proximo elemento da lista

class Lista:
    class No:
        def __init__(self, valor, proximo=None):
            self.valor = valor
            self.proximo = None

        def __str__(self):
            return str(self.valor)
  
    def __init__(self):
        self.__cabeca = None
        self.__quantidade = 0
    
    def __getitem__(self, posicao):
        
        if isinstance(posicao, slice):
            passo = posicao.step if posicao.step is not None else 1
            
            if passo == 0:
                raise ValueError("Passo não pode ser zero.")
            if passo > 0:
                inicio = posicao.start if posicao.start is not None else 0
                fim = posicao.stop if posicao.stop is not None else len(self)
            else:
                inicio = posicao.start if posicao.start is not None else len(self) - 1
                fim = posicao.stop if psoicao.stop is not None else - 1
                
            if inicio < 0:
                inicio = len(self) + inicio
                
            if fim < 0 and posicao.stop is not None:
                fim = len(self) + fim
        
        if posicao < 0:
            posicao = len(self) + posicao
        
        if posicao < 0 or posicao >= self.__quantidade:
            raise IndexError("Posição invélida")
    
        atual = self.__cabeca
        for i in range(posicao):
            atual = atual.proximo  

        return atual.valor
    
    def __iter__(self):
        atual = self.__cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo
    
    def __str__(self):
        return '['+ ' ,'.join([str(valor) for valor in self]) + ']'
    
    
    def __len__(self):
        return self.__quantidade
  
    def inserir(self, posicao, valor):
        novo = self.No(valor)
        self.__quantidade += 1
        # Quando a lista é vazia
        if self.__cabeca is None:
            self.__cabeca = novo
            return
    
    # Inserir na cabeca (primeira posicao)
        if posicao <= 0:
            novo.proximo = self.__cabeca
            self.__cabeca = novo
            return
    
        i = 0
        atual = self.__cabeca
        while atual.proximo is not None and i < posicao -1:
            atual = atual.proximo
            i+=1
    
        novo.proximo = atual.proximo
        atual.proximo = novo


lista = Lista()
lista.inserir(0, 5)
lista.inserir(1, 20)
lista.inserir(1, 15)
lista.inserir(1, 10)

print(lista)
print(lista[-1])