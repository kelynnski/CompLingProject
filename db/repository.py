import abc
from app.germanword import *
from app.englishword import *
from app import word


class Repository:

    def load_word(self):
        raise NotImplementedError

    def load_germanword(self):
        raise NotImplementedError

    def load_englishword(self):
        raise NotImplementedError
