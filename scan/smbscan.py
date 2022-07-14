import socket


class smbScan:
    def conn_port(self, host, port):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(2)  # 设置超时时间
        try:
            sk.connect((host, port))
            sk.close()
            return True
        except Exception:
            sk.close()
            return False

    def smb_scan(self, host, port):
        res = self.conn_port(host, port)
        if res:
            print(" [+] " + host + "在" + str(port) + "端口上的SMB端口开启")
            return True
        return False


smbscan = smbScan()
smbscan.smb_scan("10.133.73.212", 445)
