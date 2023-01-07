import socket

dns_table = {"www.google.com":"192.165.1.1",
"www.youtube.com":"192.165.1.2",
"www.python.org":"192.165.1.3",
"www.aurcc.ac.in":"192.165.1.4",
"www.amazon.in":"192.165.1.5",
"www.gmail.com":"192.165.1.6"}

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


       # s.close()

def buscaIP(data):
    ip = leArquivo(data)#dns_table.get(data, "não encontrado!").encode()
    if(ip == 404):
        ip = requisitarServidorRaiz(data)

    return ip

def leArquivo(dado):
    arq = open("dns.txt", "r")
    linhas = arq.readlines()
    for linha in linhas:
        linha = linha.split()
        dns_table[linha[0]] = linha[1]
    arq.close()

def requisitarServidorRaiz(data):
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto(data.encode(), ('192.168.98.76', 1234))
    ip, address = s.recvfrom(1024)

    return ip

def enviarDados(socket, ip, address):
    socket.sendto(ip, address)


def sevidorDNS():
    s = criarConexao("192.168.15.15", 1234)
    while True:
        data, address = receberDados(s)
        ip = buscaIP(data)
        enviarDados(s, ip, address)