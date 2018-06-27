from ChaosConverter import *
from tkinter import *
#from window import *

class CurrencyItem:

	window = ""
	name = ""
	ratio = 0.0
	owned = 0
	poetradeurl = ""

	def __init__(self, window, myname, ratio, owned, poetradeurl):
		name = StringVar(window)
		self.name.set(myname)
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