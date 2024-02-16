import threading
import socket
import tkinter as tk
import random
import sys
sys.path.append('/home/yasmin/jogodamemoria')
import extracaoimg
clientes = []

def tratamento(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048).decode()
            if mensagem.startswith("Jogada:"):
                coordenadas = mensagem.split(":")[1].split(",")
                linha1, coluna1 = map(int, coordenadas[:2])
                linha2, coluna2 = map(int, coordenadas[2:])
                resposta = jogo.fazer_jogada(linha1, coluna1, linha2, coluna2)
                cliente.send(resposta.encode())
        except:
            removerCliente(cliente)
            break

def broadcast(mensagem, cliente):
    for x in clientes:
        if x != cliente:
            try:
                x.send(mensagem)
            except:
                removerCliente(x)

def removerCliente(cliente):
    clientes.remove(cliente)

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind(('localhost', 7777))
        servidor.listen()
    except:
        return print('O servidor não pode ser iniciado')

    while True:
        cliente, _ = servidor.accept()
        clientes.append(cliente)
        thread = threading.Thread(target=tratamento, args=[cliente])
        thread.start()
        
        diretorio_salvar = 'cerrado'
        url = 'https://www.todamateria.com.br/animais-do-cerrado/' 
        thread_scraping = threading.Thread(target=extracaoimg.extrair_imagens, args=(url, diretorio_salvar))
        thread_scraping.start()
        
        
        
main()