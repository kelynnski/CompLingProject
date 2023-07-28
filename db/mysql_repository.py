from db.repository import *
import mysql.connector


class MySQLRepository(Repository):

    def __init__(self):
        #super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # to run on git this should be 'db'
            'port': '32000',  # to run on git this should be '3306'
            'database': 'words'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

"""
    def map_pos(self, entry: dict) -> PartOfSpeech:
        pos_switcher = {
            'adjective': PartOfSpeech.ADJECTIVE,
            'adposition': PartOfSpeech.ADPOSITION,
            'adverb': PartOfSpeech.ADVERB,
            'auxiliary': PartOfSpeech.AUXILIARY,
            'coor. conjunction': PartOfSpeech.C_CONJUNCTION,
            'determiner' = PartOfSpeech.DETERMINER,
            'interjection': PartOfSpeech.INTERJECTION,
            'noun': PartOfSpeech.NOUN,
            'numeral': PartOfSpeech.NUMERAL,
            'particle': PartOfSpeech.PARTICLE,
            'pronoun': PartOfSpeech.PRONOUN,
            'proper noun': PartOfSpeech.PROPER_NOUN,
            'punctuation': PartOfSpeech.PUNCTUATION,
            'sub. conjunction': PartOfSpeech.S_CONJUNCTION,
            'symbol': PartOfSpeech.SYMBOL,
            'verb': PartOfSpeech.VERB,
            'other': PartOfSpeech.OTHER
        }
        pos = pos_switcher.get(entry.get('pos'), None)
        return pos
"""

def load_germanwords(self):
    sql = 'SELECT * FROM german_words'
    self.cursor.execute(sql)
    entries = [{'id': id,
                'word': word,
                'language': language,
                'pos': pos,
                'english_translation': english_translation,
                'ex_sentence': ex_sentence,
                'synonyms': synonyms,
                'number': number,
                'gender': gender,
                'tense': tense,
                'person': person
                } for (id, word, language, pos, english_translation, ex_sentence,
                       synonyms, number, gender, tense, person) in self.cursor]
    words = [self.mapper(entry) for entry in entries]
    return words
