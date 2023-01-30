import socket


def criarConexao(ip,porta): #cria conexão com o cliente
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Iniciando Servidor...")
    s.bind((ip, porta))

    return s

def receberDados(socket): #recebe os dados do cliente
    data, address = socket.recvfrom(1024)
    
    print(f"{address} buscando dados.")

    data = data.decode()

    return data, address
       # s.close()

def buscaIP(data):
    print('Inciando busca de IP...')
    ip = leArquivo(data)
    if(ip == "404"):
        #pega a partir do segundo ponto do data
        dom = data.split(".")[3:]
        try:

            if dom[0] == "br":
                ip = requisitarServidorBR(data)
            elif dom[0] == "us":
                ip = requisitarServidorUS(data)
            return ip
        except:
            return "404"
    return ip

def leArquivo(dado):
    print("Lendo arquivo...")
    try:
        with open("names.txt") as names:
            for line in names:
                if dado in line:
                    #se estiver, retorna o ip
                    return line.split(" | ")[1]
            #se não estiver, retorna 404       
            return '404'
    except:
        return '404'

def requisitarServidorBR(data):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Enviando Requisição para Servidor BR")
    print(data)
    s.sendto(data.encode(), ('10.14.26.221', 1253))
    data = s.recvfrom(1024)
    ip = data[0].decode().strip()

    return ip

def requisitarServidorUS(data):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Enviando Requisição para Servidor US")
    s.sendto(data.encode(), ('192.168.98.76', 1235))
    data = s.recvfrom(1024)
    ip = data[0].decode().strip()

    return ip

def enviarDados(socket, ip, address):
    print("Retornando dados...")
    socket.sendto(ip.encode(), address)


def servidorDNS():
    s = criarConexao("10.14.96.48", 1234)
    print("Servidor pronto...")
    while True:
        data, address = receberDados(s)
        ip = buscaIP(data)
        enviarDados(s, ip, address)

#printa o ip do requisitarServidorBR
servidorDNS()