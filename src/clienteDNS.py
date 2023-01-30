import socket
import time

hostname = socket.gethostname() 

ipaddr = "10.14.107.19"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.settimeout(5) #20 segundos

addr = (ipaddr, 1237) 

c = "S"
while c.upper() == "S":
    req_domain= input("Nome do dominio:")
    send = s.sendto(req_domain.encode(), addr)
    try:

        data, address = s.recvfrom(1024)
        reply_ip= data.decode().strip() 
        print(f"IP para o dominio {req_domain}:{reply_ip}")
    except socket.timeout:
        print("Servidor sem resposta.\nDesconectando da aplicação...")
        c = (input(""))

        break
    c = (input("Continuar? (s/n)"))


""" 
n = 0
start= time.time()

req_domain= "www.google.com"
while time.time() - start < 10:

    send = s.sendto(req_domain.encode(), addr) 
    data, address = s.recvfrom(1024)
    reply_ip= data.decode().strip() 
    print(f"IP para o dominio {req_domain}:{reply_ip}")
    n += 1
    print(n)

"""