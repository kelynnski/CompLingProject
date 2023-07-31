from db.mysql_repository import *

repo = MySQLRepository()


def test_load_germanword():
    words = repo.load_germanword()
    print(words)

