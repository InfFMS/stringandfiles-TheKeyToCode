# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
import re
def found_max(words):
    max_word = ""
    for i in range(len(words)):
        if(len(words[i]) > len(max_word)):
            max_word=words[i]
    return max_word
with open('task5.txt', encoding='utf-8') as f:
    text = f.read()

words = list(re.split(r'[ \n,?!.]', text))
words = list(set(words))
max_word = found_max(words)
print("Самое длинное слово:",max_word)
print("Его длина:",len(max_word))
