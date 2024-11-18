class TabelaHashBasica:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = {}
        for i in range(self.tamanho):
            self.tabela[i] = []

    def funcaoHash(self, chave):
        return len(chave) % self.tamanho

    def adicionar(self, chave, valor):
        posicao = self.funcaoHash(chave)
        self.tabela[posicao].append(valor)

    def buscar(self, chave):
        posicao = self.funcaoHash(chave)
        return self.tabela[posicao]

    def mostrarTabela(self):
        for i in range(self.tamanho):
            print(f"Posição {i}: {self.tabela[i]}")

# Exemplo de uso:
minhaTabela = TabelaHashBasica(5)
minhaTabela.adicionar("dog", 10)
minhaTabela.adicionar("cat", 20)
minhaTabela.adicionar("fish", 30)
minhaTabela.mostrarTabela()
