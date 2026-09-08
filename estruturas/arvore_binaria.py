class NoArvore:
    def __init__(self, codigo, posicao):
        self.esquerda = None
        self.direita = None
        self.codigo = codigo
        self.posicaio = posicao


def adicionar_no_arvore(raiz, codigo, posicao):
    if raiz is None:
        return NoArvore(codigo, posicao)
    if int(codigo) > raiz.codigo:
        raiz.direita = adicionar_no_arvore(raiz.direita, codigo, posicao)
    else:
        raiz.esquerda = adicionar_no_arvore(raiz.direita, codigo, posicao)
    return raiz


    