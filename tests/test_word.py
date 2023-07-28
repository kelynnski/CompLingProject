#from app.word import Word
from app.germanword import *
from app.englishword import *

def test_word():
    my_word = word.Word('music', 0)
    print(my_word.word)
    assert my_word.word == 'music'


def test_gerword():
    my_word = GermanWord('Musik', 1, 8, 'music', 'Ich hoere Musik', ['Test1', 'Test2'])
    print(my_word.synonyms)
    assert my_word.ex_sentence == 'Ich hoere Musik'


def test_engword():
    my_word = EnglishWord('cat', 0, 'Katze')
    print(my_word.language)
    assert my_word.language == 0