cars = ['Bmw', 'audi', 'ford', 'reno']

if 'audi'.lower() in cars and 'fORd'.lower() in cars:
    print("эти машины в наличии")

if cars:
    print("Список заполнен")
else:
    print("Список пуст")

for car in cars:
    if car.lower() == 'bmw':
        print(car.upper())
    else:
        print(car.title())

age = -80
if age > 0 and age < 4:
    print("Тебе билет бесплатный")
elif age >= 4 and age < 12:
    print("Тебе билет стоит 100 грн")
elif age >= 12 and age < 18:
    print("Тебе билет стоит 150 грн")
elif age >= 18 and age <= 150:
    print("Тебе билет стоит 200 грн")
else:
    print("Некорректный возраст")

'''
meal = ['сахар', 'хлеб']
for i in meal:
    if i == 'хлеб' or i == 'мука':
        print(i)
        print('Покупаю!')
        break
    else:
        print("У Вас нет того, что мне нужно!")
'''