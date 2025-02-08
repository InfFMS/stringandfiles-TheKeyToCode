# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
import re
with open('task2.txt', encoding='utf-8') as f:
    text = f.read()
print(text)
words = list(re.split(r'[ \n,?!.]', text))
words.sort()
print(words)

words = list(set(words))
print(words)
if len(words) > 0 and words[0]=='':
    words.pop(0)
print(len(words))