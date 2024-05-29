from class_no import No

class Lista_encadeada:
  def __init__(self):
    self.inicio = None
    self.tamanho  = 0
  
  # def adicionarNoInicio(self, valor):
  #   no = No(valor)
  #   if self.inicio == None:
  #     self.inicio = no
  #   else:
  #     no.proximo = self.inicio
  #     self.inicio = no
  #   self.tamanho += 1
  
  def imprimir(self):
    print("------Lista Encadeada--------------------------")
    if self.inicio == None:
      print( "Lista Vazia" )
    else:
      print( self.tamanho, " elementos na Lista" )
      aux = self.inicio
      while aux:
        print( aux.dado )
        aux = aux.proximo
        
  def adicionarNoInicio(self, valor):

      nodo = No(valor)

      if self.inicio:

         nodo.proximo = self.inicio

      self.inicio = nodo

      self.tamanho += 1

      self.imprimir()   
    
  
  
  def adicionarNoFim(self, valor):
    no = No(valor)
    if self.inicio == None:
      self.inicio = no
    else:
      aux = self.inicio
      while aux.proximo:
        aux =  aux.proximo
      aux.proximo = no
    self.tamanho += 1
    self.imprimir()
    
  # def removerDoInicio(self):
  #   if self.inicio == None:
  #     self.imprimir()
    
  #   elif self.inicio.proximo == None:
  #     self.inicio = None
      
  #   else:
  #     self.inicio = self.inicio.proximo 
      
  #   self.imprimir()
  
  def removerDoInicio(self):
    if self.inicio:
      self.inicio = self.inicio.proximo
      self.tamanho -= 1
    self.imprimir()
    
  def removerDoFim(self):
    if self.inicio:
      if self.inicio.proximo == None:
        self.inicio = None
      else:
        anterior = self.inicio
        aux = self.inicio.proximo
        while aux.proximo:
          anterior = aux
          aux = aux.proximo
        anterior.proximo = None
      self.tamanho -= 1
    self.imprimir()