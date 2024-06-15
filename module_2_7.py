#Цель задания: Освоить создание функций с параметрами по умолчанию и практику вызова этих функций с различным количеством аргументов.
#Задача "Распаковка"

#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'Hello', c = True):
    print(a,b,c)
print_params()
print_params(2, 7)
print_params(b = 25)
print_params(c = [1,2,3])

#2.Распаковка параметров:
values_list = [1, 'Hello', True]
values_dict = {'a': False, 'b': 27, 'c': 'Bye'}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)