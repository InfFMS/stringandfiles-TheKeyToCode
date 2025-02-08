# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
import numpy

with open('task2.txt', encoding='utf-8') as f:
    text = f.read()
print(type(text))
text = text.replace("Python","Питон")
try:
    file = open('task2_answer.txt', 'r+', encoding='utf-8')
except IOError:
    file = open('task2_answer.txt', 'w+', encoding='utf-8')
file.write(text)
