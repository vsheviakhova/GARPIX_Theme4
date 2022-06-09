lst1 = ['Санкт-Петербург', 'Москва', 'Казань']
lst2 = ['Воронеж', 'Санкт-Петербург', 'Иваново']

intersection_lst = []
complement_lst = []

for i in lst1:
    for k in lst2:
        if i == k:
            intersection_lst.append(i)
print(f'Города, которые есть в обоих списках: {intersection_lst}')

for i in lst1:
    for k in intersection_lst:
        if i != k:
            complement_lst.append(i)

for i in lst2:
    for k in intersection_lst:
        if i != k:
            complement_lst.append(i)
print(f'Города, которые есть только в одном из списков: {complement_lst}')


