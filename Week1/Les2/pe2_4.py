uurLoon = float(input("Wat verdien je per uur: "))
urenGewerkt = float(input("Hoeveel uur heb je gewerkt: "))
totaalLoon = urenGewerkt * uurLoon
urenGewerktStr = str(urenGewerkt)
uurLoonStr = str(uurLoon)
totaalLoonStr = str(totaalLoon)
overzicht = urenGewerktStr + " uur werken levert " + totaalLoonStr + " Euro op"
print(overzicht)