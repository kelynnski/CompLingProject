from app import word
from app.germanword import *


class EnglishWord(word.Word):
    def __init__(self, word: str, language: bool, german_translation):
        super().__init__(word, language)
        self.german_translation = german_translation
