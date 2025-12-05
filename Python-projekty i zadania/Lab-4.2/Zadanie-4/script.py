import random
max_liczba = 100

# a)
def wylosj_szczesliwa_liczbe():
    twoja_liczba = random.randint(0,max_liczba)
    print(f'Twoja szczęśliwa liczba to: {twoja_liczba}')
wylosj_szczesliwa_liczbe()

# b)
roczniki = [1996, 2001, 1999, 2005, 1997, 2003, 2008, 1995, 2000, 2006,
            2002, 1998, 2004, 2007, 1996, 2001, 2003, 2005, 1999, 2007]
def wylosuj_szczesliwy_rocznik():
    szczesliwy_rocznik = random.choice(roczniki)
    print(f'Szczęśliwy rocznik to: {szczesliwy_rocznik}')
wylosuj_szczesliwy_rocznik()