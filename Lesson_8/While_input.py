# пример ввода
#message = input("Tell me something: ")
#print(message)

# приведение типов
#a = int(input("a = "))
#b = int(input("b = "))
#c = a + b
#print(f'a + b = {c}')

# цикл while
message2 = ''
messages = []

while message2 != 'quit':
    message2 = input("Enter your message: ")
    messages.append(message2)
print(messages)