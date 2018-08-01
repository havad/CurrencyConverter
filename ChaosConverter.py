"""
This is a program to help estimate currency in terms of chaos by pulling data off of currency.poe.trade
depends on BeautifulSoup4 to scrape the data off of the pages
"""

from bs4 import BeautifulSoup
from currencyItem import *
import requests

EXTRA_SMALL = 6
ratio = "ratios.txt"
inventory = "inventory.txt"

#any commented out objects below often have less than 5 entries. when a check for this is implemented, uncomment and put them in listOfObj

scrollObj = CurrencyItem("Scroll of Wisdom", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=17", "wisdom")
portalObj = CurrencyItem("Portal Scroll", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=18", "portal")
whetstoneObj = CurrencyItem("Blacksmith's Whetstone", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=20", "whetstone")
scrapObj = CurrencyItem("Armourer's Scrap", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=19", "scrap")
baubleObj = CurrencyItem("Glassblower's Bauble", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=21", "bauble")
gcpObj = CurrencyItem("Gemcutter's Prism", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=5", "gcp")
chiselObj = CurrencyItem("Cartographer's Chisel", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=10", "chisel")
transmuteObj = CurrencyItem("Orb of Transmutation", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=22", "transmute")
altObj = CurrencyItem("Orb of Alteration", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=1", "alt")
annulObj = CurrencyItem("Orb of Annulment", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=513", "annul")
chanceObj = CurrencyItem("Orb of Chance", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=9", "chance")
exaltObj = CurrencyItem("Exalted Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=6", "ex")
mirrorObj = CurrencyItem("Mirror of Kalandra", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=24", "mirror")
regalObj = CurrencyItem("Regal Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=14", "regal")
alchObj = CurrencyItem("Orb of Alchemy", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=3", "alch")
chaosObj = CurrencyItem("Chaos Orb", 1, 0, None, "chaos")
blessedObj = CurrencyItem("Blessed Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=12", "blessed")
augObj = CurrencyItem("Orb of Augmentation", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=23", "aug")
exshardObj = CurrencyItem("Exalted Shard", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=521", "exshard")
mirrorshardObj = CurrencyItem("Mirror Shard", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=520", "mshard")
divineObj = CurrencyItem("Divine Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=15", "divine")
jewellerObj = CurrencyItem("Jeweller's Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=8", "jeweller")
fusingObj = CurrencyItem("Orb of Fusing", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=2", "fuse")
chromeObj = CurrencyItem("Chromatic Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=7", "chrome")
scourObj = CurrencyItem("Orb of Scouring", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=11", "scour")
regretObj = CurrencyItem("Orb of Regret", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=13", "regret")
vaalObj = CurrencyItem("Vaal Orb", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=16", "vaal")
perandusObj = CurrencyItem("Perandus Coin", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=26", "perandus")
silverObj = CurrencyItem("Silver Coin", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=35", "silver")
acsObj = CurrencyItem("Apprentice Cartographer's Sextant", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=45", "acs")
jcsObj = CurrencyItem("Journeyman Cartographer's Sextant", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=46", "jcs")
mcsObj = CurrencyItem("Master Cartographer's Sextant", 0, 0, "http://currency.poe.trade/search?league=Incursion&online=x&want=4&have=47", "mcs")

listOfObj = [scrollObj, portalObj, whetstoneObj, scrapObj, baubleObj, gcpObj, chiselObj, transmuteObj, altObj, annulObj, chanceObj, exaltObj,
			mirrorObj, regalObj, alchObj, chaosObj, blessedObj, augObj, exshardObj, mirrorshardObj, divineObj, jewellerObj, fusingObj, chromeObj,
			scourObj, regalObj, vaalObj, perandusObj, silverObj, acsObj, jcsObj, mcsObj]


def main():
	print("Program Running")

	loadFile()

	while(True):
		print("What would you like to do?\n")
		print("(R)efresh ratios")
		print("Edit (O)ne")
		print("Edit (A)ll")
		print("(C)urrency in Chaos")
		print("(Q)uit\n")
		selection = input().lower()
		if(selection == "q"):
			saveData()
			exit(0)
		elif(selection == "r"):
			refresh()
		elif(selection == "o"):
			editOne()
		elif(selection == "a"):
			editAll()
		elif(selection == "c"):
			showChaos()
	

def saveData():
	ratioFile = open(ratio, "w")
	inventoryFile = open(inventory, "w")
	for item in listOfObj:
		ratioFile.write(str(item.getRatio()) + "\n")
		inventoryFile.write(str(item.getOwned()) + "\n")
	ratioFile.close()
	inventoryFile.close()

#loads data from ratios.txt and inventory.txt to all currency objects
def loadFile():
	try:
		ratioFile = open(ratio, "r+")
		lines = ratioFile.readlines()
		i = 0
		for item in listOfObj:
			item.setRatio(float(lines[i]))
			i += 1
		ratioFile.close()
	except:
		print(ratio + " not found, creating it now...")
		ratioFile = open(ratio, "w+")
		ratioFile.close()
	try:
		inventoryFile = open(inventory, "r+")
		lines = inventoryFile.readlines()
		i = 0
		for item in listOfObj:
			item.setOwned(int(lines[i]))
			i += 1
		inventoryFile.close()
	except:
		print(inventory + " not found, creating it now...")
		inventoryFile = open(inventory, "w+")
		inventoryFile.close()

#shows how much currency in chaos the user has based on the current ratios and owned amounts
#displays chaos for each currency and then a total at the end
def showChaos():
	count = 0
	for item in listOfObj:
		"""
		if(item.getOwned() == 0):
			inChaos = 0
		else:
			inChaos = item.getRatio()/item.getOwned()
		"""
		if(item.getRatio() == 0):
			inChaos = 0
		else:
			inChaos = item.getOwned()/item.getRatio()
		print(item.getName() + ": " + str(inChaos) + " chaos")
		count = count + inChaos
	print("Total Chaos: " + str(count) + "\n")

#don't think this function is relevant anymore
"""
def toChaos(currencyPrice, currencyName):
	print("AVG %s price is : %s" % (currencyName, currencyPrice))
	currency = input("How many %s do you have? " % (currencyName))
	currencyC = float(currency)/currencyPrice
	print("You have %f chaos in %s" % (currencyC, currencyName))
	print("")
	return currencyC
"""

#Refreshes the ratios for all currency objects
def refresh():
	print("Refreshing, please wait...")

	for item in listOfObj:
		if(item.getName() != "Chaos Orb"):
			item.setRatio(priceChecker(item.getPoetradeurl()))
			#print(item.getName() + " " + str(item.getRatio()))  #works as far as i know. left in for debugging
	print("All ratios refreshed!\n")

#lets the user choose one currency inventory to edit
def editOne():
	print("Which currency would you like to edit?\n")
	req = input().lower()
	found = False
	for item in listOfObj:
		if((req == item.getName().lower()) or (req == item.getCode().lower())):
			found = True
			print("Input new amount owned")
			while(True):
				try:
					newAmount = int(input())
				except:
					print("Not a number. Please enter a new value.")
				else:
					item.setOwned(int(newAmount))
					break
			#print(item.getOwned())		#works, left in for debugging
		if(found == True):
			break

#lets the user edit every currency inventory
def editAll():
	print("Editing All")
	for item in listOfObj:
		print(item.getName() + ": ")
		while(True):
			try:
				amount = int(input())
			except:
				print("Not a number. Please enter a new value")
			else:
				item.setOwned(int(amount))
				break

#scrapes the proper currency.poe.trade url for the ratio of currency -> chaos
def priceChecker(currencyURL):
	url = currencyURL

	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')
	smallTag = soup.findAll("small")
	arrayLength = len(smallTag)
	#print(str(arrayLength))
	#print(str(arrayLength - 6))
	#for thing in smallTag:
		#print(thing)

	ratios = [0] * 10

	i = 0
	avg = 0
	while ((i < (arrayLength - EXTRA_SMALL)) and (i < 10)):
		myString = smallTag[i].encode("UTF-8")
		splitMyString = myString.decode("UTF-8").split(" ")
		ratios[i] = float(splitMyString[6])
		avg = avg + ratios[i]
		i = i + 2
		#print("i is: " + str(i))
		#print(str(ratios[i]))

	#sometimes there are no listings, arrayLength-EXTRA_SMALL will be 0 when this happens, i will never be zero after the loop so i've left the code like this, can probably be changed
	#print(str((arrayLength-EXTRA_SMALL)/2))		#left in for debugging
	if(((arrayLength-EXTRA_SMALL)/2) == 0):
		avg = 0
	else:
		avg = avg/(i/2)
	#print("avg is: " + str(avg))
	return avg


if __name__ == "__main__":
	main()