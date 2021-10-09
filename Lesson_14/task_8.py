'''
Сообщения: создайте список с серией коротких сообщений. Передайте список функции show_messages(),
которая выводит текст каждого сообщения в списке
Отправка сообщений: начните с копии вашей программы из упражнения 9. Напишите функцию send_messages(),
 которая выводит каждое сообщение и перемещает его в новый список с именем sent_messages.
 После вызова функции выведите оба списка и убедитесь в том, что перемещение прошло успешно'''

short_msg_list = [ 'Hi man!', 'Whats up!', 'Hello girl!']
second_msg_list = ['How do u do?', 'Hello, friend']


def show_messages(msg_list):
    '''Функця для показа сообщений'''
    for i in msg_list:
        print(i)


show_messages(short_msg_list)

# part 2
sent_messages = []


def messages(msg_lst, sent_msg_list):
    ''' Функция для отображения и перемещения элементов'''

    copy_msg_list = msg_lst[:]

    while copy_msg_list:
        ready = copy_msg_list.pop(0)
        sent_msg_list.append(ready)


messages(short_msg_list, sent_messages)
print(short_msg_list)
print(sent_messages)