moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
moja_druga_lista = [23,24,25,26]

moja_lista.append(22)
print(moja_lista) # [1, 17, 3, 5, 3, 4, 86, 90, 2, 21, 22]

moja_lista.insert(1, 2)
print(moja_lista) # [1, 2, 17, 3, 5, 3, 4, 86, 90, 2, 21, 22]

moja_lista.extend(moja_druga_lista)
print(moja_lista) # [1, 2, 17, 3, 5, 3, 4, 86, 90, 2, 21, 22, 23, 24, 25, 26]

moja_lista.remove(17)
print(moja_lista) # [1, 2, 3, 5, 3, 4, 86, 90, 2, 21, 22, 23, 24, 25, 26]

moja_lista.pop()
print(moja_lista) # [1, 2, 3, 5, 3, 4, 86, 90, 2, 21, 22, 23, 24, 25]

print(moja_lista[4]) # 3
print(moja_lista[0:10:2]) # [1, 3, 3, 86, 2]

moja_lista.sort()
print(moja_lista) # [1, 2, 2, 3, 3, 4, 5, 21, 22, 23, 24, 25, 86, 90]

moja_lista.reverse()
print(moja_lista) # [90, 86, 25, 24, 23, 22, 21, 5, 4, 3, 3, 2, 2, 1]

print(len(moja_lista)) # 14
print(max(moja_lista)) # 90
print(min(moja_lista)) # 1
print(sum(moja_lista)) # 311
print(moja_lista + moja_druga_lista) # [90, 86, 25, 24, 23, 22, 21, 5, 4, 3, 3, 2, 2, 1, 23, 24, 25, 26]
print(moja_lista * 5) # [90, 86, 25, 24, 23, 22, 21, 5, 4, 3, 3, 2, 2, 1, 90, 86, 25, 24, 23, 22, 21, 5, 4, 3, 3, 2, 2, 1, 90, 86, 25, 24, 23, 22, 21, 5, 4, 3, 3, 2, 2, 1, 90, 86, 25, 24, 23, 22, 21, 5, 4, 3, 3, 2, 2, 1, 90, 86, 25, 24, 23, 22, 21, 5, 4, 3, 3, 2, 2, 1]
