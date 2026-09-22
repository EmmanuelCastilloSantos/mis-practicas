calificaciones = [8.5, 9.0, 6.0, 10.0, 7.5, 5.0, 9.5, 8.0, 7.0, 6.5, 10.0, 4.0, 8.5, 9.0, 7.0]

lista_asc = calificaciones
n = len(lista_asc)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if lista_asc[j] > lista_asc[j + 1]:
            lista_asc[j], lista_asc[j + 1] = lista_asc[j + 1], lista_asc[j]
            swapped = True
    if not swapped:
        break
#> ascendente
print("Orden Ascendente:", lista_asc)

lista_desc = calificaciones
n = len(lista_desc)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if lista_desc[j] < lista_desc[j + 1]:
            lista_desc[j], lista_desc[j + 1] = lista_desc[j + 1], lista_desc[j]
            swapped = True
    if not swapped:
        break
#< descendente
print("Orden Descendente:", lista_desc)