# обьявление словаря
pizza = {'peperoni'  : 'tomato',
         'havai'     : 'chicken, pineapple, tomato',
         'margarita' : 'tomato, cheese'}

# обращаемся к элементу словаря
print(pizza['peperoni'])

# добавление элементов в словарь
pizza['diablo'] = 'pepper, meat, mashrooms'
print(pizza['diablo'])

# создание пустого словаря
dictionary = { }

# изменение значения в словаре
pizza['margarita'] = 'tomato, cheese, chedder'
print(pizza)

# удаление элементов из словаря
del pizza['diablo']
print(pizza)

# обращение к элементу словаря
print(pizza.get('diablo', 'Pizza was delete'))

# вывод элементов "ключ-значение"
for i, j in pizza.items():
    print(f'key: {i}')
    print(f'value: {j}')
print('=======================================================')

# перебор ключей
for element in pizza:
    print(element)
print("===")
for element in pizza.keys():
    print(element)

# метод .keys() для конструкции if
if 'tomato' in pizza.keys():
    print('true')

# сортировка вывода
print('=====sort=====')
for element in sorted(pizza.items()):
    print(element)

# перебор значений
for element in pizza.values():
    print(element)

# вывод не повторяющихся значений
cars = {'shop 1' : 'audi ford reno',
        'shop 2' : 'bmw fiat jaguar',
        'shop 3' : 'audi ford reno'}
print("=====cars=====")

for element in set(cars.values()):
    print(element)