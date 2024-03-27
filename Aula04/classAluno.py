class Aluno:
    def __init__(self, codigo, nome, matricula):
        self._codigo = codigo
        self._nome =  nome
        self._matricula = matricula
    @property
    def codigo(self):
        return self._codigo

    @property 
    def nome(self):
        return self._nome

    @property
    def matricula(self):
        return self._matricula
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    def __str__(self):
        return f'Código: {self.codigo} | Nome Aluno: {self.nome} | N° de Matrícula: {self.matricula}'
    
    def imprimir(self):
        print(str(self))

