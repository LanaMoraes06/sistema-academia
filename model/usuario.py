class Usuario:
    def __init__(self, codigo, login, senha, perfil):
        self.codigo = codigo
        self.login = login
        self.senha = senha
        
        perfis_permitidos = ["Administrador", "Professor", "Recepcionista"]
        
        if perfil not in perfis_permitidos:
            raise ValueError("Erro: Perfil inválido.")
            
        self.perfil = perfil