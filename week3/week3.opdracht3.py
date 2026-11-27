getal1 = input('Kies een eerste getal:')
getal2 = input('Kies een tweede getal:')
getal1int = int(getal1)
getal2int = int(getal2)

if getal1int > getal2int:
    print(f'getal 1 is hoger dan getal 2 ({getal1int} > {getal2int})')
elif getal1int < getal2int:
    print(f'getal 2 is hoger dan getal 1 ({getal2int} > {getal1int})')
else:
    print(f'getal 1 is gelijk aan getal 2 ({getal2int} = {getal1int})')