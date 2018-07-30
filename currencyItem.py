class CurrencyItem:

	name = ""
	ratio = 0.0
	owned = 0
	poetradeurl = ""

	def __init__(self, name, ratio, owned, poetradeurl):
		self.name = name
		self.ratio = ratio
		self.owned = owned
		self.poetradeurl = poetradeurl

	def getName(self):
		return self.name

	def setRatio(self, ratio):
		self.ratio = ratio

	def getPoetradeurl(self):
		return self.poetradeurl

	def getRatio(self):
		return self.ratio

	def setOwned(self, owned):
		self.owned = owned

	def getOwned(self):
		return self.owned






"""
from ChaosConverter import priceChecker

class CurrencyItem:

	name = ""
	ratio = 0.0
	owned = 0
	poetradeurl = ""

	def __init__(self, name, ratio, owned, poetradeurl):
		#name = StringVar(window)
		self.name = name
		self.ratio = ratio
		self.owned = owned
		self.poetradeurl = poetradeurl

	def getName(self):
		return self.name

	def getRatio(self):
		return self.ratio

	def setRatio(self, num):
		self.ratio = num

	def getOwned(self):
		return self.owned

	def setOwned(self, num):
		self.owned = num

	def getPoetradeurl(self):
		return self.poetradeurl

	def updateRatio(self):
		self.setRatio(priceChecker(self.poetradeurl))

"""