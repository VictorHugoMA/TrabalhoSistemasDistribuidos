import socket

dns_table = {"www.google.com":"192.165.1.1",
"www.youtube.com":"192.165.1.2",
"www.python.org":"192.165.1.3",
"www.aurcc.ac.in":"192.165.1.4",
"www.amazon.in":"192.165.1.5",
"www.gmail.com":"192.165.1.6"}

def criarConexao(): #cria conexão com o cliente
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Iniciando Servidorr...")
    s.bind(("192.168.15.76", 1234))

    return s


def receberDados(): #recebe os dados do cliente
    while True:

        data, address = s.recvfrom(1024)
       
        print(f"{address} buscando dados.")

        data = data.decode()

        ip = dns_table.get(data, "não encontrado!").encode() 
        send = s.sendto(ip, address)

    s.close()