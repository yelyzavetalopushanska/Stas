# множества (set)
my_set = {'Alice', 'alice', 8, 10}

# словарь (dict)
my_dict = {'people1' : 'Alice',
           'people2' : 'Stas',
           'people3' : 'Ivan'}

# список словарей
kiev_users = {'Petya' : ['number1', 'number2'],
         'Ira' : ['number1']}

lviv_users = {'Vasya' : ['number1', 'number2'],
         'Anya' : ['number1']}

city_list = [kiev_users, lviv_users]

# словарь в словаре
dict_in_dict = {
    'Vasya' : {'MTC'      : ['number1', 'number2'],
               'Kievstar' : ['number1'],
               'Life'     : ['number1', 'number2']},
    'Kolya' : {'MTC'      : ['number1', 'number2'],
               'Kievstar' : ['number1'],
               'Life'     : ['number1', 'number2']},
}