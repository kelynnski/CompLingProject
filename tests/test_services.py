from services.services import Services


def test_services():
    service = Services()
    word_info = service.get_word_details("Wasser")
    print(word_info)
    englishtest = service.get_from_english('to walk')
    print(englishtest)
