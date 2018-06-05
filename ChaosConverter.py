"""
This is a program to help estimate currency in terms of chaos by pulling data off of currency.poe.trade
depends on BeautifulSoup4 to scrape the data off of the pages
"""

from bs4 import BeautifulSoup
import requests



def main():

	print ("Up to date prices:")
	print ("")

	wisdomPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=17")
	wisdomC = toChaos(wisdomPrice, "wisdoms")

	portalPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=18")
	portalC = toChaos(portalPrice, "portals")

	whetstonePrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=20")
	whetstoneC = toChaos(whetstonePrice, "whetstones")

	scrapsPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=19")
	scrapsC = toChaos(scrapsPrice, "scraps")

	baublesPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=21")
	baublesC = toChaos(baublesPrice, "baubles")

	gcpPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=5")
	gcpC = toChaos(gcpPrice, "gcp")

	chiselsPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=10")
	chiselsC = toChaos(chiselsPrice, "chisels")

	transmutePrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=22")
	transmuteC = toChaos(transmutePrice, "transmutes")

	altPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=1")
	altC = toChaos(altPrice, "alts")

	annulPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=513")
	annulC = toChaos(annulPrice, "annuls")

	chancePrice =  priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=9")
	chanceC = toChaos(chancePrice, "chances")

	exaltPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=6")
	exaltC = toChaos(exaltPrice, "exalts")

	mirrorPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=9")
	mirrorC = toChaos(mirrorPrice, "mirrors")

	regalPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=14")
	regalC = toChaos(regalPrice, "regals")

	alchPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=3")
	alchC = toChaos(alchPrice, "alchs")

	chaosC = input("How many chaos do you have? ")
	print ("")

	blessedPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=12")
	blessedC = toChaos(blessedPrice, "blessed")

	augPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=23")
	augC = toChaos(augPrice, "augs")

	divinePrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=15")
	divineC = toChaos(divinePrice, "divine")

	jewelerPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=8")
	jewelerC = toChaos(jewelerPrice, "jewelers")

	fusingPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=2")
	fusingC = toChaos(fusingPrice, "fusing")

	chromePrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=7")
	chromeC = toChaos(chromePrice, "chromes")

	scourPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=11")
	scourC = toChaos(scourPrice, "scours")

	regretPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=13")
	regretC = toChaos(regretPrice, "regrets")

	vaalPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=16")
	vaalC = toChaos(vaalPrice, "vaals")

	silverPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=35")
	silverC = toChaos(silverPrice, "silver")

	acsPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=45")
	acsC = toChaos(acsPrice, "acs")

	jcsPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=46")
	jcsC = toChaos(jcsPrice, "jcs")

	mcsPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=47")
	mcsC = toChaos(mcsPrice, "mcs")

	offeringPrice = priceChecker("http://currency.poe.trade/search?league=Bestiary&online=x&want=4&have=40")
	offeringC = toChaos(offeringPrice, "offering")

	total = float(wisdomC) + float(portalC) + float(whetstoneC) + float(scrapsC) + float(baublesC) + float(gcpC) + float(chiselsC) + float(transmuteC) + float(altC) + float(annulC) + float(chanceC) + float(exaltC) + float(mirrorC) + float(regalC) + float(alchC) + float(chaosC) + float(blessedC) + float(augC) + float(divineC) + float(jewelerC) + float(fusingC) + float(chromeC) + float(scourC) + float(regretC) + float(vaalC) + float(silverC) + float(acsC) + float(jcsC) + float(mcsC) + float(offeringC)
	print("Total chaos is : %f" % total)



def toChaos(currencyPrice, currencyName):
	print("AVG %s price is : %s" % (currencyName, currencyPrice))
	currency = input("How many %s do you have? " % (currencyName))
	currencyC = float(currency)/currencyPrice
	print("You have %f chaos in %s" % (currencyC, currencyName))
	print("")
	return currencyC



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

