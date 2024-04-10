from Pessoa import Pessoa

class pessoaFisica(Pessoa):
    def __init__(self, nome, endereco, telefone, cpf, idade, peso, altura):
        super().__init__(nome, endereco, telefone)
        self._cpf = cpf
        self._idade = idade
        self._altura = altura
        self._peso = peso

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, novoCPF):
        self._cpf = novoCPF


    def imprimeCPF(self):
        print(f'CPF: {self.cpf}')

    def imprimeIMC(self):
        imc = self._peso / self._altura**2
        print(f'O imc do {self.nome} é {imc}')