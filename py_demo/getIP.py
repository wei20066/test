import socket

def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip


if __name__ == '__main__':
    print(get_host_ip())
    #获取计算机名称
    hostname=socket.gethostname()
    print(hostname)
    #获取本机IP
    ip=socket.gethostbyname(hostname)
    print(ip)