import socket
from datetime import datetime
import tkinter as tk

def imprimir_etiqueta():

    # Pegando o dia e o horario que foi gerado a etiqueta
    data_var = datetime.now().strftime("%d/%m/%Y")
    now = datetime.now()
    hora_atual = now.strftime("%H:%M:%S")

    # entrando com os dados
    conteudo_qrcode = entrada.get()
    remessa = conteudo_qrcode
    print(remessa)

    if conteudo_qrcode.isdigit():
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

    else :
        print('Invalido')
        print('POR FAVOR, INSIRA UMA REMESSA VÁLIDA  :')

# Cria a janela
janela = tk.Tk()

# Define o tamanho da janela
janela.geometry("300x200")

#Nome da janela
janela.title("Imprimir etiqueta")

# Cria um rótulo
rotulo = tk.Label(janela, text="Remessa :")

# Define a posição do rótulo na janela
rotulo.pack()


# Cria um campo de entrada
entrada = tk.Entry(janela)
entrada.pack()

# Cria um botão que executa a função imprimir_etiqueta()
botao = tk.Button(janela, text="Imprimir", command=imprimir_etiqueta)
botao.pack()

# Inicia o loop da janela
janela.mainloop()
# This is a sample Python script.
