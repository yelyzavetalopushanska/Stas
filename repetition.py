# my_list = ["some", "words", "in", "the", "list"]
# my_list.reverse()
# print(my_list)
#
# new_list = [num + 10 for num in range(7, 90, 5)]
# print(new_list)
#
# a = 7
# b = 90
# c = a
# print(c)
# c = b
# print(c)
# c = "something"
# print(c)
#
# tuple_1 = (6, 9)
# tuple_2 = (7, 90, 5)
# print(tuple_1)
# print(tuple_2)
#
# tuple_1 = (7, 9)
# print(tuple_1)

for i in range(10, 90, 5):
    if i % 10 == 0:
        continue
    else:
        print(i)

inp = input("Input 0 for exit: ");

while inp != "0":
    print(inp)
    inp = input("Input 0 for exit: ");
