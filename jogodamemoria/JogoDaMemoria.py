import random

class JogoDaMemoria:
    def __init__(self, tamanho_tabuleiro):
        self.tamanho_tabuleiro = tamanho_tabuleiro
        self.tabuleiro = []
        self.pares = []
        self.jogadas = 0
        self.criar_tabuleiro()

    def criar_tabuleiro(self):
        numeros = list(range(1, (self.tamanho_tabuleiro * self.tamanho_tabuleiro) // 2 + 1))
        self.pares = numeros * 2
        random.shuffle(self.pares)

        for _ in range(self.tamanho_tabuleiro):
            linha = []
            for _ in range(self.tamanho_tabuleiro):
                linha.append(self.pares.pop())
            self.tabuleiro.append(linha)

    def fazer_jogada(self, linha1, coluna1, linha2, coluna2):
        if (linha1 == linha2 and coluna1 == coluna2) or \
           linha1 < 0 or coluna1 < 0 or linha2 < 0 or coluna2 < 0 or \
           linha1 >= self.tamanho_tabuleiro or coluna1 >= self.tamanho_tabuleiro or \
           linha2 >= self.tamanho_tabuleiro or coluna2 >= self.tamanho_tabuleiro:
            return "Jogada inválida. Tente novamente."

        valor1 = self.tabuleiro[linha1][coluna1]
        valor2 = self.tabuleiro[linha2][coluna2]

        if valor1 == valor2:
            self.tabuleiro[linha1][coluna1] = "X"
            self.tabuleiro[linha2][coluna2] = "X"
            self.jogadas += 1
            if self.verificar_vitoria():
                return "Parabéns! Você venceu em {} jogadas.".format(self.jogadas)
            return "Par encontrado!"
        else:
            return "Os valores não coincidem. Tente novamente."

    def verificar_vitoria(self):
        for linha in self.tabuleiro:
            for valor in linha:
                if valor != "X":
                    return False
        return True
