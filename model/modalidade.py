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
