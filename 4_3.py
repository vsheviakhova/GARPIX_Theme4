list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]

for i in list1:
    if i == "":
        i_index = list1.index(i)
        list1.pop(i_index)
#тут я не поняла, почему в цикле все-таки остаются
# последние "" и тупо удалила их через remove.
# А почему цикл не удаляет последнюю пустую строку?

list1.remove("")
print(list1)
