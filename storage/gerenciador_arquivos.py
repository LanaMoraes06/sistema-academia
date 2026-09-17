import os
from estruturas.arvore_binaria import ArvoreBinaria
from modelos.entidades import Aluno, Professor, Modalidade, Matricula

class GerenciadorAlunos:
    def __init__(self, caminho_arquivo="data/alunos.txt"):
        self.arquivo = caminho_arquivo
        self.arvore = ArvoreBinaria()
        self._carregar_indices() #ele reconstroi a arvore
                                                                                #"a" = append, adicionar
    def _carregar_indices(self):                                                #"r" read, ler
        with open(self.arquivo, "a+", encoding="utf-8") as f:
            f.seek(0) 
            posicao_atual = f.tell() 
            linha = f.readline()
            while linha:
                dados = linha.strip().split(';')
                codigo_aluno = int(dados[0])
                self.arvore.inserir_no(codigo_aluno, posicao_atual)
                posicao_atual = f.tell() 
                linha = f.readline()
    
    def salvar(self, aluno: Aluno):                            
        with open(self.arquivo, "a", encoding="utf-8") as f:
            posicao = f.tell()
            linha_texto = f"{aluno.codigo_aluno};{aluno.nome};{aluno.data_nascimento};{aluno.peso};{aluno.altura}\n"
            f.write(linha_texto)
            self.arvore.inserir_no(aluno.codigo_aluno, posicao)

    def buscar_codigo(self, codigo_aluno):
        posicao = self.arvore.buscar(codigo_aluno)

        if posicao is None:
            return None
        
        with open(self.arquivo, "r", encoding="utf-8") as f:
            f.seek(posicao)
            linha = f.readline().strip()
            dados = linha.split(';')
            return Aluno(dados[0],dados[1],dados[2],dados[3],dados[4])


    def listar(self):
        posicoes = self.arvore.obter_posicoes_em_ordem()
        alunos_cadastrados = []
        with open(self.arquivo, "r", encoding="utf-8") as f:
            for pos in posicoes:
                f.seek(pos)
                linha = f.readline().strip()
                dados = linha.split(';')
                aluno = Aluno(dados[0],dados[1],dados[2],dados[3],dados[4])
                alunos_cadastrados.append(aluno)
            return alunos_cadastrados

    def excluir(self, codigo_aluno):
        posicao = self.arvore.buscar(codigo_aluno)

        if posicao is None:
            return False
        todos_alunos = self.listar()

        with open(self.arquivo, "w", encoding="utf-8") as f:
            pass
            self.arvore = ArvoreBinaria()

        for aluno in todos_alunos:
            if aluno.codigo_aluno != codigo_aluno:
                self.salvar(aluno) 
                
        return True


    def atualizar(self, aluno_modificado: Aluno):
            if self.arvore.buscar(aluno_modificado.codigo_aluno) is None:
                return False 
            self.excluir(aluno_modificado.codigo_aluno)
            self.salvar(aluno_modificado)
            
            return True

class GerenciadorProfessor:
    def __init__(self, caminho_arquivo="data/professor.txt"):
        self.arquivo = caminho_arquivo
        self.arvore = ArvoreBinaria()
        self._carregar_indices() 
                                                                            
    def _carregar_indices(self):                                                
        with open(self.arquivo, "a+", encoding="utf-8") as f:
            f.seek(0) 
            posicao_atual = f.tell() 
            linha = f.readline()
            while linha:
                dados = linha.strip().split(';')
                codigo_prof = int(dados[0])
                self.arvore.inserir_no(codigo_prof, posicao_atual)
                posicao_atual = f.tell() 
                linha = f.readline()
    
    def salvar(self, prof: Professor):                            
        with open(self.arquivo, "a", encoding="utf-8") as f:
            posicao = f.tell()
            linha_texto = f"{prof.codigo_prof};{prof.nome};{prof.endereco};{prof.telefone}\n"
            f.write(linha_texto)
            self.arvore.inserir_no(prof.codigo_prof, posicao)

    def buscar_codigo(self, codigo_prof):
        posicao = self.arvore.buscar(codigo_prof)

        if posicao is None:
            return None
        
        with open(self.arquivo, "r", encoding="utf-8") as f:
            f.seek(posicao)
            linha = f.readline().strip()
            dados = linha.split(';')
            return Professor(dados[0],dados[1],dados[2],dados[3])


    def listar(self):
        posicoes = self.arvore.obter_posicoes_em_ordem()
        professor_cadastrados = []
        with open(self.arquivo, "r", encoding="utf-8") as f:
            for pos in posicoes:
                f.seek(pos)
                linha = f.readline().strip()
                dados = linha.split(';')
                prof = Professor(dados[0],dados[1],dados[2],dados[3])
                professor_cadastrados.append(prof)
            return professor_cadastrados

    def excluir(self, codigo_prof):
        posicao = self.arvore.buscar(codigo_prof)

        if posicao is None:
            return False
        todos_professores = self.listar()

        with open(self.arquivo, "w", encoding="utf-8") as f:
            pass
            self.arvore = ArvoreBinaria()

        for prof in todos_professores:
            if prof.codigo_prof != codigo_prof:
                self.salvar(prof) 
                
        return True


    def atualizar(self, prof_modificado: Professor):
            if self.arvore.buscar(prof_modificado.codigo_prof) is None:
                return False 
            self.excluir(prof_modificado.codigo_prof)
            self.salvar(prof_modificado)
            
            return True

class GerenciadorModalidade:
    def __init__(self, caminho_arquivo="data/modalidade.txt"):
        self.arquivo = caminho_arquivo
        self.arvore = ArvoreBinaria()
        self._carregar_indices() 
                                                                            
    def _carregar_indices(self):                                                
        with open(self.arquivo, "a+", encoding="utf-8") as f:
            f.seek(0) 
            posicao_atual = f.tell() 
            linha = f.readline()
            while linha:
                dados = linha.strip().split(';')
                codigo_modalidade = int(dados[0])
                self.arvore.inserir_no(codigo_modalidade, posicao_atual)
                posicao_atual = f.tell() 
                linha = f.readline()
    
    def salvar(self, mod: Modalidade):                            
        with open(self.arquivo, "a", encoding="utf-8") as f:
            posicao = f.tell()
            linha_texto = f"{mod.codigo_modalidade};{mod.descricao};{mod.codigo_prof};{mod.valor_aula};{mod.limite_alunos};{mod.total_alunos}\n"
            f.write(linha_texto)
            self.arvore.inserir_no(mod.codigo_modalidade, posicao)

    def buscar_codigo(self, codigo_modalidade):
        posicao = self.arvore.buscar(codigo_modalidade)

        if posicao is None:
            return None
        
        with open(self.arquivo, "r", encoding="utf-8") as f:
            f.seek(posicao)
            linha = f.readline().strip()
            dados = linha.split(';')
            return Modalidade(dados[0],dados[1],dados[2],dados[3],dados[4],dados[5])


    def listar(self):
        posicoes = self.arvore.obter_posicoes_em_ordem()
        modalidade_cadastradas = []
        with open(self.arquivo, "r", encoding="utf-8") as f:
            for pos in posicoes:
                f.seek(pos)
                linha = f.readline().strip()
                dados = linha.split(';')
                mod = Modalidade(dados[0],dados[1],dados[2],dados[3],dados[4],dados[5])
                modalidade_cadastradas.append(mod)
            return modalidade_cadastradas

    def excluir(self, codigo_modalidade):
        posicao = self.arvore.buscar(codigo_modalidade)

        if posicao is None:
            return False
        todas_modalidades = self.listar()

        with open(self.arquivo, "w", encoding="utf-8") as f:
            pass
            self.arvore = ArvoreBinaria()

        for mod in todas_modalidades:
            if mod.codigo_modalidade != codigo_modalidade:
                self.salvar(mod) 
                
        return True


    def atualizar(self, mod_modificado: Modalidade):
            if self.arvore.buscar(mod_modificado.codigo_modalidade) is None:
                return False 
            self.excluir(mod_modificado.codigo_modalidade)
            self.salvar(mod_modificado)
            
            return True

#
class GerenciadorMatricula:
    def __init__(self, caminho_arquivo="data/matricula.txt"):
        self.arquivo = caminho_arquivo
        self.arvore = ArvoreBinaria()
        self._carregar_indices() 
                                                                            
    def _carregar_indices(self):                                                
        with open(self.arquivo, "a+", encoding="utf-8") as f:
            f.seek(0) 
            posicao_atual = f.tell() 
            linha = f.readline()
            while linha:
                dados = linha.strip().split(';')
                codigo_matricula = int(dados[0])
                self.arvore.inserir_no(codigo_matricula, posicao_atual)
                posicao_atual = f.tell() 
                linha = f.readline()
    
    def salvar(self, mat: Matricula):                            
        with open(self.arquivo, "a", encoding="utf-8") as f:
            posicao = f.tell()
            linha_texto = f"{mat.codigo_matricula};{mat.codigo_aluno};{mat.codigo_modalidade};{mat.qtd_aulas}\n"
            f.write(linha_texto)
            self.arvore.inserir_no(mat.codigo_matricula, posicao)

    def buscar_codigo(self, codigo_matricula):
        posicao = self.arvore.buscar(codigo_matricula)

        if posicao is None:
            return None
        
        with open(self.arquivo, "r", encoding="utf-8") as f:
            f.seek(posicao)
            linha = f.readline().strip()
            dados = linha.split(';')
            return Matricula(dados[0],dados[1],dados[2],dados[3])


    def listar(self):
        posicoes = self.arvore.obter_posicoes_em_ordem()
        matricula_cadastradas = []
        with open(self.arquivo, "r", encoding="utf-8") as f:
            for pos in posicoes:
                f.seek(pos)
                linha = f.readline().strip()
                dados = linha.split(';')
                mat = Matricula(dados[0],dados[1],dados[2],dados[3])
                matricula_cadastradas.append(mat)
            return matricula_cadastradas

    def excluir(self, codigo_matricula):
        posicao = self.arvore.buscar(codigo_matricula)

        if posicao is None:
            return False
        todas_matriculas = self.listar()

        with open(self.arquivo, "w", encoding="utf-8") as f:
            pass
            self.arvore = ArvoreBinaria()

        for mat in todas_matriculas:
            if mat.codigo_matricula != codigo_matricula:
                self.salvar(mat) 
                
        return True


    def atualizar(self, mat_modificado: Matricula):
            if self.arvore.buscar(mat_modificado.codigo_matricula) is None:
                return False 
            self.excluir(mat_modificado.codigo_matricula)
            self.salvar(mat_modificado)
            
            return True
