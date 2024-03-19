import bs4

def getAverageBill(item: bs4.element.Tag) -> str:
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
