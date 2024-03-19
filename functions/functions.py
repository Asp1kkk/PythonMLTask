import bs4

def getAverageBill(item: bs4.element.Tag) -> str:
	bill_span = item.find("span", {"class": "average-bill"})
	average_bill = bill_span.get_text().replace(".", "") if bill_span != None else None
	return average_bill

def getName(item: bs4.element.Tag) -> str:
	return item.find("a", {"class": "name"}).get_text()