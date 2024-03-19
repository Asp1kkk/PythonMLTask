from functions.functions import crawl
import sqlite3

if __name__ == "__main__":
	url = "https://www.restoran.ru/msk/catalog/restaurants/kitchen/russian/"
	createQuery = """
	CREATE TABLE "restaurants" (
		"id"	INTEGER NOT NULL UNIQUE,
		"name"	INTEGER,
		"rating" NUMERIC(2,1),
		"bill"	TEXT,
		"tags" TEXT,
		PRIMARY KEY("id" AUTOINCREMENT)
	);
	"""

	insertQuery = """
	INSERT INTO restaurants (name, rating, bill, tags) VALUES (?, ?, ?, ?)
	"""

	restaurants = crawl(url, 18)
	
	con = sqlite3.connect("./database/restaurants.db")
	cur = con.cursor()

	cur.execute(createQuery)

	for res in restaurants:
		cur.execute(insertQuery, (res.name, res.rate, res.average, ", ".join(res.tags)))