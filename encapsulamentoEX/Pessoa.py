class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self._codigo = None
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
    @property
    def nome(self):
        return self._nome

    @property
    def endereco(self):
        return self._endereco
    
    @property
    def telefone(self):
        return self._telefone

    @nome.setter
    def nome(self, novoNome):
        self._nome = novoNome
    
    @endereco.setter
    def endereco(self, novoEndereco):
        self._endereco = novoEndereco

    @endereco.setter
    def telefone(self, novoTelefone):
        self._telefone =  novoTelefone

    def __str__(self):
        return f'Nome: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}'
    
    def imprimeNome(self):
        print(f'Nome: {self.nome}')

    def imprimeTelefone(self):
        print(f'Telefone: {self.telefone}')
        

    
        