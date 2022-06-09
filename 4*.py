strings = []

while True:
    str = input('Напишите что-нибудь: ')
    strings.append(str)
    if str == 'q':
        break

print(strings)
