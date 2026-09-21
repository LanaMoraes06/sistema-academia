class Professor: 
    def __init__(self, codigo_prof, nome, endereco, telefone):
        self.codigo_prof = int(codigo_prof)
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone 

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome or not str(novo_nome).strip():
            raise ValueError("Erro: O nome não pode ser nulo ou vazio!")
        self._nome = str(novo_nome).strip()

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        if not novo_endereco or not str(novo_endereco).strip():
            raise ValueError("Erro: O endereco não pode ser nulo ou vazio!")
        self._endereco = str(novo_endereco).strip()

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if not novo_telefone or not str(novo_telefone).strip():
            raise ValueError("Erro: O telefone não pode ser nulo ou vazio!")
        self._telefone = str(novo_telefone).strip()
