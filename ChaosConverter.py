"""
This is a program to help estimate currency in terms of chaos by pulling data off of currency.poe.trade
depends on BeautifulSoup4 to scrape the data off of the pages
"""

from bs4 import BeautifulSoup
import requests




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

