import db.mysql_repository


class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MySQLRepository()

    def get_word_details(self, german_word):
        word_details = self.repo.load_germanword(german_word)

        # If word doesn't exist:
        if not word_details:
            return f"'{german_word}' not found in the database."
        return {key: value for key, value in word_details.items() if value is not None}

    def get_from_english(self, word):
        word_details = self.repo.translate_english_word(word)

        # If word doesn't exist:
        if not word_details:
            return f"'{word}' not found in the database."
        return {key: value for key, value in word_details.items() if value is not None}
