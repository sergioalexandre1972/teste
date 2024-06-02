from socket import socket

s = socket()

server = '127.0.0.1'
port = 8793

s.connect((server, port))

nome_escola = '-'

while nome_escola != '':
    
    nome_escola = input('Digite o nome da escola: ')
    
    if nome_escola == '':
        break
    
    msg_envio = nome_escola + ':'
    
    lista_notas = []
    for i in range(5):
        lista_notas.append(input(f'Digite a nota {i+1} da escola: '))
        if i != 4:
            msg_envio += lista_notas[-1] + ';'
        else:
            msg_envio += lista_notas[-1]
    

    meusbytes = str.encode(msg_envio, "UTF-8") # faz o encode dos dados para enviar ao servidor.
    s.send(meusbytes) # envia os dados para o servidor.
    
    data = s.recv(4096)  # Recebe os dados do servidor.
    resposta = data.decode()  # decodifica os dados vindos do servidor.
    
    nome_escola = resposta.split(':')[0]
    notas = resposta.split(':')[1]
    soma_notas = float(resposta.split(':')[2])
    lista_notas_str = notas.split(';')
    
    lista_notas =[]
    for nota in lista_notas_str:
        lista_notas.append(float(nota))
    
    print( f'O servidor respondeu: {nome_escola}\t{lista_notas[0]:.1f}\t{lista_notas[1]:.1f}\t{lista_notas[2]:.1f}\t{soma_notas:.1f}' )

s.close()
