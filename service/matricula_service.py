from model.matricula import Matricula
from model.aluno import Aluno
from model.modalidade import Modalidade

class MatriculaService:
    def __init__(self, gerenciador_mat, gerenciador_aluno, gerenciador_mod):
        self.gerenciador_mat = gerenciador_mat
        self.gerenciador_aluno = gerenciador_aluno
        self.gerenciador_mod = gerenciador_mod

    def realizar_matricula(self, codigo_mat, codigo_aluno, codigo_mod, qtd_aulas):
        if self.gerenciador_mat.findById(codigo_mat) is not None:
            raise ValueError("Erro: O código de matricula já existe")    
        if self.gerenciador_aluno.findById(codigo_aluno) is None:
            raise ValueError(f"Erro: Aluno com o {codigo_aluno} não existe")
        
        modalidade = self.gerenciador_mod.findById(codigo_mod)
        if modalidade is None:
            raise ValueError("Erro: Modalidade não encontrada")


        if modalidade.total_alunos >= modalidade.limite_alunos:
            raise ValueError(f"Erro: A modalidade {modalidade.descricao} já atingiu o limite de {modalidade.limite_alunos} alunos")
        
        nova_matricula = Matricula(codigo_mat, codigo_aluno, codigo_mod, qtd_aulas)
        self.gerenciador_mat.save(nova_matricula)

        modalidade.total_alunos += 1
        self.gerenciador_mod.update(modalidade)        
        return True

    def listar_matriculas(self):
        matricula = self.gerenciador_mat.findAll()
        if not matricula:
            raise ValueError(f"Não existem matriculas cadastrados no sistema.")
        return matricula

    def buscar_cod(self, codigo_mat):
        matricula = self.gerenciador_mat.findById(codigo_mat) 
        if matricula is None:
            raise ValueError(f"Erro: Nenhuma matricula encontrado no sistema com o código: {codigo_mat}")
        return matricula

    def excluir(self, codigo_mat):
        self.buscar_cod(codigo_mat)
        self.gerenciador_mat.delete(codigo_mat)
        modalidade = self.gerenciador_mod.findById(matricula_excluida.codigo_modalidade)
        if modalidade is not None:
            modalidade.total_alunos -= 1
            self.gerenciador_mod.update(modalidade)

    def atualizar(self, codigo_mat, codigo_aluno, codigo_mod, qtd_aulas):
        self.buscar_cod(codigo_mat)
        mat_modificada = Matricula(codigo_mat, codigo_aluno, codigo_mod, qtd_aulas)
        self.gerenciador_mat.update(mat_modificada)

