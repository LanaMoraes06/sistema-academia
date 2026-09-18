from model.entidades import Modalidade, Professor, Matricula

class ModalidadeService:

    def __init__(self, gerenciador_modalidade, gerenciador_prof, gerenciador_matricula):
        self.gerenciador_modalidade = gerenciador_modalidade
        self.gerenciador_prof = gerenciador_prof
        self.gerenciador_matricula = gerenciador_matricula


    def cadastrar_modalidade(self, codigo_modalidade, descricao, codigo_prof, valor_aula, limite_alunos, total_alunos):
        if self.gerenciador_modalidade.findById(codigo_modalidade) is not None:
            raise ValueError(f"Erro: O codigo {codigo_modalidade} já está em uso por outra modalidade!")
        
        if self.gerenciador_prof.findById(codigo_prof) is None:
            raise ValueError(f"Erro: Não foi encontrado professor com o código: {codigo_prof}")
        nova_modalidade = Modalidade(codigo_modalidade, descricao, codigo_prof, valor_aula,limite_alunos, total_alunos)
        self.gerenciador_modalidade.save(nova_modalidade)
        return True

    def listar_modalidade(self):
        modalidade = self.gerenciador_modalidade.findAll()
        if not modalidade:
            raise ValueError(f"Não existem modalidades cadastrados no sistema.")
        return modalidade

    def buscar_cod(self, codigo_modalidade):
        modalidade = self.gerenciador_modalidade.findById(codigo_modalidade) 
        if modalidade is None:
            raise ValueError(f"Erro: Nenhuma modalidade encontrada no sistema com o código: {codigo_modalidade}")
        return modalidade

    def excluir(self, codigo_modalidade):
        self.buscar_cod(codigo_modalidade)
        self.gerenciador_modalidade.delete(codigo_modalidade)

    def atualizar(self, codigo_modalidade, descricao, codigo_prof, valor_aula,limite_alunos, total_alunos):
        self.buscar_cod(codigo_modalidade)
        modalidade_modificada = Modalidade(codigo_modalidade, descricao, codigo_prof, valor_aula,limite_alunos, total_alunos)
        self.gerenciador_modalidade.update(modalidade_modificada)

    def calcular_faturamento(self, codigo_modalidade):
        modalidade = self.buscar_cod(codigo_modalidade)
        
        professor = self.gerenciador_prof.findById(modalidade.codigo_prof)
        nome_professor = professor.nome if professor else "Sem professor"

        todas_matriculas = self.gerenciador_matricula.findAll()
        
        faturamento_total = 0
        if todas_matriculas:
            for matricula in todas_matriculas:
                if int(matricula.codigo_modalidade) == int(codigo_modalidade):
                    faturamento_total += (modalidade.valor_aula * matricula.qtd_aulas)


        return modalidade.descricao, nome_professor, faturamento_total
