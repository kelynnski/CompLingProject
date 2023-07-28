from app import word
from app.enums import *
from .englishword import EnglishWord


class GermanWord(word.Word):
    def __init__(self, word: str, language: bool, pos: PartOfSpeech, english_translation,
                 ex_sentence: str, synonyms: list):
        super().__init__(word, language)
        self.pos = pos
        self.english_translation = english_translation
        self.ex_sentence = ex_sentence
        self.synonyms = synonyms


class Noun(GermanWord):
    def __init__(self, word: str, language: bool, pos: PartOfSpeech, english_translation,
                 ex_sentence: str, synonyms: list, number: Number, gender: Gender):
        super().__init__(word, language, pos, english_translation, ex_sentence, synonyms)
        self.number = number
        self.gender = gender


class Verb(GermanWord):
    def __init__(self, word: str, language: bool, pos: PartOfSpeech, english_translation,
                 ex_sentence: str, synonyms: list, tense: Tense, person: Person):
        super().__init__(word, language, pos, english_translation, ex_sentence, synonyms)
        self.tense = tense
        self.person = person