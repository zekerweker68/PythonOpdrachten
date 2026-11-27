jaar = input('Typ een jaartal in: ')
jaarint = int(jaar)

if jaarint % 4 == 0 and jaarint % 100 != 0 or jaarint % 400 == 0:
    print(f'De jaar {jaarint} is een schrikkeljaar')
else:
    print(f'De jaar {jaarint} is geen schrikkeljaar')