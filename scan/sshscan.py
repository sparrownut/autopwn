import socket


def conn_port(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(2)  # 设置超时时间
    try:
        sk.connect((host, port))
        recv = sk.recv(1024)
        sk.close()
        if b"SSH" in recv:
            return True
        else:
            return False
    except Exception:
        sk.close()
        return False


def ssh_scan(host,port):
    res = conn_port(host, port)
    if res:
        print(" [+] " + host + "在"+str(port)+"端口上的SSH服务开启")
        return True
    return False


ssh_scan("10.112.78.66",22)
