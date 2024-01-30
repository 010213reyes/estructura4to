def ordenamiento_por_seleccion(lista):
    n = len(lista)
    for i in range(n):
        maximo_actual = i
        for j in range(i+1, n):
            if lista[j] > lista[maximo_actual]:
                maximo_actual = j
        lista[i], lista[maximo_actual] = lista[maximo_actual], lista[i]
    return lista
