cijferICOR = 7
cijferPROG = 7
cijferCSN = 8.5
gemiddelde = str((cijferICOR + cijferPROG + cijferCSN) / 3)
beloning = str((cijferICOR * 30) + (cijferPROG * 30) + (cijferCSN * 30))
overzicht = "Mijn cijfers (gemiddeld een " + gemiddelde + ") leveren een beloning van €" + beloning + " op!"
print(overzicht)