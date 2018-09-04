class Phonebook:

	def __init__(self, dimensions=None):
		self.entries = {}
		self.dimensions = dimensions or PhysicalDimensions()

	def add(self, name, number):
		self.entries[name] = number

	def lookup(self, name):
		return self.entries[name]

	def keep_publishing(self):
		if self.dimensions.weight < 2:
			return 'stop publishing'
		elif self.dimensions.weight > 10:
			return 'publish digitally'
		else:
			return 'publish print'


class PhysicalDimensions:

	def __init__(self, weight=None):
		self.weight = weight or 0
