

class Buffer:
	buffer_ram: list = []
	buffer_cpu: list = []
	buffer_bus: list = []
	
	def get_buffer_ram(self):
		return self.buffer_ram
	
	def get_buffer_cpu(self):
		return self.buffer_cpu
	
	def get_buffer_bus(self):
		return self.buffer_bus
