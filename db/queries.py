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