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