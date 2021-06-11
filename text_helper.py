class Text:
    @staticmethod
    def clean_text(text):
        """Limpia el texto de caracteres especiales y convierte todo a minúscula"""
        special_characters = ",.;:?!¡¿"
        for char in special_characters:
            text = text.replace(char,
                                "")

        text = text.lower()
        words = text.split()
        return words

    @classmethod
    def count_frequent_words(cls, text):
        """Encuentra las palabras repetidas en el texto"""
        frequents = {}
        for words in cls.clean_text(text):
            frequents[words] = frequents.get(words, 0) + 1

        for words in list(frequents):
            if frequents[words] < 2:
                frequents.pop(words)

        return frequents

    @classmethod
    def top_words_frequency(cls, text, top):
        """Ordena las palabras frecuentes en un top indicado por parámetros"""
        ranking = sorted(cls.count_frequent_words(text).items(), key=lambda x: x[1], reverse=True)
        ranking = ranking[0:top]
        return ranking
