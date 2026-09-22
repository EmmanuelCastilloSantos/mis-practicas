lista = [4, 2, 0, 8, 5, 3, 7, 0]

for i in range(len(lista)):
    minimo = i
    for x in range(i,len(lista)):
        if lista[x] < lista[minimo]:
            minimo = x
    aux = lista[i]
    lista[i] = lista[minimo]
    lista[minimo] = aux

print(lista)