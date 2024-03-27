from classAluno import Aluno

class AlunoEM(Aluno):
    def __init__(self,codigo, nome, matricula, ano):
        super().__init__(codigo, nome, matricula)
        self._ano = ano

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano
    
    def __str__(self) -> str:
        return super().__str__() + f' | Ano: {self.ano}'
    
    def imprimir(self):
        print(str(self)) 

alunoMedio = AlunoEM(1, 'William', '12233', 2)
alunoMedio.imprimir()