import socket

def criarConexao(ip,porta): #cria conexão com o cliente
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Iniciando Servidorr...")
    s.bind((ip, porta))

    return s

def receberDados(socket): #recebe os dados do cliente
        data, address = socket.recvfrom(1024)
       
        print(f"{address} buscando dados.")

        data = data.decode()

        return data, address

def buscaIP(data):
    ip = leArquivo(data)#dns_table.get(data, "não encontrado!").encode()
    if(ip == 404):
        return 404

    return ip

def leArquivo(dado):
    with open("namesbr.txt") as names:
        for line in names:
            if dado in line:
                #se estiver, retorna o ip
                return line.split(" | ")[1]
            #se não estiver, retorna 404       
        return 404

def enviarDados(socket, ip, address):
    socket.sendto(ip, address)

def sevidorDNS():
    s = criarConexao("192.168.15.15", 1235)
    while True:
        data, address = receberDados(s)
        ip = buscaIP(data)
        enviarDados(s, ip, address)
