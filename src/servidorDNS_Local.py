import socket
import time

def criarConexao(ip, port): #cria conexão com o cliente
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Iniciando Servidorr...")
    s.bind((ip, port))

    return s


def receberDados(socket): #recebe os dados do cliente
    data, address = socket.recvfrom(1024)
    print(f"{address} buscando dados.")
    data = data.decode()

    return data, address

def buscaIP(data):
    print("Iniciando busca de IP...")
    ip = leArquivo(data)#dns_table.get(data, "não encontrado!").encode()
    if(ip == '404'):
        ip = requisitarServidorRaiz(data)

    return ip

def leArquivo(dado):
    print("Lendo arquivo...")
    try:
        with open("cache.txt") as names:
            for line in names:
                if dado in line:
                    #se estiver, retorna o ip
                    return line.split(" | ")[1]
            #se não estiver, retorna 404       
            return '404'
    except:
        return '404'


def requisitarServidorRaiz(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('10.14.96.48', 1234) 
    print('Enviando requisição para o servidor raiz...')
    s.sendto(data.encode(), addr)
    data = s.recvfrom(1024)

    ip = data[0].decode().strip()
    
    return ip

def enviarDados(socket, ip, address):
    print("Retornando dados...")
    socket.sendto(ip.encode(), address)


def servidorDNS():
    s = criarConexao("10.14.107.19", 1237)
    while True:
        data, address = receberDados(s)
        ip = buscaIP(data)
        enviarDados(s, ip, address)

servidorDNS()