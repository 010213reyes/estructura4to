def bubbleSort(lista):
  n = len(lista) # Obtener el número total de elementos
  for i in range(n-1): # Realizar el ciclo externo
    for j in range(n-i-1): # Realizar el ciclo interno
      if lista[j] > lista[j+1]: # Comparar el elemento actual con el siguiente
        lista[j], lista[j+1] = lista[j+1], lista[j] # Intercambiar sus posiciones
  return lista # Devolver la lista ordenada

# Ejemplo de uso
lista = [21, 6, 9, 33, 3]
lista_ordenada = bubbleSort(lista)
print(lista_ordenada)