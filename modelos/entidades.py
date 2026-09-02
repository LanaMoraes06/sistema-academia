class Aluno:
    def __init__(self, codigo_aluno, data_nascimento, peso, altura):
        self.codigo_aluno = codigo_aluno
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.altura = altura


class Professor: 
    def __init__(self, codigo_prof, nome, endereco, telefone):
        self.codigo_prof = codigo_prof
        self.nome = nome
        self.endereco = endereco


class Modalidade:
    def __init__(self, codigo_modalidade, descricao, codigo_prof, valor_aula, limite_alunos, total_alunos):
        self.codigo_modalidade = codigo_modalidade
        self.descricao = descricao
        self.codigo_prof = codigo_prof
        self.valor_aula = valor_aula
        self.limite_alunos = limite_alunos
        self.total_alunos = total_alunos

class Matricula: 
    def __init__(self, codigo_matricula, codigo_aluno, codigo_modalidade, qtd_aulas):
        self.codigo_matricula = codigo_matricula
        self.codigo_aluno = codigo_aluno
        self.codigo_modalidade = codigo_modalidade
        self.qtd_aulas = qtd_aulas