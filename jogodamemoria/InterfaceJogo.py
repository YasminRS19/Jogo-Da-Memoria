import tkinter as tk
from tkinter import messagebox

class InterfaceJogo:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Memória")
        self.root.geometry("400x200")
        
        self.frame_selecao = tk.Frame(self.root)
        self.frame_selecao.pack()

        self.lbl_instrucao = tk.Label(self.frame_selecao, text="Escolha uma opção:")
        self.lbl_instrucao.pack()

        self.btn_servidor = tk.Button(self.frame_selecao, text="Servidor", command=self.abrir_servidor)
        self.btn_servidor.pack(pady=5)

        self.btn_cliente = tk.Button(self.frame_selecao, text="Cliente", command=self.abrir_cliente)
        self.btn_cliente.pack(pady=5)

    def abrir_servidor(self):
        self.frame_selecao.destroy()
        self.frame_jogo = tk.Frame(self.root)
        self.frame_jogo.pack()

        self.lbl_tabuleiro = tk.Label(self.frame_jogo, text="Tabuleiro do jogo")
        self.lbl_tabuleiro.pack()

        # Adicionar a validação

    def abrir_cliente(self):
        self.frame_selecao.destroy()
        self.frame_jogo = tk.Frame(self.root)
        self.frame_jogo.pack()

        self.lbl_tabuleiro = tk.Label(self.frame_jogo, text="Tabuleiro do jogo")
        self.lbl_tabuleiro.pack()

        # Adicionar a validação

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceJogo(root)
    root.mainloop()