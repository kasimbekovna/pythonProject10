class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contacts TEXT,
            date TEXT,
            quality_food INTEGER,
            clean INTEGER,
            EXTRA_COMMENTS TEXT
        )
    """

    INSERT_COMMENTS = """
    INSERT INTO survey (name, contacts, date, quality_food,clean,EXTRA_COMMENTS) VALUES(?,?,?,?,?,?)
    """