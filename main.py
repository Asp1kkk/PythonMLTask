from functions.functions import crawl
from database.queries import createQuery, insertQuery
import sqlite3

if __name__ == "__main__":
	url = "https://www.restoran.ru/msk/catalog/restaurants/kitchen/russian/"
	restaurants = crawl(url, 18)
	
	con = sqlite3.connect("./database/restaurants.db")
	cur = con.cursor()

	cur.execute(createQuery)

	for res in restaurants:
		cur.execute(insertQuery, (res.name, res.rate, res.average, ", ".join(res.tags)))