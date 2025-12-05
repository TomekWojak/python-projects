def pokazWspolneWartosci(arr1: list | tuple | set, arr2: list | tuple | set):
    wspolneWartosci = set(arr1) & set(arr2)
    return wspolneWartosci

print(pokazWspolneWartosci([1,2,3],[1,3,5]))