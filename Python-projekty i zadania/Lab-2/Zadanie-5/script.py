# a)
def pokazNotowania():
    with open('notowania_gieldowe.txt', 'r') as plik:
        for linia in plik:
            print(linia.strip())

pokazNotowania()

# b)
with open('notowania_gieldowe.txt', 'a') as plik:
        plik.write('ALR, 113\n')

pokazNotowania()
