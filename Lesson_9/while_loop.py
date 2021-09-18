# бесконечный цикл
while True:
    print("Я выполняюсь бесконечно!!!!!!!!!!!!!")
    break


pizza = []
toppings = ['кетчуп', 'сыр', 'помидоры']
active = True # флаг

'''
while active:
    topping = input('Введите топпинг: ')
    if topping in toppings:
        pizza.append(topping)
    elif topping == 'quit':
        active = False
    elif topping not in toppings:
        active = False
'''

pizza = []
toppings = ['кетчуп', 'сыр', 'помидоры']

while True:
    topping = input('Введите топпинг: ')
    if topping in toppings:
        pizza.append(topping)
        continue
    break
