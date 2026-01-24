import matplotlib.pyplot as plt

# czas (s)
x = [1, 2, 3, 4, 5]

# prędkość chwilowa (m/s)
y = [2, 4, 6, 8, 10]

plt.scatter(x, y)
plt.xlabel("Czas [s]")
plt.ylabel("Prędkość chwilowa [m/s]")
plt.title("Zależność prędkości od czasu")

plt.show()
