import itertools
p_list = []
for x in itertools.product(range(3), repeat = 3):
    p_list.append(x)
print(p_list)
