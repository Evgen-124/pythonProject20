my_string = input("Введите произвольный текст: ")
print("Количество символов в тексте:", len(my_string))
print("Строка в верхнем регистре:", my_string.upper())
print("Строка в нижнем регистре:", my_string.lower())
my_string = my_string.replace(" ", "")
print("Строка без пробелов:", my_string)
print("Первый символ строки:", my_string[0])
print("Последний символ строки:", my_string[-1])
