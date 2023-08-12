from db.mysql_repository import *

def test_load_germanword():
    repo = MySQLRepository()
    word_details = repo.load_germanword("Wasser")
    print(word_details)
    assert word_details is not None
    #assert word_details['word'] == "Wasser"
    assert word_details['english_translation'] == "water"
    repo.close()

def test_translate():
    repo = MySQLRepository()
    word_details = repo.translate_english_word("water")
    print(word_details)
    assert word_details is not None
    assert word_details['german_translation'] == "Wasser"
    assert word_details['pos'] == "NOUN"
    repo.close()
