# 1. Дано целое число (int). Определить сколько нулей в этом числе.

num_1 = 1234003003250000
num_str_1 = str(num_1)
result_1 = len([symbol for symbol in num_str_1 if symbol == '0'])
print(result_1)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

num_2 = 123400300325000
result_2 = 0
while num_2 % 10 == 0:
    num_2 //= 10
    result_2 += 1
print(result_2)

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_3_1 = ['a', 'b', 'c', 'd', 'e', 'f']
my_list_3_2 = ['g', 'h', 'i', 'j', 'k']
my_result_3 = []
my_result_3 = my_list_3_1[::2] + my_list_3_2[1::2]
print(my_result_3)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list_4 = [1, 2, 3, 4]
new_list_4 = my_list_4.copy()
val_first_4 = new_list_4.pop(0)
new_list_4.append(val_first_4)
print(new_list_4)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list_5 = [1, 2, 3, 4]
val_first_5 = my_list_5.pop(0)
my_list_5.append(val_first_5)
print(my_list_5)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

str_6 = "43 больше чем 34 но меньше чем 56"
str_list_6 = str_6.split(" ")
result_6 = sum([int(value) for value in str_list_6 if value.isdigit()])
print(result_6)

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str_7 = "My long string"
l_limit_7 = "o"
r_limit_7 = "g"
start_index_7 = my_str_7.index(l_limit_7)
end_index_7 = my_str_7.rindex(r_limit_7)
sub_str_7 = my_str_7[start_index_7 + 1:end_index_7:]
print(sub_str_7)

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

my_str_8 = "abcde"
if not len(my_str_8) % 2 == 0:
    my_str_8 += "_"
my_str_list_8 = [my_str_8[index:index + 2] for index in range(0, len(my_str_8), 2)]
print(my_str_list_8)

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

numb_list = [2, 4, 1, 5, 3, 9, 0, 7]
numb_list_9 = [numb_list[i] for i in range(1, len(numb_list) - 1) if numb_list[i] > numb_list[i - 1] + numb_list[i + 1]]
result_9 = len(numb_list_9)
print(result_9)

# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

my_list_10 = [1, 2, 3, "11", "22", 33]
str_list_10 = [value for value in my_list_10 if type(value) == str]
print(str_list_10)

# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.

my_str_11 = "asdfasewasdfasadfqwraakip"
my_str_list_11 = set(my_str_11)
my_symbol_list_11 = [symbol for symbol in my_str_list_11 if my_str_11.count(symbol) == 1]
print(my_symbol_list_11)

# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_12_1 = "asdfasewasdfasadfqwraakip"
my_str_12_2 = "kejgfkwengi2utiweiterwtjha"
my_symbol_list_12 = list(set(my_str_12_1) & set(my_str_12_2))
print(my_symbol_list_12)

# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

my_str_13_1 = "aaaasdf1"
my_str_13_2 = "asdfff2"
my_str_set_13 = set(my_str_13_1) & set(my_str_13_2)
my_unique_symbol_list_13 = [symbol for symbol in my_str_set_13 if (my_str_13_1 + my_str_13_2).count(symbol) == 2]
print(my_unique_symbol_list_13)

