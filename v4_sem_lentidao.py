import socket
import tkinter.messagebox
from datetime import datetime
import tkinter as tk
from PIL import ImageTk, Image


def imprimir_etiqueta():

    # Pegando o dia e o horario que foi gerado a etiqueta
    data_var = datetime.now().strftime("%d/%m/%Y")
    now = datetime.now()
    hora_atual = now.strftime("%H:%M:%S")

    # entrando com os dados
    conteudo_qrcode = entrada.get()
    remessa = conteudo_qrcode
    print(remessa)

    if (conteudo_qrcode.isdigit() and (len(conteudo_qrcode) >= 8 )):
        #Layot da etiquta
        codigo_zpl = '^XA~TA000~JSN^LT0^MNW^MTT^PON^PMN^LH0,0^JMA^PR4,4~SD20^JUS^LRN^CI0^XZ \n' \
                     '^XA\n' \
                     '^MMT\n' \
                     '^PW799\n' \
                     '^LL0400\n' \
                     '^LS0\n' \
                     '^FT62,53^A0N,28,38^FH\^FDEWM - SAP/APOLLO  - ^FS\n' \
                     '^FT644,53^A0N,28,28^FH\\^FD' + hora_atual + '^FS\n' \
                     '^FT473,53^A0N,28,28^FH\\^FD' + data_var +'^FS\n' \
                     '^FT25,297^A0N,28,28^FH\^FDENDERE\80O :^FS\n' \
                     '^FT25,337^A0N,28,28^FH\^FDQTD CAIXA : ^FS\n' \
                     '^FT25,381^A0N,28,28^FH\^FDUSU\B5RIO : ^FS ^FT326,234^BQN,2,7\n' \
                     '^FH\^FDLA,' + conteudo_qrcode + ' ^FS\n' \
                     '^FO177,298^GB590,0,1^FS\n' \
                     '^FO177,333^GB590,0,1^FS\n' \
                     '^FO177,373^GB590,0,1^FS\n' \
                     '^FT287,247^A0N,28,28^FH\^FDREMESSA N\F8' + remessa + '^FS\n' \
                     '^PQ1,0,1,Y^XZ'

        # Endereço IP da impressora
        HOST = '192.168.152.52'
        # Porta padrão de comunicação com a impressora
        PORT = 9100

        # Conecta-se à impressora
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        # Envia o código ZPL para a impressora
        s.sendall(codigo_zpl.encode())

        # Fecha a conexão com a impressora
        s.close()

    else:
        tkinter.messagebox.showerror(title="ERRO", message="Por favor, insira uma remessa válida.")

def sair():
    janela.destroy()

import tkinter as tk
from PIL import ImageTk, Image


# Cria a janela
janela = tk.Tk()

# Define o tamanho da janela
janela.geometry("500x500")

# Nome da janela
janela.title("Imprimir etiqueta")

# carrega a imagem
imagem = Image.open('C:/Users/frederico.almeida/PycharmProjects/qrcodev6/m.png')
# redimensiona a imagem para o tamanho da janela
imagem = imagem.resize((500, 500), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)

# cria um canvas com o tamanho da janela
canvas = tk.Canvas(janela, width=500, height=500)
canvas.create_image(0, 0, anchor='nw', image=imagem)

# posiciona o canvas na janela
canvas.grid(row=0, column=0, columnspan=2, sticky='nsew')

# ajusta o tamanho da imagem para preencher toda a janela
def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized_imagem = imagem.resize((new_width, new_height), Image.ANTIALIAS)
    canvas.itemconfig(imagem_id, image=resized_imagem)
    canvas.config(width=new_width, height=new_height)

imagem_id = canvas.create_image(0, 0, anchor='nw', image=imagem)
canvas.bind('<Configure>', resize_image)

# Cria um rótulo
rotulo1 = tk.Label(janela, text="GERADOR DE QRCODE REMESSA")
rotulo1.grid(row=1, column=0, padx=5, pady=5, sticky='W')

# Cria um rótulo
rotulo2 = tk.Label(janela, text="Digite a Remessa : ")
rotulo2.grid(row=2, column=0, padx=5, pady=5, sticky='W')

# Cria um campo de entrada
entrada = tk.Entry(janela)
entrada.grid(row=2, column=1, padx=5, pady=5)

# Cria um botão que executa a função imprimir_etiqueta()
botao_imprimir = tk.Button(janela, text="Imprimir", command=imprimir_etiqueta)
botao_imprimir.grid(row=3, column=1, padx=5, pady=5, sticky='E')

# Cria um botão para sair
botao_sair = tk.Button(janela, text="Sair", command=janela.quit)
botao_sair.grid(row=3, column=0, padx=5, pady=5, sticky='W')

# Inicia o loop da janela
janela.mainloop()

# Cria um botão para sair
botao_sair = tk.Button(janela, text="Sair", command=janela.quit)
botao_sair.place(x=10, y=450)

# Inicia o loop da janela
janela.mainloop()
