leeftijd = input("Hoe oud ben je?: ")
leeftijdint = int(leeftijd)
geldigid = input('Heb je een geldig ID, ja of nee?: ')

if leeftijdint >= 18 and geldigid == "ja":
    print("je mag een leeftijdsgebonden product kopen")
else:
    print("je mag geen leeftijdsgebonden product kopen")
