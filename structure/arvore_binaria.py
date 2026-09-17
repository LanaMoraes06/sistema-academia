class No:
    #O init é o construtor do python
    def __init__(self, cod, pos):
        self.cod = int(cod) #tem que colocar o int pra garantir que o codigo seja inteiro
        self.pos = int(pos) 
        self.esq = None
        self.dir = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None #Raiz tem que começar vazia 

    #Método público para adicionar um novo registro    
    def inserir_no(self, cod, pos):
        cod = int(cod)
        pos = int(pos)
        #Se a árvore estiver totalmente vazia, o novo nó se torna o topo
        if self.raiz is None:
            self.raiz = No(cod, pos)
        else: #Se ja existir a raiz, vai para a função de inserir nó filho para achar seu lugar
            self.inserir_no_filho(self.raiz, cod, pos)
        
    #Função recursiva para achar o lugar correto
    def inserir_no_filho(self, pai, cod, pos):
        if cod < pai.cod: 
            if pai.esq is None: #Codigo menor é sempre na esquerda, se estiver livre, adiciona um novo nó
                pai.esq = No(cod, pos) 
            else: 
                self.inserir_no_filho(pai.esq, cod, pos) #Se estiver ocupado, a função chama ela mesma para descer mais um andar pela esquerda
        elif cod > pai.cod: 
            if pai.dir is None:
                pai.dir = No(cod, pos)
            else:
                self.inserir_no_filho(pai.dir, cod, pos)
        else:
            pai.pos = pos #Atualiza a posição no disco

    def buscar(self, cod):
        return self.buscar_cod(self.raiz, int(cod)) #Converte a busca para inteiro e aciona a função recursiva de busca
    
    #Função de busca comum
    def buscar_cod(self, raiz, cod):
        if raiz is None:
            return None
        elif raiz.cod == cod:
            return raiz.pos
        elif cod < raiz.cod:
            return self.buscar_cod(raiz.esq, cod)
        else:
            return self.buscar_cod(raiz.dir, cod)

    def deletar(self, cod):
        self.raiz = self.excluir(self.raiz, int(cod)) #A exclusão pode mudar a árvore inteira, então ela tem que atualizar a raiz
        
    def excluir(self, raiz, cod):
        if raiz is None: #Se a arvore está vazia, não tem o que excluir
            return None
        if cod < raiz.cod: #Busca do nó
            raiz.esq = self.excluir(raiz.esq, cod)
        elif cod > raiz.cod:
            raiz.dir = self.excluir(raiz.dir, cod)
        else:
            if raiz.esq is None: #Se o nó só tem filho na direita, retorna o filho da direita para ser "puxado" para cima para substituir o nó apagado
                return raiz.dir
            elif raiz.dir is None: #Se o nó só tem filho na esquerda, então ele substitui o pai
                return raiz.esq
            else: #Tem filho nos dois lados
                ex = self.minimo(raiz.dir) #Busca os sucessores
                raiz.cod = ex.cod #Substitui os dados
                raiz.pos = ex.pos
                raiz.dir = self.excluir(raiz.dir, ex.cod) #Apaga o sucessor lá de baixo
        return raiz 
        
        # Função auxiliar usada na exclusão, vai sempre para a esquerda até não dar mais
    def minimo(self, pai):
        atual = pai
        while atual.esq is not None:
            atual = atual.esq
        return atual
    
    # Função para devolver os dados em ordem
    def obter_posicoes_em_ordem(self):
        posicoes = []
        def percorrer(no):
            if no is not None:
                percorrer(no.esq) #Pega tudo o que é menor
                posicoes.append(no.pos) #Salva a posição atual do nó
                percorrer(no.dir) #Pega tudo que é maior
        percorrer(self.raiz)
        return posicoes