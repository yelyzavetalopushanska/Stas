numbers = [1,2,3,4,5,6,7,8,9]
if 1 in numbers:
    print("1st")
if 2 in numbers:
    print("2nd")
if 3 in numbers:
    print("3rd")
''' 
не смог
"1st 2nd 3rd 4th 5th 6th 7th 8th 9th",
'''
#if  in numbers:
#        print(f'{i} + "th"')

for i in range(3, 9):
    print(f'{numbers[i]}th')

for i in numbers[3:]:
    print(f'{i}th')