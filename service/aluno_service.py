from model.entidades import Aluno

class AlunoService:

    def __init__(self, gerenciador_alunos):
        self.gerenciador_alunos = gerenciador_alunos

    def cadastrar_aluno(self, codigo_aluno, nome, data_nascimento, peso, altura):
        if self.gerenciador_alunos.findById(codigo_aluno) is not None:
            raise ValueError(f"Erro: O código {codigo_aluno} já está em uso por outro aluno!")
        novo_aluno = Aluno(codigo_aluno, nome, data_nascimento, peso, altura)
        self.gerenciador_alunos.save(novo_aluno)
        return True

    def listar_alunos(self):
        alunos = self.gerenciador_alunos.findAll()
        if not alunos:
            raise ValueError(f"Não existem alunos cadastrados no sistema.")
        return alunos

    def buscar_cod(self, codigo_aluno):
        aluno = self.gerenciador_alunos.findById(codigo_aluno) 
        if aluno is None:
            raise ValueError(f"Erro: Nenhum aluno encontrado no sistema com o código: {codigo_aluno}")
        return aluno

    def excluir(self, codigo_aluno):
        self.buscar_cod(codigo_aluno)
        self.gerenciador_alunos.delete(codigo_aluno)

    def atualizar(self, codigo_aluno, nome, data_nascimento, peso, altura):
        self.buscar_cod(codigo_aluno)
        aluno_modificado = Aluno(codigo_aluno, nome, data_nascimento, peso, altura)
        self.gerenciador_alunos.update(aluno_modificado)
        
    
    

        


    