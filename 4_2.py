list1 = [5, 10, 15, 20, 25, 50, 20, 20, 20]
for i in list1:
    if i == 20:
        i_index = list1.index(20)
        list1[i_index] = 200
print(list1)