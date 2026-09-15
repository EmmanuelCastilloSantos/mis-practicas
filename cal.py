# 1. Creación de un arreglo (lista)
numeros = [10, 25, 30, 45, 50]

# 2. Acceso a elementos por su índice (inicia en 0)
print("Primer elemento:", numeros[0])
print("Último elemento:", numeros[-1])

# 3. Modificación de un elemento
numeros[2] = 99  # Cambia el 30 por 99

# 4. Agregar elementos
numeros.append(60)       # Agrega 60 al final
numeros.insert(1, 15)    # Inserta 15 en el índice 1

# 5. Eliminar elementos
numeros.remove(45)       # Elimina la primera aparición de 45
ultimo = numeros.pop()   # Elimina y retorna el último elemento

# 6. Recorrer el arreglo con un bucle
print("\nElementos actuales del arreglo:")
for num in numeros:
    print(f"- {num}")

# 7. Operaciones comunes
print("\nCantidad de elementos:", len(numeros))
print("Suma total:", sum(numeros))
print("Valor máximo:", max(numeros))
#Resultado del análisis
Análisis breve de complejidad (tiempo y espacio) 

- Creación y modificaciones básicas 
  - Crear la lista y operaciones de acceso, modificación, inserción y eliminación en posiciones específicas: 
    - Acceso por índice: O(1) 
    - Modificación por índice: O(1) 
    - append: amortizado O(1) 
    - insert en posición arbitraria: O(n) en el peor caso (debido a desplazamientos) 
    - remove/ pop (sin índice): O(n) en el peor caso para el elemento; pop() al final es O(1) 
- Recorrido con bucle 
  - Recorrer todos los elementos una vez: O(n) tiempo 
- Operaciones agregadas 
  - len(numeros): O(1) 
  - sum(numeros): O(n) 
  - max(numeros): O(n) 

Espacio 
- Espacio adicional: O(n) para almacenar la lista y sus elementos; operaciones que crean temporales son O(1) aparte de la entrada/salida de la lista.