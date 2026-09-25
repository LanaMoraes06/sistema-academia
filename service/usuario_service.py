from model.usuario import Usuario

class UsuarioService:
    def __init__(self, gerenciador_usuarios):
        self.gerenciador_usuarios = gerenciador_usuarios

    def autenticar_usuario(self, login, senha):
        usuario = self.gerenciador_usuarios.findByLogin(login)
        if usuario is None or usuario.senha != senha:
            raise ValueError("Erro: Login ou senha inválidos")
        return usuario