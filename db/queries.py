class Queries:
    CREATE_REVIEW_TABLE = """
        CREATE TABLE IF NOT EXISTS review (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone INTEGER,
            date TEXT,
            rate TEXT,
            clean INTEGER,
            comment TEXT
        )
    """

    CREATE_CATEGORIES_TABLE = """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        """

    CREATE_DISHES_TABLE = """
            CREATE TABLE IF NOT EXISTS dishes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price INTEGER,
                picture TEXT,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """

    DROP_CATEGORIES_TABLE = "DROP TABLE IF EXISTS categories"
    DROP_DISHES_TABLE = "DROP TABLE IF EXISTS dishes"

    POPULATE_CATEGORIES = """
    INSERT INTO categories (name) VALUES ('пиццы'), ('горячие блюда'), ('гарниры'), ('напитки') 
    """

    POPULATE_DISHES = """
    INSERT INTO dishes (name, price, picture, category_id) VALUES ('Куринная пицца', '465', 'pics/Medium.png', '1'),
    ('Китайский суп', '380', 'pics/soup.png', '2'),
    ('Картошка фри', '180', 'pics/fry.png', '3'),
    ('Лимонад', '120', 'pics/juice.png', '4')
    """