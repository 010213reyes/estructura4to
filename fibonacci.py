# Define una función llamada 'fibonacci' que toma un argumento 'n'.
def fibonacci(n):
    # Si 'n' es menor o igual a 0, la función devuelve un mensaje de error.
    if n <= 0:
        return "El número debe ser mayor que 0"
    # Si 'n' es 1, la función devuelve 0, que es el primer término de la serie de Fibonacci.
    elif n == 1:
        return 0
    # Si 'n' es 2, la función devuelve 1, que es el segundo término de la serie de Fibonacci.
    elif n == 2:
        return 1
    # Si 'n' es mayor que 2, la función se llama a sí misma dos veces: una para 'n-1' y otra para 'n-2'.
    # Luego suma estos dos resultados para obtener el n-ésimo término de la serie de Fibonacci.
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejemplo de uso de la función:
# La función 'fibonacci' se llama con 'n' igual a 10, por lo que calcula el décimo término de la serie de Fibonacci.
# Luego, este término se imprime en la consola.
print(fibonacci(2))
print(fibonacci(4))
print(fibonacci(6))
print(fibonacci(10))


