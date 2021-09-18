# обьявление функции

def great_user():
    '''Приветсвие пользователя'''
    print('Hello')

great_user()

# передача аргументов
def great_user_by_name (username):
    '''Обращение к пользователю по имени'''
    print(f'Hello, {username.title()}!')

great_user_by_name('stas')
great_user_by_name('liza')