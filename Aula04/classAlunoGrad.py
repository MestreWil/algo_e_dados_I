from classAluno import Aluno

class AlunoGrad(Aluno):
    def __init__(self,codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self._semestre = semestre

    @property
    def semestre(self):
        return self._semestre

    @semestre.setter
    def semestre(self, semestre):
        self._semestre = semestre

    def __str__(self) -> str:
        return super().__str__() + f' | Semestre: {self.semestre}'

    def imprimir(self):
        print(str(self))

