# German Lexical Information

## Providing a German word
Users can input a word in German using the first interface.
Two examples of words users can enter are 'Wasser' and 'laufen'.
The page will then display the lexical information for that word such as part of speech, the English translation,
German synonyms for the word, etc. as a JSON string. For example, if a user enters 'Wasser' the output will be:

    {
        "english_translation": "water",
        "ex_sentence": "Ich trinke gerne Wasser",
        "gender": "NEU",
        "number": "SINGULAR",
        "pos": "NOUN",
        "synonyms": "Aqua, H2O, blaues Gold"
    }



The API can be used without going through the front end using a POST request, with the endpoint
'http://localhost:5000/get_word'. The JSON body needs to have the "word" key, for example:

{"word":"Wasser"}

## Providing an English word
Users can also provide an English word into the second interface, and get the same information as described
above about the translated word.

The endpoint for this API is 'http://localhost:5000/get_translation' and also requires a JSON body with the 'word' key.