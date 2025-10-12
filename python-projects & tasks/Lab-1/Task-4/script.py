Cena = 39.99
Rabat = .2
Cena_po_rabacie = round((Cena - Cena * Rabat), 2) # metoda round pozwala na zaokrąglenie danej wartości liczbowej. Można podać także opcjonalny, drugi argument w celu określenia dokładności zaokrąglenia

print(Cena_po_rabacie)