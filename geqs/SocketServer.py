import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
	
	def handle(self):
		self.data = self.request.recv(1024).strip()
		print "{} wrote:".format(self.client_address[0])
		print self.data
		self.request.sendall(self.data.upper())
		
if _name_ == "_main_":
	HOST, POST = "localhost", 9999
	server = SocketServer.ThreadingTCPServer((HOST, POST), MyTCPHandler)
	server.serve_forever()
	

