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


    def load_germanword(self, word_to_fetch):
        sql = 'SELECT * FROM german_words WHERE word = %s'
        self.cursor.execute(sql, (word_to_fetch,))
        row = self.cursor.fetchone()

        if row:
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
            word = self.mapper(entry)
            relevant_items = ['pos', 'english_translation', 'ex_sentence', 'synonyms', 'number', 'gender', 'tense', 'person']
            required_info = {key: word[key] for key in relevant_items if key in word}
            return required_info
        return None

    def translate_english_word(self, word_to_fetch):
        sql = 'SELECT * FROM german_words WHERE english_translation = %s'
        self.cursor.execute(sql, (word_to_fetch,))
        row = self.cursor.fetchone()

        if row:
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
            word = self.mapper(entry)
            relevant_items = ['word', 'pos', 'ex_sentence', 'synonyms', 'number', 'gender', 'tense', 'person']
            required_info = {key: word[key] for key in relevant_items if key in word}
            rename_word = 'german_translation'
            required_info[rename_word] = required_info.pop('word')
            return required_info
        return None