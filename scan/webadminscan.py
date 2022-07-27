from scan.portscan import portscan
from utils.utils import urlToHost


class webadminscan:
    def webAdminDirScan(self, url):
        host = urlToHost(url)
        if portscan(host, 80):
            print(" [+] " + host + "端口80开启")
        else:
            print(" [-] " + host + "端口80未开启")
            return False