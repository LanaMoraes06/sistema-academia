class Usuario:
    def __init__(self, codigo, login, senha, perfil):
        self.codigo = codigo
        self.login = login
        self.senha = senha
        
        # Define quais são os perfis aceitos pelo sistema
        perfis_permitidos = ["Administrador", "Recepcionista"]
        
        # Regra de Negócio Blindada: Impede a criação de perfis inválidos
        if perfil not in perfis_permitidos:
            raise ValueError("Erro: Perfil inválido. Escolha entre 'Administrador' ou 'Recepcionista'.")
            
        self.perfil = perfil