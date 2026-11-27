gewicht = input('Wat is je geiwcht?: ')
gewichtfloat = float(gewicht)
lengte = input('Wat is je lengte in meters?: ')
lengtefloat = float(lengte)

bmi = float(gewichtfloat / (lengtefloat * lengtefloat))
bmi1= round(bmi, 1)

if bmi < 18.5:
    print (bmi1)
    print('ondergewicht')
elif bmi >= 18.5 and bmi < 25:
    print (bmi1)
    print('gezond gewicht')
elif bmi >= 25:
    print (bmi1)
    print('overgewicht')