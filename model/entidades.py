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



class Modalidade:
    def __init__(self, codigo_modalidade, descricao, codigo_prof, valor_aula, limite_alunos, total_alunos):
        self.codigo_modalidade = int(codigo_modalidade)
        self.descricao = descricao
        self.codigo_prof = int(codigo_prof) 
        self.valor_aula = float(valor_aula) 
        self.limite_alunos = int(limite_alunos) 
        self.total_alunos = int(total_alunos) 

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if not nova_descricao or not str(nova_descricao).strip():
            raise ValueError("Erro: A descrição não pode ser nula ou vazia!")
        self._descricao = str(nova_descricao).strip()

    @property
    def codigo_prof(self):
        return self._codigo_prof

    @codigo_prof.setter
    def codigo_prof(self, novo_codigo_prof):
        if not novo_codigo_prof or not str(novo_codigo_prof).strip():
            raise ValueError("Erro: O código do professor não pode ser nulo ou vazio!")
        
        codigo_prof_convertido = int(novo_codigo_prof) 
        
        if codigo_prof_convertido <= 0:
            raise ValueError ("O codigo do professor deve ser maior que 0!")
            
        self._codigo_prof = codigo_prof_convertido

    @property
    def valor_aula(self):
        return self._valor_aula

    @valor_aula.setter
    def valor_aula(self, novo_valor_aula):
        if not novo_valor_aula or not str(novo_valor_aula).strip():
            raise ValueError("Erro: O valor da aula não pode ser nulo ou vazio!")
        
        valor_aula_convertida = float(novo_valor_aula) 
        
        if valor_aula_convertida <= 0:
            raise ValueError ("O valor da aula deve ser maior que 0!")
            
        self._valor_aula = valor_aula_convertida

    @property
    def limite_alunos(self):
        return self._limite_alunos

    @limite_alunos.setter
    def limite_alunos(self, novo_limite_alunos):
        if not novo_limite_alunos or not str(novo_limite_alunos).strip():
            raise ValueError("Erro: O limite de alunos não pode ser nulo ou vazio!")
        
        limite_alunos_convertido = int(novo_limite_alunos) 
        
        if limite_alunos_convertido <= 0:
            raise ValueError ("O limite de alunos deve ser maior que 0!")
            
        self._limite_alunos = limite_alunos_convertido

    @property
    def total_alunos(self):
        return self._total_alunos

    @total_alunos.setter
    def total_alunos(self, novo_total_alunos):
        if novo_total_alunos is None or str(novo_total_alunos).strip() == "":
            raise ValueError("Erro: O total de alunos não pode ser nulo ou vazio!")
        
        total_alunos_convertido = int(novo_total_alunos) 
        
        if total_alunos_convertido < 0:
            raise ValueError ("O total de alunos não pode ser menor que 0!")
            
        self._total_alunos = total_alunos_convertido

class Matricula: 
    def __init__(self, codigo_matricula, codigo_aluno, codigo_modalidade, qtd_aulas):
        self.codigo_matricula = int(codigo_matricula)
        self.codigo_aluno = int(codigo_aluno)
        self.codigo_modalidade = int(codigo_modalidade)
        self.qtd_aulas = int(qtd_aulas) 
    @property
    def qtd_aulas(self):
        return self._qtd_aulas
        
    @qtd_aulas.setter
    def qtd_aulas(self, nova_qtd_aulas):
        if not nova_qtd_aulas or not str(nova_qtd_aulas).strip():
            raise ValueError("Erro: A quantidade de aulas não pode ser nula ou vazia!")
            
        qtd_convertida = int(nova_qtd_aulas)
        if qtd_convertida <= 0:
            raise ValueError("Erro: A quantidade de aulas deve ser maior que 0!")
            
        self._qtd_aulas = qtd_convertida        