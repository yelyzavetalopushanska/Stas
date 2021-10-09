import json
# простое чтение из файла
# абсолютный путь к файлу
filename = 'C:\\Urs\\38068\\Desktop\\file.txt'
try:
    with open(filename) as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

# запись данных в файл
filename_2 = 'package/filename_2'
with open(filename_2, 'w') as file:
    file.write("Old info\n")

# добавить инфо к уже существующему файлу
with open(filename_2, 'a') as file:
    file.write("New info")

