class Usuario:
    def __init__(self, codigo_usuario, login, senha, perfil):
        self.codigo_usuario = codigo_usuario
        self.login = login
        self.senha = senha

    @property
    def login(self):
        return self._login  
    
    @login.setter
    def login(self, novo_login):
        if not novo_login or not str(novo_login).strip():
            raise ValueError("Erro: O login não pode ser nulo ou vazio!")
        self._login = str(novo_login).strip()

    @property
    def senha(self):
        return self._senha
        
    @senha.setter
    def senha(self, nova_senha):
        if not nova_senha or not str(nova_senha).strip():
            raise ValueError("Erro: A senha não pode ser nula ou vazia!")
        self._senha = str(nova_senha).strip()

    perfis_permitidos = ["Administrador", "Recepcionista"]
    if perfil not in perfis_permitidos:
            raise ValueError(f"Erro: Perfil inválido. Escolha entre 'Administrador' ou 'Recepcionista'.")
            
    self.perfil = perfil