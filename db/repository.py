import abc
from app.germanword import *
from app.englishword import *
from app import word


class Repository(metaclass=abc.ABCMeta):

    def load_word(self):
        raise NotImplementedError

    def load_germanword(self):
        pass

    def load_englishword(self):
        raise NotImplementedError
