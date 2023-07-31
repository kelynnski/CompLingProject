from db.repository import *
import mysql.connector


class MySQLRepository(Repository):

    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # to run on local this should be localhost
            'port': '32000',  # to run on git this should be '32000'
            'database': 'words'
        }
        self.connection = mysql.connector.connect(**config)
        print("Database connected.")
        self.cursor = self.connection.cursor()
        print("Cursor established")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


    def mapper(self, entry):
        return entry


    def load_germanword(self):
        sql = 'SELECT * FROM german_words'
        self.cursor.execute(sql)

        # Get all the rows
        fetched_rows = list(self.cursor)
        print("Fetched rows:", fetched_rows)

        # Create a list to hold the entries
        entries = []

        # Convert each row into a dictionary
        for row in fetched_rows:
            entry = {
                'id': row[0],
                'word': row[1],
                'lang': row[2],
                'pos': row[3],
                'english_translation': row[4],
                'ex_sentence': row[5],
                'synonyms': row[6],
                'number': row[7],
                'gender': row[8],
                'tense': row[9],
                'person': row[10]
            }
            entries.append(entry)

        print("Processed entries:", entries)
        return entries

