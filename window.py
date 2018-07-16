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



if __name__ == "__main__":
	main()
