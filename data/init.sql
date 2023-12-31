CREATE DATABASE words;
use words;

CREATE TABLE german_words (
    id INT NOT NULL AUTO_INCREMENT,
    word VARCHAR(50),
    lang INT,
    pos VARCHAR(30),
    english_translation VARCHAR(50),
    ex_sentence VARCHAR(300),
    synonyms VARCHAR(300),
    number VARCHAR(30),
    gender VARCHAR(3),
    tense VARCHAR(30),
    person VARCHAR(30),
    PRIMARY KEY (id)
    );

INSERT INTO german_words
    (word, lang, pos, english_translation, ex_sentence, synonyms, number, gender, tense, person)
VALUES
    ('laufen', '0', 'VERB', 'to walk', 'Wir laufen schnell', 'rennen, sprinten, stieben', NULL, NULL, 'PRESENT', 'Wir, Sie/sie'),
    ('Wasser', '0', 'NOUN', 'water', 'Ich trinke gerne Wasser', 'Aqua, H2O, blaues Gold', 'SINGULAR', 'NEU', NULL, NULL);


CREATE TABLE english_words (
    id INT NOT NULL AUTO_INCREMENT,
    word VARCHAR(50),
    lang INT,
    german_translation VARCHAR(50),
    PRIMARY KEY (id)
    );

INSERT INTO english_words
    (word, lang, german_translation)
VALUES
    ('walk', '1', 'laufen'),
    ('water', '1', 'Wasser');
