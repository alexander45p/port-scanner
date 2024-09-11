import socket

ip = input("enter the ip to scan: ")

for puerto in range(1,65535):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip,puerto))

    if result == 0:
        print("open port" +  str(puerto))
        sock.close()
    else:
        print("close port" + str(puerto))

