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