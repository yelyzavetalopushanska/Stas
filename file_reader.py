with open("package/for_reading.txt") as file:
    content = file.read()

print(content)

# try:
#     a = int(input("Enter the number: "))
# except Exception:
#     print("You entered not a number")

try:
    a = int(input("Enter the number (but not zero): "))
    print(10/a)

except ValueError:
    pass
    # print("Not a number")

except ZeroDivisionError:
    print("Divition by zero")

else:
    # выполняется в том случаи если блок try не переходит в except
    print("Try block was done")


#
# except Exception:
#     print("Another exc")