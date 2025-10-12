
# Przykład A
# 1.
print(type(1 + 2)) # 3, <class 'int'>, + => operator dodawania

#2
print(type(1 + 4.5)) # 5.5, <class 'float'>, + => operator dodawania

#3
print(type(3 / 2)) # 1.5, <class 'float'>, / => operator dzielenia

#4
print(type(4 / 2)) # 2.0, <class 'float'>, / => operator dzielenia

#5
print(type(3 // 2)) # 1  <class 'int'> // => operator dzielenia całkowitego z zaokrąglaniem w dół

#6
print(type(-3 // 2)) # -2, <class 'int'> // => operator dzielenia całkowitego z zaokrąglaniem w dół

#7
print(type(11 % 2 )) # 1, <class 'int'> % => modulo, określa resztę z dzielenia przez daną liczbę

#8
print(type(2 ** 10)) # 1024, <class 'int'> ** => operator potęgowania

#9
print(type(8 ** (1/3))) # 2.0 <class 'float'> ** => operator potęgowania


# Przykład B

#1
print(int(3.0), type(int(3.0))) # 3, <class 'int'> => int wymusza konwersję na liczbę całkowtą

#2
print(float(3), type(float(float(3)))) # 3.0, <class 'float'> => float wymusza konwersję na liczbę zmiennoprzecinkową

#3
print(float("3"), type(float(float(3)))) # 3.0, <class 'float'> => konwersja str na liczbę zmiennoprzecinkową

#4
print(str(12.4), type(str(12.4))) # "12.4", <class 'str'> => konwersja liczby zmiennoprzecinkowej na str

#5
print(bool(0), type(bool(0))) # False, <class 'bool'> => konwersja na typ bool, cyfra zero należy do 'falsy values', więc wynik to False
