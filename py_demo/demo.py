import socket
from zope.interface import Interface
from zope.interface.declarations import implementer
# 定义接口 
class IHost(Interface):
	def goodmorning(self,host):
	 	"""Say good morning to host"""

@implementer(IHost) #继承接口

class Host(object):
	def goodmorning(self, name):
		"""Say good morning to guests""" 
		return "Good morning, %s!" % name

	def get_host_ip(self):
		try:
			s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			s.connect(('8.8.8.8',80))
			ip=s.getsockname()[0]
		finally:
			s.close()
		return ip
	
	def get_host_name(self):
		hostname=socket.gethostname()
		return hostname

	def get_host_ip_by_name(self):
		ip=socket.gethostbyname(self.get_host_name())
		return ip


if __name__ == '__main__':
	h = Host()
	hi = h.goodmorning('zhangsan')
	print(hi)
	print(h.get_host_ip())
	print(h.get_host_name())
	print(h.get_host_ip_by_name())
	p = Host() 
	hi = p.goodmorning('Tom') 
	print(hi)
