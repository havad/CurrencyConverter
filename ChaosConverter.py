"""
This is a program to help estimate currency in terms of chaos by pulling data off of currency.poe.trade
depends on BeautifulSoup4 to scrape the data off of the pages
"""

from bs4 import BeautifulSoup
from currencyItem import *
import requests
from tkinter import *

EXTRA_SMALL = 6			#this variable is for the number of extra small tags on any given currency.poe.trade page that lists offers

#create all of the currency objects
scrollObj = CurrencyItem("Scroll of Wisdom", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=17", "wisdom")
portalObj = CurrencyItem("Portal Scroll", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=18", "portal")
whetstoneObj = CurrencyItem("Blacksmith's Whetstone", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=20", "whetstone")
scrapObj = CurrencyItem("Armourer's Scrap", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=19", "scrap")
baubleObj = CurrencyItem("Glassblower's Bauble", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=21", "bauble")
gcpObj = CurrencyItem("Gemcutter's Prism", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=5", "gcp")
chiselObj = CurrencyItem("Cartographer's Chisel", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=10", "chisel")
transmuteObj = CurrencyItem("Orb of Transmutation", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=22", "transmute")
altObj = CurrencyItem("Orb of Alteration", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=1", "alt")
annulObj = CurrencyItem("Orb of Annulment", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=513", "annul")
chanceObj = CurrencyItem("Orb of Chance", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=9", "chance")
exaltObj = CurrencyItem("Exalted Orb", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=6", "ex")
mirrorObj = CurrencyItem("Mirror of Kalandra", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=24", "mirror")
regalObj = CurrencyItem("Regal Orb", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=14", "regal")
alchObj = CurrencyItem("Orb of Alchemy", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=3", "alch")
chaosObj = CurrencyItem("Chaos Orb", 1, 0, None, "chaos")
blessedObj = CurrencyItem("Blessed Orb", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=12", "blessed")
augObj = CurrencyItem("Orb of Augmentation", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=23", "aug")
exshardObj = CurrencyItem("Exalted Shard", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=521", "exshard")
mirrorshardObj = CurrencyItem("Mirror Shard", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=520", "mshard")
divineObj = CurrencyItem("Divine Orb", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=15", "divine")
jewellerObj = CurrencyItem("Jeweller's Orb", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=8", "jeweller")
fusingObj = CurrencyItem("Orb of Fusing", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=2", "fuse")
chromeObj = CurrencyItem("Chromatic Orb", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=7", "chrome")
scourObj = CurrencyItem("Orb of Scouring", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=11", "scour")
regretObj = CurrencyItem("Orb of Regret", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=13", "regret")
vaalObj = CurrencyItem("Vaal Orb", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=16", "vaal")
perandusObj = CurrencyItem("Perandus Coin", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=26", "perandus")
silverObj = CurrencyItem("Silver Coin", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=35", "silver")
acsObj = CurrencyItem("Apprentice Cartographer's Sextant", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=45", "acs")
jcsObj = CurrencyItem("Journeyman Cartographer's Sextant", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=46", "jcs")
mcsObj = CurrencyItem("Master Cartographer's Sextant", 0, 0, "http://currency.poe.trade/search?league=Standard&online=x&want=4&have=47", "mcs")

listOfObj = [scrollObj, portalObj, whetstoneObj, scrapObj, baubleObj, gcpObj, chiselObj, transmuteObj, altObj, annulObj, chanceObj, exaltObj,
			mirrorObj, regalObj, alchObj, chaosObj, blessedObj, augObj, exshardObj, mirrorshardObj, divineObj, jewellerObj, fusingObj, chromeObj,
			scourObj, regalObj, vaalObj, perandusObj, silverObj, acsObj, jcsObj, mcsObj]


#Refreshes the ratios for all currency objects

#scrapes the proper currency.poe.trade url for the ratio of currency -> chaos
def priceChecker(currencyURL):
	url = currencyURL

	page = requests.get(url)

	soup = BeautifulSoup(page.content, 'html.parser')
	smallTag = soup.findAll("small")
	arrayLength = len(smallTag)

	ratios = [0] * 10

	i = 0
	avg = 0
	while ((i < (arrayLength - EXTRA_SMALL)) and (i < 10)):
		myString = smallTag[i].encode("UTF-8")
		splitMyString = myString.decode("UTF-8").split(" ")
		ratios[i] = float(splitMyString[6])
		avg = avg + ratios[i]
		i = i + 2

	if(((arrayLength-EXTRA_SMALL)/2) == 0):
		avg = 0
	elif((i/2) == 0):
		avg = 0
	else:
		avg = avg/(i/2)
	return avg


class Window:

	
	def __init__(self, master):
		self.master = master
		self.master.title("CurrencyConverter")
		self.centerWindow()
		#refresh()

		scrollRatioText = StringVar(master)
		portalRatioText = StringVar(master)
		whetstoneRatioText = StringVar(master)
		scrapRatioText = StringVar(master)
		baubleRatioText = StringVar(master)
		gcpRatioText = StringVar(master)
		chiselRatioText = StringVar(master)
		transmuteRatioText = StringVar(master)
		altRatioText = StringVar(master)
		annulRatioText = StringVar(master)
		chanceRatioText = StringVar(master)
		exaltRatioText = StringVar(master)
		mirrorRatioText = StringVar(master)
		regalRatioText = StringVar(master)
		alchRatioText = StringVar(master)
		
		blessedRatioText = StringVar(master)
		augRatioText = StringVar(master)
		exshardRatioText = StringVar(master)
		mirrorshardRatioText = StringVar(master)
		divineRatioText = StringVar(master)
		jewellerRatioText = StringVar(master)
		fusingRatioText = StringVar(master)
		chromeRatioText = StringVar(master)
		scourRatioText = StringVar(master)
		regretRatioText = StringVar(master)
		vaalRatioText = StringVar(master)
		perandusRatioText = StringVar(master)
		silverRatioText = StringVar(master)
		acsRatioText = StringVar(master)
		jcsRatioText = StringVar(master)
		mcsRatioText = StringVar(master)

		ratioText = [scrollRatioText, portalRatioText, whetstoneRatioText, scrapRatioText, baubleRatioText, gcpRatioText, chiselRatioText, transmuteRatioText, altRatioText,
					annulRatioText, chanceRatioText, exaltRatioText, mirrorRatioText, regalRatioText, alchRatioText, "0", blessedRatioText, augRatioText, exshardRatioText,
					mirrorshardRatioText, divineRatioText, jewellerRatioText, fusingRatioText, chromeRatioText, scourRatioText, regretRatioText, vaalRatioText, perandusRatioText,
					silverRatioText, acsRatioText, jcsRatioText, mcsRatioText]

		scrollChaosText = StringVar(master)
		portalChaosText = StringVar(master)
		whetstoneChaosText = StringVar(master)
		scrapChaosText = StringVar(master)
		baubleChaosText = StringVar(master)
		gcpChaosText = StringVar(master)
		chiselChaosText = StringVar(master)
		transmuteChaosText = StringVar(master)
		altChaosText = StringVar(master)
		annulChaosText = StringVar(master)
		chanceChaosText = StringVar(master)
		exaltChaosText = StringVar(master)
		mirrorChaosText = StringVar(master)
		regalChaosText = StringVar(master)
		alchChaosText = StringVar(master)
		chaosChaosText = StringVar(master)
		blessedChaosText = StringVar(master)
		augChaosText = StringVar(master)
		exshardChaosText = StringVar(master)
		mirrorshardChaosText = StringVar(master)
		divineChaosText = StringVar(master)
		jewellerChaosText = StringVar(master)
		fusingChaosText = StringVar(master)
		chromeChaosText = StringVar(master)
		scourChaosText = StringVar(master)
		regretChaosText = StringVar(master)
		vaalChaosText = StringVar(master)
		perandusChaosText = StringVar(master)
		silverChaosText = StringVar(master)
		acsChaosText = StringVar(master)
		jcsChaosText = StringVar(master)
		mcsChaosText = StringVar(master)
		chaosText = [scrollChaosText, portalChaosText, whetstoneChaosText, scrapChaosText, baubleChaosText, gcpChaosText, chiselChaosText, transmuteChaosText, altChaosText, 
					annulChaosText, chanceChaosText, exaltChaosText, mirrorChaosText, regalChaosText, alchChaosText, chaosChaosText, blessedChaosText, augChaosText, 
					exshardChaosText, mirrorshardChaosText, divineChaosText, jewellerChaosText, fusingChaosText, chromeChaosText, scourChaosText, regretChaosText, vaalChaosText, 
					perandusChaosText, silverChaosText, acsChaosText, jcsChaosText, mcsChaosText]
		
		#scrollRatioText.set("0")

		titleLabel = Label(self.master, text="Currency")
		titleEntry = Label(self.master, text="You Own")
		titleRatio = Label(self.master, text="Ratio")
		titleChaos = Label(self.master, text="Currency in Chaos")
		titleLabel.grid(row=0, column=0)
		titleEntry.grid(row=0, column=1)
		titleRatio.grid(row=0, column=2)
		titleChaos.grid(row=0, column=3)

		scrollLabel = Label(self.master, text=scrollObj.getName())
		scrollEntry = Entry(self.master)
		scrollEntry.insert(0, "0")
		scrollRatio = Label(self.master, textvariable=scrollRatioText)
		scrollChaos = Label(self.master, textvariable=scrollChaosText)
		scrollLabel.grid(row=1, column=0)
		scrollEntry.grid(row=1, column=1)
		scrollRatio.grid(row=1, column=2)
		scrollChaos.grid(row=1, column=3)

		portalLabel = Label(self.master, text=portalObj.getName())
		portalEntry = Entry(self.master)
		portalEntry.insert(0, "0")
		portalRatio = Label(self.master, textvariable=portalRatioText)
		portalChaos = Label(self.master, textvariable=portalChaosText)
		portalLabel.grid(row=2, column=0)
		portalEntry.grid(row=2, column=1)
		portalRatio.grid(row=2, column=2)
		portalChaos.grid(row=2, column=3)

		whetstoneLabel = Label(self.master, text=whetstoneObj.getName())
		whetstoneEntry = Entry(self.master)
		whetstoneEntry.insert(0, "0")
		whetstoneRatio = Label(self.master, textvariable=whetstoneRatioText)
		whetstoneChaos = Label(self.master, textvariable=whetstoneChaosText)
		whetstoneLabel.grid(row=3, column=0)
		whetstoneEntry.grid(row=3, column=1)
		whetstoneRatio.grid(row=3, column=2)
		whetstoneChaos.grid(row=3, column=3)

		scrapLabel = Label(self.master, text=scrapObj.getName())
		scrapEntry = Entry(self.master)
		scrapEntry.insert(0, "0")
		scrapRatio = Label(self.master, textvariable=scrapRatioText)
		scrapChaos = Label(self.master, textvariable=scrapChaosText)
		scrapLabel.grid(row=4, column=0)
		scrapEntry.grid(row=4, column=1)
		scrapRatio.grid(row=4, column=2)
		scrapChaos.grid(row=4, column=3)

		baubleLabel = Label(self.master, text=baubleObj.getName())
		baubleEntry = Entry(self.master)
		baubleEntry.insert(0, "0")
		baubleRatio = Label(self.master, textvariable=baubleRatioText)
		baubleChaos = Label(self.master, textvariable=baubleChaosText)
		baubleLabel.grid(row=5, column=0)
		baubleEntry.grid(row=5, column=1)
		baubleRatio.grid(row=5, column=2)
		baubleChaos.grid(row=5, column=3)

		gcpLabel = Label(self.master, text=gcpObj.getName())
		gcpEntry = Entry(self.master)
		gcpEntry.insert(0, "0")
		gcpRatio = Label(self.master, textvariable=gcpRatioText)
		gcpChaos = Label(self.master, textvariable=gcpChaosText)
		gcpLabel.grid(row=6, column=0)
		gcpEntry.grid(row=6, column=1)
		gcpRatio.grid(row=6, column=2)
		gcpChaos.grid(row=6, column=3)

		chiselLabel = Label(self.master, text=chiselObj.getName())
		chiselEntry = Entry(self.master)
		chiselEntry.insert(0, "0")
		chiselRatio = Label(self.master, textvariable=chiselRatioText)
		chiselChaos = Label(self.master, textvariable=chiselChaosText)
		chiselLabel.grid(row=7, column=0)
		chiselEntry.grid(row=7, column=1)
		chiselRatio.grid(row=7, column=2)
		chiselChaos.grid(row=7, column=3)

		transmuteLabel = Label(self.master, text=transmuteObj.getName())
		transmuteEntry = Entry(self.master)
		transmuteEntry.insert(0, "0")
		transmuteRatio = Label(self.master, textvariable=transmuteRatioText)
		transmuteChaos = Label(self.master, textvariable=transmuteChaosText)
		transmuteLabel.grid(row=8, column=0)
		transmuteEntry.grid(row=8, column=1)
		transmuteRatio.grid(row=8, column=2)
		transmuteChaos.grid(row=8, column=3)

		altLabel = Label(self.master, text=altObj.getName())
		altEntry = Entry(self.master)
		altEntry.insert(0, "0")
		altRatio = Label(self.master, textvariable=altRatioText)
		altChaos = Label(self.master, textvariable=altChaosText)
		altLabel.grid(row=9, column=0)
		altEntry.grid(row=9, column=1)
		altRatio.grid(row=9, column=2)
		altChaos.grid(row=9, column=3)

		annulLabel = Label(self.master, text=annulObj.getName())
		annulEntry = Entry(self.master)
		annulEntry.insert(0, "0")
		annulRatio = Label(self.master, textvariable=annulRatioText)
		annulChaos = Label(self.master, textvariable=annulChaosText)
		annulLabel.grid(row=10, column=0)
		annulEntry.grid(row=10, column=1)
		annulRatio.grid(row=10, column=2)
		annulChaos.grid(row=10, column=3)

		chanceLabel = Label(self.master, text=chanceObj.getName())
		chanceEntry = Entry(self.master)
		chanceEntry.insert(0, "0")
		chanceRatio = Label(self.master, textvariable=chanceRatioText)
		chanceChaos = Label(self.master, textvariable=chanceChaosText)
		chanceLabel.grid(row=11, column=0)
		chanceEntry.grid(row=11, column=1)
		chanceRatio.grid(row=11, column=2)
		chanceChaos.grid(row=11, column=3)

		exaltLabel = Label(self.master, text=exaltObj.getName())
		exaltEntry = Entry(self.master)
		exaltEntry.insert(0, "0")
		exaltRatio = Label(self.master, textvariable=exaltRatioText)
		exaltChaos = Label(self.master, textvariable=exaltChaosText)
		exaltLabel.grid(row=12, column=0)
		exaltEntry.grid(row=12, column=1)
		exaltRatio.grid(row=12, column=2)
		exaltChaos.grid(row=12, column=3)
		
		mirrorLabel = Label(self.master, text=mirrorObj.getName())
		mirrorEntry = Entry(self.master)
		mirrorEntry.insert(0, "0")
		mirrorRatio = Label(self.master, textvariable=mirrorRatioText)
		mirrorChaos = Label(self.master, textvariable=mirrorChaosText)
		mirrorLabel.grid(row=13, column=0)
		mirrorEntry.grid(row=13, column=1)
		mirrorRatio.grid(row=13, column=2)
		mirrorChaos.grid(row=13, column=3)

		regalLabel = Label(self.master, text=regalObj.getName())
		regalEntry = Entry(self.master)
		regalEntry.insert(0, "0")
		regalRatio = Label(self.master, textvariable=regalRatioText)
		regalChaos = Label(self.master, textvariable=regalChaosText)
		regalLabel.grid(row=14, column=0)
		regalEntry.grid(row=14, column=1)
		regalRatio.grid(row=14, column=2)
		regalChaos.grid(row=14, column=3)

		alchLabel = Label(self.master, text=alchObj.getName())
		alchEntry = Entry(self.master)
		alchEntry.insert(0, "0")
		alchRatio = Label(self.master, textvariable=alchRatioText)
		alchChaos = Label(self.master, textvariable=alchChaosText)
		alchLabel.grid(row=15, column=0)
		alchEntry.grid(row=15, column=1)
		alchRatio.grid(row=15, column=2)
		alchChaos.grid(row=15, column=3)

		chaosLabel = Label(self.master, text=chaosObj.getName())
		chaosEntry = Entry(self.master)
		chaosEntry.insert(0, "0")
		chaosRatio = Label(self.master, text="1")
		chaosChaos = Label(self.master, textvariable=chaosChaosText)
		chaosLabel.grid(row=16, column=0)
		chaosEntry.grid(row=16, column=1)
		chaosRatio.grid(row=16, column=2)
		chaosChaos.grid(row=16, column=3)

		blessedLabel = Label(self.master, text=blessedObj.getName())
		blessedEntry = Entry(self.master)
		blessedEntry.insert(0, "0")
		blessedRatio = Label(self.master, textvariable=blessedRatioText)
		blessedChaos = Label(self.master, textvariable=blessedChaosText)
		blessedLabel.grid(row=17, column=0)
		blessedEntry.grid(row=17, column=1)
		blessedRatio.grid(row=17, column=2)
		blessedChaos.grid(row=17, column=3)

		augLabel = Label(self.master, text=augObj.getName())
		augEntry = Entry(self.master)
		augEntry.insert(0, "0")
		augRatio = Label(self.master, textvariable=augRatioText)
		augChaos = Label(self.master, textvariable=augChaosText)
		augLabel.grid(row=18, column=0)
		augEntry.grid(row=18, column=1)
		augRatio.grid(row=18, column=2)
		augChaos.grid(row=18, column=3)

		exshardLabel = Label(self.master, text=exshardObj.getName())
		exshardEntry = Entry(self.master)
		exshardEntry.insert(0, "0")
		exshardRatio = Label(self.master, textvariable=exshardRatioText)
		exshardChaos = Label(self.master, textvariable=exshardChaosText)
		exshardLabel.grid(row=19, column=0)
		exshardEntry.grid(row=19, column=1)
		exshardRatio.grid(row=19, column=2)
		exshardChaos.grid(row=19, column=3)

		mirrorshardLabel = Label(self.master, text=mirrorshardObj.getName())
		mirrorshardEntry = Entry(self.master)
		mirrorshardEntry.insert(0, "0")
		mirrorshardRatio = Label(self.master, textvariable=mirrorshardRatioText)
		mirrorshardChaos = Label(self.master, textvariable=mirrorshardChaosText)
		mirrorshardLabel.grid(row=20, column=0)
		mirrorshardEntry.grid(row=20, column=1)
		mirrorshardRatio.grid(row=20, column=2)
		mirrorshardChaos.grid(row=20, column=3)

		divineLabel = Label(self.master, text=divineObj.getName())
		divineEntry = Entry(self.master)
		divineEntry.insert(0, "0")
		divineRatio = Label(self.master, textvariable=divineRatioText)
		divineChaos = Label(self.master, textvariable=divineChaosText)
		divineLabel.grid(row=21, column=0)
		divineEntry.grid(row=21, column=1)
		divineRatio.grid(row=21, column=2)
		divineChaos.grid(row=21, column=3)

		jewellerLabel = Label(self.master, text=jewellerObj.getName())
		jewellerEntry = Entry(self.master)
		jewellerEntry.insert(0, "0")
		jewellerRatio = Label(self.master, textvariable=jewellerRatioText)
		jewellerChaos = Label(self.master, textvariable=jewellerChaosText)
		jewellerLabel.grid(row=22, column=0)
		jewellerEntry.grid(row=22, column=1)
		jewellerRatio.grid(row=22, column=2)
		jewellerChaos.grid(row=22, column=3)

		fusingLabel = Label(self.master, text=fusingObj.getName())
		fusingEntry = Entry(self.master)
		fusingEntry.insert(0, "0")
		fusingRatio = Label(self.master, textvariable=fusingRatioText)
		fusingChaos = Label(self.master, textvariable=fusingChaosText)
		fusingLabel.grid(row=23, column=0)
		fusingEntry.grid(row=23, column=1)
		fusingRatio.grid(row=23, column=2)
		fusingChaos.grid(row=23, column=3)

		chromeLabel = Label(self.master, text=chromeObj.getName())
		chromeEntry = Entry(self.master)
		chromeEntry.insert(0, "0")
		chromeRatio = Label(self.master, textvariable=chromeRatioText)
		chromeChaos = Label(self.master, textvariable=chromeChaosText)
		chromeLabel.grid(row=24, column=0)
		chromeEntry.grid(row=24, column=1)
		chromeRatio.grid(row=24, column=2)
		chromeChaos.grid(row=24, column=3)

		scourLabel = Label(self.master, text=scourObj.getName())
		scourEntry = Entry(self.master)
		scourEntry.insert(0, "0")
		scourRatio = Label(self.master, textvariable=scourRatioText)
		scourChaos = Label(self.master, textvariable=scourChaosText)
		scourLabel.grid(row=25, column=0)
		scourEntry.grid(row=25, column=1)
		scourRatio.grid(row=25, column=2)
		scourChaos.grid(row=25, column=3)

		regretLabel = Label(self.master, text=regretObj.getName())
		regretEntry = Entry(self.master)
		regretEntry.insert(0, "0")
		regretRatio = Label(self.master, textvariable=regretRatioText)
		regretChaos = Label(self.master, textvariable=regretChaosText)
		regretLabel.grid(row=26, column=0)
		regretEntry.grid(row=26, column=1)
		regretRatio.grid(row=26, column=2)
		regretChaos.grid(row=26, column=3)

		vaalLabel = Label(self.master, text=vaalObj.getName())
		vaalEntry = Entry(self.master)
		vaalEntry.insert(0, "0")
		vaalRatio = Label(self.master, textvariable=vaalRatioText)
		vaalChaos = Label(self.master, textvariable=vaalChaosText)
		vaalLabel.grid(row=27, column=0)
		vaalEntry.grid(row=27, column=1)
		vaalRatio.grid(row=27, column=2)
		vaalChaos.grid(row=27, column=3)

		perandusLabel = Label(self.master, text=perandusObj.getName())
		perandusEntry = Entry(self.master)
		perandusEntry.insert(0, "0")
		perandusRatio = Label(self.master, textvariable=perandusRatioText)
		perandusChaos = Label(self.master, textvariable=perandusChaosText)
		perandusLabel.grid(row=28, column=0)
		perandusEntry.grid(row=28, column=1)
		perandusRatio.grid(row=28, column=2)
		perandusChaos.grid(row=28, column=3)

		silverLabel = Label(self.master, text=silverObj.getName())
		silverEntry = Entry(self.master)
		silverEntry.insert(0, "0")
		silverRatio = Label(self.master, textvariable=silverRatioText)
		silverChaos = Label(self.master, textvariable=silverChaosText)
		silverLabel.grid(row=29, column=0)
		silverEntry.grid(row=29, column=1)
		silverRatio.grid(row=29, column=2)
		silverChaos.grid(row=29, column=3)

		acsLabel = Label(self.master, text=acsObj.getName())
		acsEntry = Entry(self.master)
		acsEntry.insert(0, "0")
		acsRatio = Label(self.master, textvariable=acsRatioText)
		acsChaos = Label(self.master, textvariable=acsChaosText)
		acsLabel.grid(row=30, column=0)
		acsEntry.grid(row=30, column=1)
		acsRatio.grid(row=30, column=2)
		acsChaos.grid(row=30, column=3)

		jcsLabel = Label(self.master, text=jcsObj.getName())
		jcsEntry = Entry(self.master)
		jcsEntry.insert(0, "0")
		jcsRatio = Label(self.master, textvariable=jcsRatioText)
		jcsChaos = Label(self.master, textvariable=jcsChaosText)
		jcsLabel.grid(row=31, column=0)
		jcsEntry.grid(row=31, column=1)
		jcsRatio.grid(row=31, column=2)
		jcsChaos.grid(row=31, column=3)

		mcsLabel = Label(self.master, text=mcsObj.getName())
		mcsEntry = Entry(self.master)
		mcsEntry.insert(0, "0")
		mcsRatio = Label(self.master, textvariable=mcsRatioText)
		mcsChaos = Label(self.master, textvariable=mcsChaosText)
		mcsLabel.grid(row=32, column=0)
		mcsEntry.grid(row=32, column=1)
		mcsRatio.grid(row=32, column=2)
		mcsChaos.grid(row=32, column=3)

		entries = [scrollEntry, portalEntry, whetstoneEntry, scrapEntry, baubleEntry, gcpEntry, chiselEntry, transmuteEntry, altEntry, annulEntry, chanceEntry, exaltEntry,
					mirrorEntry, regalEntry, alchEntry, chaosEntry, blessedEntry, augEntry, exshardEntry, mirrorshardEntry, divineEntry, jewellerEntry, fusingEntry, 
					chromeEntry, scourEntry, regretEntry, vaalEntry, perandusEntry, silverEntry, acsEntry, jcsEntry, mcsEntry]

		refreshButton = Button(self.master, text="Refresh Ratios", command=lambda: self.refresh(ratioText))
		refreshButton.grid(row=33, column=0)

		cncText = StringVar(master)
		cncLabel = Label(self.master, textvariable=cncText)
		cncLabel.grid(row=33, column=3)

		calcButton = Button(self.master, text="Calculate", command=lambda: self.calc(chaosText, entries, cncText))
		calcButton.grid(row=33, column=1)
		totalLabel = Label(self.master, text="Total Chaos:")
		totalLabel.grid(row=33, column=2)
		


	def centerWindow(self):
		w = 575
		h = 725

		sw = self.master.winfo_screenwidth()
		sh = self.master.winfo_screenheight()

		x = (sw - w) / 2
		y = (sh - h) / 2

		self.master.geometry("%dx%d+%d+%d" % (w,h,x,y))

	def calc(self, chaos, e, c):
		count = 0
		cnc = 0
		for item in chaos:
			if (listOfObj[count].getRatio() == 0):
				item.set("0.0")
			elif(listOfObj[count].getName() == "Chaos Orb"):
				item.set("%.2f" % float(e[count].get()))
				cnc = cnc + float(e[count].get())
			else:
				item.set("%.2f" % float(float(e[count].get())/listOfObj[count].getRatio()))
				cnc = cnc + (float(e[count].get())/listOfObj[count].getRatio())
			count += 1
		c.set("%.2f" % cnc)



	def refresh(self, mylist):
		print("Refreshing, please wait...")

		for item in listOfObj:
			if(item.getName() != "Chaos Orb"):
				item.setRatio(priceChecker(item.getPoetradeurl()))
		print("All ratios refreshed!\n")
		#var.set(scrollObj.getRatio())
		count = 0
		for item in mylist:
			if(item != "0"):
				item.set("%.2f" % listOfObj[count].getRatio())
			count += 1

		
root = Tk()
app = Window(root)
root.mainloop()


"""
#writes the data from all currency objects to the text files
def saveData(ratio, inventory):
	ratioFile = open(ratio, "w")
	inventoryFile = open(inventory, "w")
	for item in listOfObj:
		ratioFile.write(str(item.getRatio()) + "\n")
		inventoryFile.write(str(item.getOwned()) + "\n")
	ratioFile.close()
	inventoryFile.close()
"""

"""
#loads data from ratios.txt and inventory.txt to all currency objects
def loadFile(ratio, inventory):
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
		for item in listOfObj:
			item.setRatio(0.0)
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
		for item in listOfObj:
			item.setOwned(0)
"""

#shows how much currency in chaos the user has based on the current ratios and owned amounts
#displays chaos for each currency and then a total at the end
def showChaos():
	count = 0
	for item in listOfObj:
		if(item.getRatio() == 0):
			inChaos = 0
		else:
			inChaos = item.getOwned()/item.getRatio()
		print(item.getName() + ": " + str(inChaos) + " chaos")
		count = count + inChaos
	print("Total Chaos: " + str(count) + "\n")




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




"""
if __name__ == "__main__":
	main()
"""