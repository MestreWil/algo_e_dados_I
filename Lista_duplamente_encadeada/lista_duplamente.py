class ListaDuplamente:
  
  class No:
    def __init__(self,valor):
      self.valor = valor
      self.proximo = None
      self.anterior = None
      
  def __init__(self):
    self.__header = None
    self.__trailer = None
    self.__quantidade = 0
    
  def __len__(self):
    return self.__quantidade

  def inserir(self, posicao, valor):
    dado = self.No(valor)
    self.__quantidade += 1
    if self.__header and self.__trailer is None:
      self.__header = dado
      self.__trailer=dado
      return
