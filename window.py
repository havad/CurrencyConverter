from tkinter import *
from ChaosConverter import *
from currencyItem import *
from functools import partial
import numpy

def main():

	mainWindow = Tk()
	mainWindow.title("ChaosConverter")

	
	wisdomObj = CurrencyItem("Wisdom Scroll", priceChecker("http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=17"), 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=17")
	portalObj = CurrencyItem("Portal Scroll", priceChecker("http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=18"), 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=18")
	whetstoneObj = CurrencyItem("Whetstone", priceChecker("http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=20"), 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=20")
	scrapObj = CurrencyItem("Scraps", priceChecker("http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=19"), 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=19")
	baubleObj = CurrencyItem("Baubles", priceChecker("http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=21"), 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=21")
	gcpObj = CurrencyItem("GCP", priceChecker("http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=5"), 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=5")
	chiselObj = CurrencyItem("Chisels", priceChecker("http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=10"), 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=10")



	ListofObj = [wisdomObj, portalObj, whetstoneObj, scrapObj, baubleObj, gcpObj, chiselObj]

	gridArray = numpy.zeros(shape=(256,4))
	gridArray[0] = [Label(mainWindow, text="Currency").grid(row = 0), Label(mainWindow, text="You Own").grid(row =0, column =1), Label(mainWindow, text="Ratio").grid(row = 0, column = 2), Label(mainWindow, text="Item in Chaos").grid(row = 0, column = 3)]
	
	count = 1
	for item in ListofObj:
		gridArray[count] = [Label(mainWindow, text=item.getName()).grid(row = count), Entry(mainWindow).grid(row = count, column = 1), Label(mainWindow, text=item.getRatio()).grid(row = count, column = 2), Label(mainWindow, text=(item.getOwned()/item.getRatio())).grid(row = count, column = 3)]
		count += count

	mainWindow.mainloop()




	"""
	portalObj = CurrencyItem("Portal Scroll", priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=18"), 0, "http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=18")
	whetstoneObj = CurrencyItem("Whetstone", priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=20"), 0, "http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=20")



	ListOfObj = [wisdomObj, portalObj, whetstoneObj]


	mainWindow = Tk()
	mainWindow.title("ChaosConverter")


	Label(mainWindow, text="Currency").grid(row = 0)
	Label(mainWindow, text="You Own").grid(row = 0, column = 1)
	Label(mainWindow, text="Ratio").grid(row = 0, column = 2)
	Label(mainWindow, text="Item in Chaos").grid(row = 0, column = 3)

	i = 0
	while(i < len(ListOfObj)):
		setupRow(mainWindow, ListOfObj[i], i+1)
		i = i + 1

	submit = Button(mainWindow, text = "Convert", command = partial(convert, mainWindow, len(ListOfObj))).grid(row = len(ListOfObj) + 1)
	"""
	"""
	Label(mainWindow, text=wisdomObj.getName()).grid(row = 1)
	wisdomEntry = Entry(mainWindow).grid(row = 1, column = 1)
	Label(mainWindow, text=wisdomObj.getRatio()).grid(row = 1, column = 2)
	Label(mainWindow, text = wisdomObj.getOwned() / wisdomObj.getRatio()).grid(row = 1, column = 3)
	"""

#	mainWindow.mainloop()
"""
#totally not functional
#FIX THIS
#want to update amount in chaos when the user hits convert
#def convert(window, length):
	#this is some good shit that i can use but it needs to be modified
	"""
#	for label in window.grid_slaves():
#		if int(label.grid_info()["row"]) == 1 and int(label.grid_info()["column"]) == 2:
#			label.grid_forget()
"""
	
"""
#	i = 1
#	for label in window.grid_slaves():
#		if int(label.grid_info()["row"]) == i and int(label.grid_info()["column"]) == 2:
#			label.grid_forget()
#			Label(window, text="hello").grid(row = i, column = 2)
#		i = i + 1
"""

"""
#	i = 1
#	while(i <= length):
#		Label(window, text="hello").grid(row = i, column = 2)
#		i = i + 1
	#print("testing")
"""
#attempts to set up a row with name, a text box, ratio and converted number

def setupRow(window, obj, objRow):
	Label(window, text=obj.getName()).grid(row = objRow, column = 0)
	objEntry = Entry(window).grid(row = objRow, column = 1)
	Label(window, text=obj.getRatio()).grid(row = objRow, column = 2)
	Label(window, text = obj.getOwned() / obj.getRatio()).grid(row = objRow, column = 3)
"""



if __name__ == "__main__":
	main()



"""This stuff might be useful when im instantiating objects"""
"""
wisdom = CurrencyItem("Scroll of Wisdom", priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=17"), 0, "http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=17")
print(wisdom.getPoetradeurl())
print(wisdom.getName())
print(wisdom.getRatio())
wisdom.setOwned(5)
print(wisdom.getOwned())
wisdom.updateRatio()
print(wisdom.getRatio())
"""



"""This stuff might be useful when i want to set up the window"""
"""
mainWindow = Tk()
mainWindow.title("ChaosConverter")

Label(mainWindow, text="Scrolls of Wisdom").grid(row = 0)
wisdomEntry = Entry(mainWindow)
wisdomEntry.grid(row = 0, column = 1)
wisdomRatio = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=17")
Label(mainWindow, text=wisdomRatio).grid(row = 0, column = 2)

mainWindow.mainloop()
"""