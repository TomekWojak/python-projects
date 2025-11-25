stopnie = ("Szeregowy","Kapral","Sierżancie","Porucznik","Kapitan","Major","Pułkownik")

ilosc_stopni = len(stopnie)
major_index = stopnie.index('Major')
pulkownik_wystepowanie = 'Pułkownik' in stopnie

print(ilosc_stopni) # 7
print(major_index) # 5
print(pulkownik_wystepowanie) # True

