import bs4
from bs4 import BeautifulSoup
import requests
import time
from functions.functions import *
from classes.restaurant import *
from typing import List

def getBill(item: bs4.element.Tag) -> str:
	bill_span = item.find("span", {"class": "average-bill"})
	average_bill = bill_span.get_text().replace(".", "") if bill_span != None else None
	return average_bill

def getName(item: bs4.element.Tag) -> str:
	return item.find("a", {"class": "name"}).get_text()

def getTags(item: bs4.element.Tag) -> list:
	props_wrap_div = item.find("div", {"class": "props-wrap"})
	cuisine_span = props_wrap_div.find("span", string="Кухня: ")
	cuisine_text = cuisine_span.find_parent().get_text()
	cuisine_text = cuisine_text.replace("Кухня:  ", "").replace('\xa0', ' ')
	cuisine_list = cuisine_text.split(', ')

	return cuisine_list

def getRate(item: bs4.element.Tag) -> float:
	dropdown_div = item.find("div", {"class": "dropdown"})
	span_element = dropdown_div.find("span")
	text_content = span_element.get_text()
	float_value = float(text_content)

	return float_value

def crawl(BASE_URL: str, pages: int,) -> List[Restaurant]:
	result = []
	for i in range(pages):
		response = requests.get(BASE_URL + f"?page={i+1}")
		soup = BeautifulSoup(response.text, 'html.parser')

		for item in soup.find("div", {"class": "catalog-list"}).find_all("div", {"class": "item"}):
			name = getName(item)
			tags = getTags(item)
			bill = getBill(item)
			rate = getRate(item)
			result.append(Restaurant(name, tags, bill, rate))
		
		time.sleep(1)

	return result