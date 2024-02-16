  
import tkinter as tk
from tkinter import messagebox
import socket
import threading
import pickle

class Cliente:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.porta = 7777
        self.sock.connect((self.host, self.porta))

    def enviar_mensagem(self, mensagem):
        self.sock.send(pickle.dumps(mensagem))

    def receber_mensagem(self):
        return pickle.loads(self.sock.recv(2048))

class InterfaceJogo:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Memória - Cliente")
        self.root.geometry("400x200")
        self.cliente = Cliente()

        self.frame_jogo = tk.Frame(self.root)
        self.frame_jogo.pack()

        self.jogo = None
        self.tabuleiro = None
        self.botao_cartas = None

        self.receber_tabuleiro()

    def receber_tabuleiro(self):
        tabuleiro = self.cliente.receber_mensagem()
        if tabuleiro:
            self.jogo = tabuleiro
            self.atualizar_tabuleiro()

    def atualizar_tabuleiro(self):
        if self.tabuleiro:
            self.tabuleiro.destroy()

        self.tabuleiro = tk.Frame(self.frame_jogo)
        self.tabuleiro.pack()

        self.botao_cartas = []

        for i in range(self.jogo.tamanho_tabuleiro):
            for j in range(self.jogo.tamanho_tabuleiro):
                valor = self.jogo.tabuleiro[i][j]
                btn_carta = tk.Button(self.tabuleiro, text=str(valor), width=4, height=2,
                                      command=lambda i=i, j=j: self.fazer_jogada(i, j))
                btn_carta.grid(row=i, column=j)
                self.botao_cartas.append(btn_carta)

    def fazer_jogada(self, linha, coluna):
        self.cliente.enviar_mensagem(("Jogada:", linha, coluna))
        resposta = self.cliente.receber_mensagem()
        messagebox.showinfo("Resposta", resposta)
        self.receber_tabuleiro()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceJogo(root)
    root.mainloop()
