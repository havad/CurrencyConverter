"""
This is a program to help estimate currency in terms of chaos by pulling data off of currency.poe.trade
depends on BeautifulSoup4 to scrape the data off of the pages
"""

from bs4 import BeautifulSoup
from currencyItem import *
import requests

scrollObj = CurrencyItem("Scroll of Wisdom", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=17")
portalObj = CurrencyItem("Portal Scroll", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=18")
whetstoneObj = CurrencyItem("Blacksmith's Whetstone", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=20")
scrapObj = CurrencyItem("Armourer's Scrap", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=19")
baubleObj = CurrencyItem("Glassblower's Bauble", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=21")
gcpObj = CurrencyItem("Gemcutter's Prism", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=5")
chiselObj = CurrencyItem("Cartographer's Chisel", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=10")
transmuteObj = CurrencyItem("Orb of Transmutation", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=22")
altObj = CurrencyItem("Orb of Alteration", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=1")
annulObj = CurrencyItem("Orb of Annulment", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=513")
chanceObj = CurrencyItem("Orb of Chance", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=9")
exaltObj = CurrencyItem("Exalted Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=6")
#mirrorObj = CurrencyItem("Mirror of Kalandra", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=24")
regalObj = CurrencyItem("Regal Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=14")
alchObj = CurrencyItem("Orb of Alchemy", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=3")
chaosObj = CurrencyItem("Chaos Orb", 1, 0, None)
blessedObj = CurrencyItem("Blessed Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=12")
augObj = CurrencyItem("Orb of Augmentation", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=23")
exshardObj = CurrencyItem("Exalted Shard", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=521")
#mirrorshardObj = CurrencyItem("Mirror Shard", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=520")
divineObj = CurrencyItem("Divine Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=15")
jewellerObj = CurrencyItem("Jeweller's Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=8")
fusingObj = CurrencyItem("Orb of Fusing", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=2")
chromeObj = CurrencyItem("Chromatic Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=7")
scourObj = CurrencyItem("Orb of Scouring", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=11")
regretObj = CurrencyItem("Orb of Regret", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=13")
vaalObj = CurrencyItem("Vaal Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=16")
#perandusObj = CurrencyItem("Perandus Coin", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=26")
silverObj = CurrencyItem("Silver Coin", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=35")
acsObj = CurrencyItem("Apprentice Cartographer's Sextant", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=45")
jcsObj = CurrencyItem("Journeyman Cartographer's Sextant", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=46")
mcsObj = CurrencyItem("Master Cartographer's Sextant", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=47")

listOfObj = [scrollObj, portalObj, whetstoneObj, scrapObj, baubleObj, gcpObj, chiselObj, transmuteObj, altObj, annulObj, chanceObj, exaltObj,
			regalObj, alchObj, chaosObj, blessedObj, augObj, exshardObj, divineObj, jewellerObj, fusingObj, chromeObj,
			scourObj, regalObj, vaalObj, silverObj, acsObj, jcsObj, mcsObj]


def main():
	print("Program Running")

	while(True):
		print("What would you like to do?\n")
		print("(R)efresh ratios")
		print("Edit (O)ne")
		print("Edit (A)ll")
		print("(Q)uit\n")
		selection = input().lower()
		if(selection == "q"):
			exit(0)
		elif(selection == "r"):
			refresh()
		elif(selection == "o"):
			editOne()
		elif(selection == "a"):
			editAll()



def toChaos(currencyPrice, currencyName):
	print("AVG %s price is : %s" % (currencyName, currencyPrice))
	currency = input("How many %s do you have? " % (currencyName))
	currencyC = float(currency)/currencyPrice
	print("You have %f chaos in %s" % (currencyC, currencyName))
	print("")
	return currencyC

#Refreshes the ratios for all currency objects
def refresh():
	print("Refreshing, please wait...")

	for item in listOfObj:
		if(item.getName() != "Chaos Orb"):
			item.setRatio(priceChecker(item.getPoetradeurl()))
			#print(item.getName() + " " + str(item.getRatio()))  #works as far as i know. left in for debugging
	print("All ratios refreshed!\n")

def editOne():
	print("Which currency would you like to edit?\n")
	req = input().lower()
	for item in listOfObj:
		if(req == item.getName().lower()):
			print("Input new amount owned")
			newAmount = input()
			item.setOwned(int(newAmount))
			#print(item.getOwned())		#works, left in for debugging

def editAll():
	print("Editing All")
	for item in listOfObj:
		print(item.getName() + ": ")
		amount = input()
		item.setOwned(int(amount))

#scrapes the proper currency.poe.trade url for the ratio of currency -> chaos
def priceChecker(currencyURL):
	url = currencyURL

	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')
	smallTag = soup.findAll("small")

	ratios = [0] * 10

	i = 0
	avg = 0
	while (i < 10):
		myString = smallTag[i].encode("UTF-8")
		splitMyString = myString.decode("UTF-8").split(" ")
		ratios[i] = float(splitMyString[6])
		avg = avg + ratios[i]
		i = i + 2

	avg = avg/5
	return avg


if __name__ == "__main__":
	main()