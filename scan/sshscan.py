import socket


def conn_port(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)  # 设置超时时间
    try:
        sk.connect((host, port))
        sk.close()
        return True
    except Exception:
        sk.close()
        return False


def conn_ssh_service(host, port):
    # ssh = paramiko.SSHClient()
    # ssh.connect(host, username="root", port=host, password="pwd")  # 建立ssh连接


def ssh_scan(host):
    res = conn_port(host, 22)
    if res:
        print(" [+]" + host + "的22端口开启")
        return True
    return False
