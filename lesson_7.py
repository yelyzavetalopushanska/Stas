all_inc = ('пицца','салат','ростбиф','стейк','лосось')
for p in all_inc:
    print(p)

#all_inc.append('burger') отказ
new_deshes = ('десерт','торт')

all_inc = new_deshes + all_inc[2:]
for d in all_inc:
    print(d)