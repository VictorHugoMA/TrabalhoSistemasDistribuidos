import socket
import time

hostname = socket.gethostname() 

ipaddr = "10.14.107.19"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = (ipaddr, 1237) 

c = "S"
while c.upper() == "S":
    req_domain= input("Nome do dominio:")
    start = time.time()
    try:
        send = s.sendto(req_domain.encode(), addr) 
        print("Enviando requisição...")
    except:
        print("Erro ao enviar dados")
        break
    data, address = s.recvfrom(1024)

    reply_ip= data.decode().strip()
    print("------------------------------------")
    print("tempo de resposta:", time.time() - start, " seg")
    print(f"IP para o dominio {req_domain}:{reply_ip}")
    print("------------------------------------")
    c = (input("Continuar? (s/n)"))

n = 0
""" start= time.time()

req_domain= "www.yahoo.com.br"
while time.time() - start < 10:

    send = s.sendto(req_domain.encode(), addr) 
    data, address = s.recvfrom(1024)
    reply_ip= data.decode().strip() 
    print(f"IP para o dominio {req_domain}:{reply_ip}")
    n += 1
    print(n)

 """