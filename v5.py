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
janela.geometry("400x100")

# Nome da janela
janela.title("GERADOR QRCODE")

# Cria um frame para centralizar os elementos
frame = tk.Frame(janela)
frame.pack(fill=tk.BOTH, expand=True)

# Cria um rótulo
rotulo1 = tk.Label(frame, text="GERADOR DE QRCODE REMESSA")
rotulo1.pack(pady=5)

# Cria um rótulo
rotulo2 = tk.Label(frame, text="Digite a Remessa : ")
rotulo2.pack(side=tk.LEFT, padx=5, pady=5)

# Cria um campo de entrada
entrada = tk.Entry(frame)
entrada.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

# Cria um botão para sair
botao_sair = tk.Button(frame, text="Sair", command=janela.quit, activebackground='red')
botao_sair.pack(side=tk.RIGHT, padx=5, pady=5)

# Cria um botão que executa a função imprimir_etiqueta()
botao_imprimir = tk.Button(frame, text="Imprimir", command=imprimir_etiqueta, activebackground='blue')
botao_imprimir.pack(side=tk.RIGHT, padx=5, pady=5)

# Inicia o loop da janela
janela.mainloop()
