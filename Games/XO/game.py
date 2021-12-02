import functionals as f

x = 'X'
o = 'O'

field = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]

fill_field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

f.print_field(field)

# PvP
# for i in range(9):
#     if i % 2 == 0:
#         while True:
#             cell = f.cell_input(x)
#             state = f.valid(cell, x, field, fill_field)
#             if state:
#                 break
#     else:
#         while True:
#             cell = f.cell_input(o)
#             state = f.valid(cell, o, field, fill_field)
#             if state:
#                 break
#     if i > 3:
#         if f.winner(x, field):
#             print("Победил X")
#             break
#         elif f.winner(o, field):
#             print("Победил О")
#             break
#     if i == 8:
#         print('Ничья')
#     f.print_field(field)


# PvE
for i in range(9):
    if i % 2 == 0:
        while True:
            cell = f.cell_input(x)
            state = f.valid(cell, x, field, fill_field)
            if state:
                break
    else:
        print('Ход компьютера')
        f.bot_move(field, fill_field)

    if i > 3:
        if f.winner(x, field):
            f.print_field(field)
            print("Победил X")
            break
        elif f.winner(o, field):
            f.print_field(field)
            print("Победил О")
            break
    if i == 8:
        print('Ничья')
    f.print_field(field)
