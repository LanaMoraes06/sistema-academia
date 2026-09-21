class Aluno:
    def __init__(self, codigo_aluno, nome, data_nascimento, peso, altura):
        self.codigo_aluno = int(codigo_aluno)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.altura = altura

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome or not str(novo_nome).strip():
            raise ValueError("Erro: O nome não pode ser nulo ou vazio!")
        self._nome = str(novo_nome).strip()

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data_nascimento):
        if not nova_data_nascimento or not str(nova_data_nascimento).strip():
            raise ValueError("Erro: A data de nascimento não pode ser nula ou vazia!")
        self._data_nascimento = str(nova_data_nascimento).strip()

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, novo_peso):
        if not novo_peso or not str(novo_peso).strip():
            raise ValueError("Erro: O peso não pode ser nulo ou vazio!")
            
        peso_convertido = float(novo_peso) 
        
        if peso_convertido <= 0:
            raise ValueError("Erro: O peso deve ser maior que 0!")
            
        self._peso = peso_convertido

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, nova_altura):
        if not nova_altura or not str(nova_altura).strip():
            raise ValueError("Erro: A altura não pode ser nula ou vazia!")
        
        altura_convertida = float(nova_altura) 
        
        if altura_convertida <= 0:
            raise ValueError ("A altura deve ser maior que 0!")
            
        self._altura = altura_convertida
    
    @property
    def imc(self):
        valor_imc = self.peso / (self.altura ** 2)
        return round(valor_imc, 2)  

    @property
    def classificacao_imc(self):
        valor = self.imc
        
        if valor < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= valor < 24.9:
            return "Peso normal"
        elif 25.0 <= valor < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"
