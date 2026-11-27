leeftijd = input("Wat is je leeftijd?: ")
leeftijdint = int(leeftijd)

if leeftijdint >= 0 and leeftijdint < 13:
    print("kind")
elif leeftijdint >= 13 and leeftijdint <= 17:
    print("tiener")
else:
    print('volwassene')