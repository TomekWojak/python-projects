def odwrocString(str):
    tekstJakoLista = list(str)
    tekstJakoLista.reverse()

    stringOdwrocony = "".join(tekstJakoLista)

    return  stringOdwrocony





print(odwrocString('Hello World'))