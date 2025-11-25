owoce = ('jabłko', 'banan', 'gruszka', 'banan', 'banan', 'malina')

def poznaj_liczbe_owocow(owoc):
    print(f'{owoc[0].upper() + owoc[1:]} występuje {owoce.count(owoc)} razy')


poznaj_liczbe_owocow('banan')