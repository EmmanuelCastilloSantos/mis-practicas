# 1. Creación de un arreglo (lista)
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
