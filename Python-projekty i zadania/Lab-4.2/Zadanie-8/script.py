import keyword

def sprawdzCzySlowoJestKluczowe(a):
    jestKluczowe = keyword.iskeyword(a)
    return jestKluczowe

print(sprawdzCzySlowoJestKluczowe("for"))
print(sprawdzCzySlowoJestKluczowe("print"))
print(sprawdzCzySlowoJestKluczowe("break"))
print(sprawdzCzySlowoJestKluczowe("done"))
print(sprawdzCzySlowoJestKluczowe("bad"))
