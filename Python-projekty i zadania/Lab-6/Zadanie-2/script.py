import matplotlib.pyplot as plt


kategorie = ['Pieczywo', 'Słodycze', 'Nabiał', 'Napoje', 'Mięso']
udzial = [150, 290, 320, 220, 400]
plt.pie(udzial, labels=kategorie,
autopct='%1.f%%', startangle=90,
colors=['skyblue', 'lightgreen',
'lightcoral', 'gold'])
plt.title('Udział w kategoriach')
plt.show()
