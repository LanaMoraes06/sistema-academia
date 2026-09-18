from model.entidades import Professor

class ProfessorService:

    def __init__(self, gerenciador_prof):
        self.gerenciador_prof = gerenciador_prof

    #CRUD BÁSICO
    def cadastrar_professor(self, codigo, nome, endereco, telefone):
        if self.gerenciador_prof.findById(codigo) is not None:
            raise ValueError(f"Erro: O codigo {codigo} já está em uso por outro professor!")
        novo_professor = Professor(codigo, nome, endereco, telefone)
        self.gerenciador_prof.save(novo_professor)
        return True

    def listar_professores(self):
        professores = self.gerenciador_prof.findAll()
        if not professores:
            raise ValueError(f"Não existem professores cadastrados no sistema.")
        return professores

    def buscar_cod(self, codigo):
        professor = self.gerenciador_prof.findById(codigo) 
        if professor is None:
            raise ValueError(f"Erro: Nenhum professor encontrado no sistema com o código: {codigo}")
        return professor

    def excluir(self, codigo):
        self.buscar_cod(codigo)
        self.gerenciador_prof.delete(codigo)

    def atualizar(self, codigo, nome, endereco, telefone):
        self.buscar_cod(codigo)
        professor_modificado = Professor(codigo, nome, endereco, telefone)
        self.gerenciador_prof.update(professor_modificado)
