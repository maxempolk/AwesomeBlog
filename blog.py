class article:
	def __init__(self, name:str, body:str, writer:str):
		self.name   = name
		self.body   = body
		self.writer = writer
	def getPost(self):
		return {"name":self.name, "body":self.body, "writer":self.writer}