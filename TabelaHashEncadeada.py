class No:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.proximo = None

class TabelaHashEncadeada:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def calcularIndice(self, chave):
        return sum(ord(c) for c in chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.calcularIndice(chave)
        novoNo = No(chave, valor)
        if not self.tabela[indice]:
            self.tabela[indice] = novoNo
        else:
            atual = self.tabela[indice]
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novoNo

    def procurar(self, chave):
        indice = self.calcularIndice(chave)
        atual = self.tabela[indice]
        while atual:
            if atual.chave == chave:
                return atual.valor
            atual = atual.proximo
        return None

    def exibir(self):
        for i in range(self.tamanho):
            elementos = []
            atual = self.tabela[i]
            while atual:
                elementos.append((atual.chave, atual.valor))
                atual = atual.proximo
            print(f"Índice {i}: {elementos}")

# Exemplo de uso:
tabelaEncadeada = TabelaHashEncadeada(7)
tabelaEncadeada.inserir("banana", 3)
tabelaEncadeada.inserir("apple", 5)
tabelaEncadeada.inserir("grape", 8)
tabelaEncadeada.exibir()
