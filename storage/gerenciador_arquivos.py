import os
import json
from model.professor import Professor
from model.matricula import Matricula
from model.aluno import Aluno
from model.modalidade import Modalidade
from model.usuario import Usuario

class GerenciadorAlunos:
    def __init__(self, caminho_arquivo="data/alunos.json"):
        self.arquivo = caminho_arquivo
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _ler_dados(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _salvar_dados(self, dados):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def save(self, aluno: Aluno):
        dados = self._ler_dados()
        aluno_dict = {
            "codigo_aluno": int(aluno.codigo_aluno),
            "nome": aluno.nome,
            "data_nascimento": str(aluno.data_nascimento),
            "peso": float(aluno.peso),
            "altura": float(aluno.altura)
        }
        dados.append(aluno_dict)
        self._salvar_dados(dados)

    def findById(self, codigo_aluno):
        dados = self._ler_dados()
        for d in dados:
            if d["codigo_aluno"] == int(codigo_aluno):
                return Aluno(d["codigo_aluno"], d["nome"], d["data_nascimento"], d["peso"], d["altura"])
        return None

    def findAll(self):
        dados = self._ler_dados()
        return [Aluno(d["codigo_aluno"], d["nome"], d["data_nascimento"], d["peso"], d["altura"]) for d in dados]

    def delete(self, codigo_aluno):
        dados = self._ler_dados()
        dados_filtrados = [d for d in dados if d["codigo_aluno"] != int(codigo_aluno)]
        
        if len(dados) == len(dados_filtrados):
            return False
            
        self._salvar_dados(dados_filtrados)
        return True

    def update(self, aluno_modificado: Aluno):
        dados = self._ler_dados()
        atualizou = False
        
        for i, d in enumerate(dados):
            if d["codigo_aluno"] == int(aluno_modificado.codigo_aluno):
                dados[i] = {
                    "codigo_aluno": int(aluno_modificado.codigo_aluno),
                    "nome": aluno_modificado.nome,
                    "data_nascimento": str(aluno_modificado.data_nascimento),
                    "peso": float(aluno_modificado.peso),
                    "altura": float(aluno_modificado.altura)
                }
                atualizou = True
                break
                
        if atualizou:
            self._salvar_dados(dados)
        return atualizou


class GerenciadorProfessor:
    def __init__(self, caminho_arquivo="data/professor.json"):
        self.arquivo = caminho_arquivo
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _ler_dados(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _salvar_dados(self, dados):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def save(self, prof: Professor):
        dados = self._ler_dados()
        prof_dict = {
            "codigo_prof": int(prof.codigo_prof),
            "nome": prof.nome,
            "endereco": prof.endereco,
            "telefone": prof.telefone
        }
        dados.append(prof_dict)
        self._salvar_dados(dados)

    def findById(self, codigo_prof):
        dados = self._ler_dados()
        for d in dados:
            if d["codigo_prof"] == int(codigo_prof):
                return Professor(d["codigo_prof"], d["nome"], d["endereco"], d["telefone"])
        return None

    def findAll(self):
        dados = self._ler_dados()
        return [Professor(d["codigo_prof"], d["nome"], d["endereco"], d["telefone"]) for d in dados]

    def delete(self, codigo_prof):
        dados = self._ler_dados()
        dados_filtrados = [d for d in dados if d["codigo_prof"] != int(codigo_prof)]
        if len(dados) == len(dados_filtrados):
            return False
        self._salvar_dados(dados_filtrados)
        return True

    def update(self, prof_modificado: Professor):
        dados = self._ler_dados()
        atualizou = False
        for i, d in enumerate(dados):
            if d["codigo_prof"] == int(prof_modificado.codigo_prof):
                dados[i] = {
                    "codigo_prof": int(prof_modificado.codigo_prof),
                    "nome": prof_modificado.nome,
                    "endereco": prof_modificado.endereco,
                    "telefone": prof_modificado.telefone
                }
                atualizou = True
                break
        if atualizou:
            self._salvar_dados(dados)
        return atualizou


class GerenciadorModalidade:
    def __init__(self, caminho_arquivo="data/modalidade.json"):
        self.arquivo = caminho_arquivo
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _ler_dados(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _salvar_dados(self, dados):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def save(self, mod: Modalidade):
        dados = self._ler_dados()
        mod_dict = {
            "codigo_modalidade": int(mod.codigo_modalidade),
            "descricao": mod.descricao,
            "codigo_prof": int(mod.codigo_prof),
            "valor_aula": float(mod.valor_aula),
            "limite_alunos": int(mod.limite_alunos),
            "total_alunos": int(mod.total_alunos)
        }
        dados.append(mod_dict)
        self._salvar_dados(dados)

    def findById(self, codigo_modalidade):
        dados = self._ler_dados()
        for d in dados:
            if d["codigo_modalidade"] == int(codigo_modalidade):
                return Modalidade(d["codigo_modalidade"], d["descricao"], d["codigo_prof"], d["valor_aula"], d["limite_alunos"], d["total_alunos"])
        return None

    def findAll(self):
        dados = self._ler_dados()
        return [Modalidade(d["codigo_modalidade"], d["descricao"], d["codigo_prof"], d["valor_aula"], d["limite_alunos"], d["total_alunos"]) for d in dados]

    def delete(self, codigo_modalidade):
        dados = self._ler_dados()
        dados_filtrados = [d for d in dados if d["codigo_modalidade"] != int(codigo_modalidade)]
        if len(dados) == len(dados_filtrados):
            return False
        self._salvar_dados(dados_filtrados)
        return True

    def update(self, mod_modificado: Modalidade):
        dados = self._ler_dados()
        atualizou = False
        for i, d in enumerate(dados):
            if d["codigo_modalidade"] == int(mod_modificado.codigo_modalidade):
                dados[i] = {
                    "codigo_modalidade": int(mod_modificado.codigo_modalidade),
                    "descricao": mod_modificado.descricao,
                    "codigo_prof": int(mod_modificado.codigo_prof),
                    "valor_aula": float(mod_modificado.valor_aula),
                    "limite_alunos": int(mod_modificado.limite_alunos),
                    "total_alunos": int(mod_modificado.total_alunos)
                }
                atualizou = True
                break
        if atualizou:
            self._salvar_dados(dados)
        return atualizou


class GerenciadorMatricula:
    def __init__(self, caminho_arquivo="data/matricula.json"):
        self.arquivo = caminho_arquivo
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _ler_dados(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _salvar_dados(self, dados):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def save(self, mat: Matricula):
        dados = self._ler_dados()
        mat_dict = {
            "codigo_matricula": int(mat.codigo_matricula),
            "codigo_aluno": int(mat.codigo_aluno),
            "codigo_modalidade": int(mat.codigo_modalidade),
            "qtd_aulas": int(mat.qtd_aulas)
        }
        dados.append(mat_dict)
        self._salvar_dados(dados)

    def findById(self, codigo_matricula):
        dados = self._ler_dados()
        for d in dados:
            if d["codigo_matricula"] == int(codigo_matricula):
                return Matricula(d["codigo_matricula"], d["codigo_aluno"], d["codigo_modalidade"], d["qtd_aulas"])
        return None

    def findAll(self):
        dados = self._ler_dados()
        return [Matricula(d["codigo_matricula"], d["codigo_aluno"], d["codigo_modalidade"], d["qtd_aulas"]) for d in dados]

    def delete(self, codigo_matricula):
        dados = self._ler_dados()
        dados_filtrados = [d for d in dados if d["codigo_matricula"] != int(codigo_matricula)]
        if len(dados) == len(dados_filtrados):
            return False
        self._salvar_dados(dados_filtrados)
        return True

    def update(self, mat_modificado: Matricula):
        dados = self._ler_dados()
        atualizou = False
        for i, d in enumerate(dados):
            if d["codigo_matricula"] == int(mat_modificado.codigo_matricula):
                dados[i] = {
                    "codigo_matricula": int(mat_modificado.codigo_matricula),
                    "codigo_aluno": int(mat_modificado.codigo_aluno),
                    "codigo_modalidade": int(mat_modificado.codigo_modalidade),
                    "qtd_aulas": int(mat_modificado.qtd_aulas)
                }
                atualizou = True
                break
        if atualizou:
            self._salvar_dados(dados)
        return atualizou


class GerenciadorUsuarios:
    def __init__(self, caminho_arquivo="data/usuarios.json"):
        self.arquivo = caminho_arquivo
        
        # Cria um admin padrão se o ficheiro não existir
        if not os.path.exists(self.arquivo):
            admin_padrao = [{
                "codigo": 1,
                "login": "admin",
                "senha": "123",
                "perfil": "Administrador"
            }]
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump(admin_padrao, f, indent=4)

    def findByLogin(self, login_buscado):
        if not os.path.exists(self.arquivo):
            return None

        with open(self.arquivo, "r", encoding="utf-8") as f:
            try:
                usuarios = json.load(f)
            except json.JSONDecodeError:
                return None
                
        for u in usuarios:
            if u.get("login") == login_buscado:
                return Usuario(u["codigo"], u["login"], u["senha"], u["perfil"])
                
        return None