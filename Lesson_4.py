my_list = ["element1", "element2", "element3", "element4"]
my_second_list = []

for i in my_list:
    print("Next element")
    print(i)

print("End of for")

for i in range(len(my_list) - 1):
    print(my_list[i] + " " + my_list[i+1])

for i in range(3, 8):
    print(i)

print("Next range")

for i in range(10, 20, 2):
    print(i)

my_third_list = [i**2 for i in range(2, 5)]

print(my_third_list)

my_fourth_list = [f'A{i}' for i in range(5)]
print(my_fourth_list)

my_fiveth_list = ["word" for i in range(8)]
print(my_fiveth_list)