import requests
from bs4 import BeautifulSoup
import os

def criar_diretorio(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

def extrair_imagens(url, diretorio_salvar):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        imagens = soup.find_all('img')
        
        criar_diretorio(diretorio_salvar)
        
        
        for img in imagens:
            img_url = img.get('src')
            if img_url:
                img_nome = img_url.split('/')[-1]
                if img_nome not in ['7graus-logo.svg', 'desktop-logo.png', 'juliana-diana_72.jpg']:
                    img_path = os.path.join(diretorio_salvar, img_nome)
                    with open(img_path, 'wb') as f:
                        f.write(requests.get(img_url).content)
                    print(f'Imagem salva: {img_path}')
                else:
                    print(f'Imagem {img_nome} ignorada.')
    else:
        print('Falha ao obter a página.')
    
    enumerar_arquivos(diretorio_salvar)

def enumerar_arquivos(diretorio_salvar):
    if os.path.exists(diretorio_salvar):
        lista_arquivos = os.listdir(diretorio_salvar)
        for idx, arquivo in enumerate(lista_arquivos):
            novo_nome = f"imagem_{idx}.{arquivo.split('.')[-1]}"
            caminho_antigo = os.path.join(diretorio_salvar, arquivo)
            caminho_novo = os.path.join(diretorio_salvar, novo_nome)
            os.rename(caminho_antigo, caminho_novo)
            print(f"Arquivo renomeado: {caminho_antigo} -> {caminho_novo}")
    else:
        print("Diretório não encontrado.")


url = 'https://www.todamateria.com.br/animais-do-cerrado/'

diretorio_salvar = 'cerrado'

extrair_imagens(url, diretorio_salvar)
