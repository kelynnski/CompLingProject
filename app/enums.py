from enum import Enum


class PartOfSpeech(Enum):
    ADJECTIVE = 1
    ADPOSITION = 2
    ADVERB = 3
    AUXILIARY = 4
    C_CONJUNCTION = 5
    DETERMINER = 6
    INTERJECTION = 7
    NOUN = 8
    NUMERAL = 9
    PARTICLE = 10
    PRONOUN = 11
    PROPER_NOUN = 12
    PUNCTUATION = 13
    S_CONJUNCTION = 14
    SYMBOL = 15
    VERB = 16
    OTHER = 17


class Tense(Enum):
    PRESENT = 1
    PERFECT = 2
    PAST = 3
    FUTURE = 4


class Person(Enum):
    ICH = 1
    DU = 2
    ER_SIE_ES = 3
    WIR = 4
    IHR = 5
    SIE_SIE = 6


class Gender(Enum):
    MAS = 1
    FEM = 2
    NEU = 3


class Number(Enum):
    SINGULAR = 1
    PLURAL = 2