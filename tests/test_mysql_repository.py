from db.mysql_repository import *

repo = MySQLRepository()


def test_load_germanwords():
    words = repo.load_germanword()
    print(words)

