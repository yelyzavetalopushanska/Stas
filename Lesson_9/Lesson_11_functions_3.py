# функции, которые возвращают значение

def subtracting (a, b):
    return a - b

c = subtracting(3, 7)
#print(c)

# изменения данных внутри функции
unprinted_designes = ['корпус', 'флаер', 'визитка', 'колеса']
completed = [ ]

def print_models (unprinted_designes, completed):
    while unprinted_designes:
        current = unprinted_designes.pop()
        print(f'Печать {current}')
        completed.append(current)

#print(unprinted_designes)
#print(completed)
#print_models(unprinted_designes[:], completed)
#print(f"Unprinted: {unprinted_designes}")
#print(f"Printed: {completed}")

# методы с произвольным количеством аргументов
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)

#make_pizza('tomato', 'cheese', 'pepper')
#print("===")
#make_pizza('chicken')

# именованый метод с произвольным количеством аргументов
# def make_pizza2 (sauce, *toppings):

# использование произвольного количества аргументов
def person (name, last, **additional_info):
    additional_info['first_name'] = name
    additional_info['last_name'] = last
    return additional_info

#print(person('Stas', 'Koval', location = 'Kiev', age = 33))