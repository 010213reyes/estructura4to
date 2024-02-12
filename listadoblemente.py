# Definición de la clase Nodo
class Nodo:
    # Constructor de la clase Nodo
    def __init__(self, dato):
        self.dato = dato # El valor del nodo
        self.siguiente = None # Referencia al siguiente nodo
        self.anterior = None # Referencia al nodo anterior

# Definición de la clase ListaDoblementeEnlazada
class ListaDoblementeEnlazada:
    # Constructor de la clase ListaDoblementeEnlazada
    def __init__(self):
        self.primero = None # El primer nodo de la lista
        self.ultimo = None # El último nodo de la lista
        self.size = 0 # El tamaño de la lista

    # Método para verificar si la lista está vacía
    def vacia(self): 
        return self.primero == None # Retorna True si la lista está vacía, False en caso contrario
        
    # Método para agregar un nodo al final de la lista
    def agregar_final(self, dato):
        if self.vacia(): # Si la lista está vacía
            self.primero = self.ultimo = Nodo(dato) # El nuevo nodo se convierte en el primero y último nodo de la lista
        else : # Si la lista no está vacía
            aux = self.ultimo # Guarda una referencia al último nodo
            self.ultimo = aux.siguiente = Nodo(dato) # Crea un nuevo nodo y lo enlaza con el último nodo
            self.ultimo.anterior = aux # Enlaza el nuevo nodo con el nodo anterior
        self.size += 1 # Incrementa el tamaño de la lista

    # Método para agregar un nodo al inicio de la lista
    def agregar_inicio(self, dato):
        if self.vacia(): # Si la lista está vacía
            self.primero = self.ultimo = Nodo(dato) # El nuevo nodo se convierte en el primero y último nodo de la lista
        else: # Si la lista no está vacía
            aux = Nodo(dato) # Crea un nuevo nodo
            aux.siguiente = self.primero # Enlaza el nuevo nodo con el primer nodo
            self.primero.anterior = aux # Enlaza el primer nodo con el nuevo nodo
            self.primero = aux # El nuevo nodo se convierte en el primer nodo de la lista
        self.size += 1 # Incrementa el tamaño de la lista

    # Método para recorrer la lista desde el inicio
    def recorrer_inicio(self): 
        aux = self.primero # Comienza por el primer nodo
        while aux: # Mientras el nodo actual no sea nulo
            print(aux.dato) # Imprime el valor del nodo
            aux = aux.siguiente # Avanza al siguiente nodo

    # Método para recorrer la lista desde el final
    def recorrer_final(self):
        aux = self.ultimo # Comienza por el último nodo
        while aux: # Mientras el nodo actual no sea nulo
            print(aux.dato) # Imprime el valor del nodo
            aux = aux.anterior # Retrocede al nodo anterior

    # Método para obtener el tamaño de la lista
    def size(self):
        return self.size # Retorna el tamaño de la lista

    # Método para eliminar el primer nodo de la lista
    def eliminar_inicio(self):
        if self.vacia(): # Si la lista está vacía
            print("Lista vacia ") # Imprime un mensaje
        elif self.primero.siguiente == None: # Si la lista solo tiene un nodo
            self.primero = self.ultimo = None # Elimina el nodo
            self.size = 0 # Actualiza el tamaño de la lista
        else: # Si la lista tiene más de un nodo
            self.primero = self.primero.siguiente # El segundo nodo se convierte en el primer nodo
            self.primero.anterior = None # El primer nodo no tiene nodo anterior
            self.size -= 1 # Decrementa el tamaño de la lista

    # Método para eliminar el último nodo de la lista
    def eliminar_final(self):
        if self.vacia(): # Si la lista está vacía
            print("Listas vacia") # Imprime un mensaje
        elif self.primero.siguiente == None: # Si la lista solo tiene un nodo
            self.primero = self.ultimo = None # Elimina el nodo
            self.size = 0 # Actualiza el tamaño de la lista
        else: # Si la lista tiene más de un nodo
            self.ultimo = self.ultimo.anterior # El penúltimo nodo se convierte en el último nodo
            self.ultimo.siguiente = None # El último nodo no tiene nodo siguiente
            self.size -= 1 # Decrementa el tamaño de la lista

# Función para mostrar un menú interactivo al usuario
def menu():
    lista = ListaDoblementeEnlazada() # Crea una lista doblemente enlazada
    while True: # Bucle infinito
        print("\n1. Agregar al inicio") # Imprime las opciones del menú
        print("2. Agregar al final")
        print("3. Recorrer desde el inicio")
        print("4. Recorrer desde el final")
        print("5. Eliminar desde el inicio")
        print("6. Eliminar desde el final")
        print("7. Salir")

        try: # Intenta ejecutar el siguiente bloque de código
            opcion = int(input("Elige una opción: ")) # Solicita al usuario que elija una opción
            if opcion == 1: # Si el usuario eligió la opción 1
                dato = input("Ingresa el dato a agregar al inicio: ") # Solicita al usuario que ingrese un dato
                lista.agregar_inicio(dato) # Agrega el dato al inicio de la lista
            elif opcion == 2: # Si el usuario eligió la opción 2
                dato = input("Ingresa el dato a agregar al final: ") # Solicita al usuario que ingrese un dato
                lista.agregar_final(dato) # Agrega el dato al final de la lista
            elif opcion == 3: # Si el usuario eligió la opción 3
                lista.recorrer_inicio() # Recorre la lista desde el inicio
            elif opcion == 4: # Si el usuario eligió la opción 4
                lista.recorrer_final() # Recorre la lista desde el final
            elif opcion == 5: # Si el usuario eligió la opción 5
                lista.eliminar_inicio() # Elimina el primer nodo de la lista
            elif opcion == 6: # Si el usuario eligió la opción 6
                lista.eliminar_final() # Elimina el último nodo de la lista
            elif opcion == 7: # Si el usuario eligió la opción 7
                break # Termina el bucle
            else: # Si el usuario eligió una opción no válida
                print("Opción no válida. Por favor, intenta de nuevo.") # Imprime un mensaje
        except ValueError: # Si ocurre un error al intentar convertir la entrada del usuario a un entero
            print("Entrada no válida. Por favor, ingresa un número.") # Imprime un mensaje

menu() # Llama a la función menu

                                  
        