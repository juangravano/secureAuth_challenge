from text_helper import Text

text = open("text.txt", "r")  # Abro archivo con el texto
text = text.read()  # Leo archivo con el texto

#Imprimo resultados
print(f"Palabras : {len(Text.clean_text(text))}")
print(f"Frecuencia : {Text.count_frequent_words(text)}")
print(f"Top-5 : {Text.top_words_frequency(text, 5)}")

