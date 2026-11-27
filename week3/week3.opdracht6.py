prijs = input("Wat is de prijs?: ")
prijsfloat = float(prijs)
lid = input("ben je lid, ja of nee?: ")

if lid == "ja":
    print(prijsfloat - (10 / 100 * prijsfloat))
elif lid == "nee":
    print(prijsfloat)