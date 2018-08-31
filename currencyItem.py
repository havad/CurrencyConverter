class CurrencyItem:

	name = ""
	ratio = 0.0
	owned = 0
	poetradeurl = ""
	code = ""

	def __init__(self, name, ratio, owned, poetradeurl, code):
		self.name = name
		self.ratio = ratio
		self.owned = owned
		self.poetradeurl = poetradeurl
		self.code = code

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

	def getCode(self):
		return self.code

	def setURL(self, url):
		self.poetradeurl = url