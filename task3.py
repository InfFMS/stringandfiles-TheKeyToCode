# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
import re
# import DataFrame
def dropna(n):
    i = 0
    while i < len(n):
        if n[i]=="":
            n.pop(i)
            # print("DEL")
        i+=1
with open('task2.txt', encoding='utf-8') as f:
    text = f.read()
# print(text)
words = list(re.split(r'[ \n,?!. ]', text))
dropna(words)
words1 = {}
# print(words)
for i in words:
    if i in words1:
        words1[i]+=1
    else:
        words1[i]=1
# words.sort()
# print(words)
# words = list(set(words))
# print(words)
if len(words) > 0 and words[0]=='':
    words.pop(0)
print("Всего слов:", len(words1))
print("Сами слова:")
current_index = 0
for i in words1:
    current_index+=1
    print(str(current_index) + ".", i, words1[i])