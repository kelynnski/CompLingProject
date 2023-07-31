from db.mysql_repository import *

def test_load_germanword():
    repo = MySQLRepository()
    words = repo.load_germanword()
    assert isinstance(words, list)
    assert len(words) == 2
    assert words[0]['word'] == 'laufen'
    repo.close()

