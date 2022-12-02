
import config

class Response:
	def __init__(self, path):

		self.file_buff = ''
		if path==config.get_401:
			self.status=401
		elif path==config.get_404:
			self.status=404
		else:
			self.status = 200		
   	
		# get file name and file type
		self.loc_of_file = path		# duong dan toi file					
		file_info = path.split('/')[-1].split('.')		
		self.file_type = file_info[-1]		# file type


		# co gang mo file da cung cap duong dan o tren, neu false tra ve status code 404 va 404.html
		try:
			if(self.file_buff == ''):
				self.buffer = open(path[1:],"rb")
		except:
			self.status = 404
			self.buffer = open(config.get_404[1:],"rb")

		# khoi tao header
		header = ''	
		# Status Line
		if (self.status==401):
			header += "HTTP/1.1 401 Unauthorized\r\n" 
		elif (self.status==404): 
			header+="HTTP/1.1 404 NOT FOUND\r\n" 
		else:
			header+="HTTP/1.1 200 OK\r\n"
		# Entity Headers
		if self.file_type in ["html","htm"]:
			header += 'Content-Type: text/html\r\n'
		elif self.file_type == "txt":
			header += 'Content-Type: text/plain\r\n'
		elif self.file_type == "css":
			header += 'Content-Type: text/css\r\n'
		elif self.file_type in ["jpg","jpeg"]:
			header += 'Content-Type: image/jpeg\r\n'
		elif self.file_type =="png":
			header += 'Content-Type: image/png\r\n'
		elif self.file_type =="gif":
			header += 'Content-Type: image/gif\r\n'
		else:
			header += 'Content-Type: application/octet-stream\r\n'
		# General Headers
		header += 'Connection: close\r\n'
		self.header = header

	def makeResponse(self):
		# truong hop file duoc gui theo cach thong thuong
			
		if(self.file_buff != ''):
			content = self.file_buff.encode('utf-8')
		else:
			content = self.buffer.read()

		self.header += "Content-Length: %d\r\n\r\n"%len(content)
		print(f'-------------------\n [HEADER RESPONSE] \n{self.header}')
		header = self.header.encode('utf-8') + content + "\r\n".encode('utf-8')
		print(f"-------------------\n [SEND RESPONSE] \n Transfer {self.loc_of_file} with normal mode")
		return header
		