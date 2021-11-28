class channel(object):
	def __init__(self,limit=0):
		self.ch = []
		self.limit = limit
	def put(self,v=0):
		if self.limit:
			while len(self.ch)+1 >= self.limit:
				continue
		self.ch.append(v)
	def pop(self):
		while not self.ch:
			continue
		return self.ch.pop()
	def wait(self):
		while self.ch:
			continue
