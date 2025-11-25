imiona = ['Jan', 'Bartek', 'Agnieszka', 'Ala']

# a)
imiona_posortowane = sorted(imiona)
print(imiona_posortowane)

# b)
imiona.append('Łukasz')
imiona.append('Alan')

ostatnia_osoba = imiona.pop()
print(ostatnia_osoba)

# c)
imiona.insert(3, 'Oliwia')
print(imiona)

# d)
imiona.reverse()
imiona *= 2
print(imiona)