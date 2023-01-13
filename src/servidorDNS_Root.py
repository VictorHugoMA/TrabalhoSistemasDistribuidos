import socket


def criarConexao(ip,porta): #cria conexão com o cliente
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Iniciando Servidorr...")
    s.bind((ip, porta))

    return s

#"192.168.15.76", 1234

def receberDados(socket): #recebe os dados do cliente
    data, address = socket.recvfrom(1024)
    
    print(f"{address} buscando dados.")

    data = data.decode()

    return data, address
       # s.close()

def buscaIP(data):
    ip = leArquivo(data)#dns_table.get(data, "não encontrado!").encode()
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
    with open("names.txt") as names:
        for line in names:
            if dado in line:
                #se estiver, retorna o ip
                return line.split(" | ")[1]
        #se não estiver, retorna 404       
        return "404" 

def requisitarServidorBR(data):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Enviando Requisição para Servidor BR")
    print(data)
    s.sendto(data.encode(), ('192.168.15.78', 1253))
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
    socket.sendto(ip.encode(), address)


def servidorDNS():
    s = criarConexao("10.14.107.19", 1234)
    while True:
        data, address = receberDados(s)
        ip = buscaIP(data)
        enviarDados(s, ip, address)

#printa o ip do requisitarServidorBR
servidorDNS()