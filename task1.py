# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
import numpy
def filter_count_of_words  (text):
    delta = False
    s=0
    if text[0].isnumeric() or text[0].isupper() or text[0].islower(): #Слова будут начинаться с цифры или буквы
        s+=1
        delta=True
    for i in range(len(text)):
        if text[i] == " " or text[i] == '\n' or text[i]=='\t':
            delta = False
        elif not(delta) and (text[i].isnumeric() or text[i].isupper() or text[i].islower()):
            delta = True
            s+=1
    return s

with open('task1.txt', encoding='utf-8') as f:
    text = f.read()
count_of_strings = text.count('\n') + 1
count_of_words = filter_count_of_words(text)
count_of_letters = len(text)
print(text, "Общее количество строк в файле:", count_of_strings)
print("Общее количество слов во всем тексте файла:", count_of_words)
print("Общее количество символов:", count_of_letters)