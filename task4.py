# Напишите программу, которая просит пользователя ввести несколько предложений (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "_".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.

n = int(input("Введиет количество строк, что будете вводить: "))

text = ''
for i in range(n):
    current_string = input()
    current_string = current_string.upper()
    current_string = current_string.replace(' ','_')
    text+=current_string + "\n"
with open('task4.txt', "+w") as f:
    f.write(text)
with open('task4.txt', "r") as f:
    content = f.read()
    print(content)

