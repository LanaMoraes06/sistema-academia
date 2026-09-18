from model.entidades import Professor

class ProfessorService:

    def __init__(self, gerenciador_prof):
        self.gerenciador_prof = gerenciador_prof

    #CRUD BÁSICO
    def cadastrar_professor(self, codigo_prof, nome, endereco, telefone):
        if self.gerenciador_prof.findById(codigo_prof) is not None:
            raise ValueError(f"Erro: O código {codigo_prof} já está em uso por outro professor!")
        novo_professor = Professor(codigo_prof, nome, endereco, telefone)
        self.gerenciador_prof.save(novo_professor)
        return True

    def listar_professores(self):
        professores = self.gerenciador_prof.findAll()
        if not professores:
            raise ValueError(f"Não existem professores cadastrados no sistema.")
        return professores

    def buscar_cod(self, codigo_prof):
        professor = self.gerenciador_prof.findById(codigo_prof) 
        if professor is None:
            raise ValueError(f"Erro: Nenhum professor encontrado no sistema com o código: {codigo_prof}")
        return professor

    def excluir(self, codigo_prof):
        self.buscar_cod(codigo_prof)
        self.gerenciador_prof.delete(codigo_prof)

    def atualizar(self, codigo_prof, nome, endereco, telefone):
        self.buscar_cod(codigo_prof)
        professor_modificado = Professor(codigo_prof, nome, endereco, telefone)
        self.gerenciador_prof.update(professor_modificado)
