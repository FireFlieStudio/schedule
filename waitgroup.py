class waitgroup(object):
	def __init__(self,limit=0):
		self.Tasks = 0
		self.Limit = limit
	def add(self,task=1):
		if self.Limit:
			while self.Tasks >= self.Limit:
				continue
		self.Tasks+= task
	def done(self):
		if self.Tasks:
			self.Tasks-=1
	def wait(self):
		while self.Tasks:
			continue
