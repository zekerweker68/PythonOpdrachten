getal = (input("Typ een getal in:"))
getalint = int(getal)

if getalint > 0:
    print(f'jouw getal ({getalint}) is positief')
elif getalint < 0:
    print(f'jouw getal ({getalint}) is negatief')
else:
    print(f'jouw getal ({getalint}) is nul')