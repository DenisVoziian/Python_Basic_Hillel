# Для задания 1-7 за основу можете взять код из предідущих ДЗ.
#
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.


def get_flip_even_index_list(input_list):
    new_list = []
    for index, value in enumerate(input_list):
        new_list.append(value) if index % 2 == 0 else new_list.append(value[::-1])
    return new_list


my_list_1 = ['12345', '23456', '34567', '45678', '56789']
new_my_list_1 = get_flip_even_index_list(my_list_1)
print(new_my_list_1)


# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".


def get_start_a_list(input_list):
    new_list = [value for value in input_list if value.startswith('a')]
    return new_list


my_list_2 = ['12a345', 'a23456', '345a67', 'a45678', 'A56789']
new_my_list_2 = get_start_a_list(my_list_2)
print(new_my_list_2)


# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.


def get_include_a_list(input_list):
    new_list = [value for value in my_list_3 if 'a' in value]
    return new_list


my_list_3 = ['12a345', 'a23456', '345a67', 'a45678', 'A56789']
new_my_list_3 = get_include_a_list(my_list_3)
print(new_my_list_3)

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.


# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
#
# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#
# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
#
# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
