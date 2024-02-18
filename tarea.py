# Define la clase Node
class Node:
    # El constructor de la clase Node
    def __init__(self, val = None):
        ''' Inicializador '''
        # Cada nodo tiene un valor y un puntero al siguiente nodo
        self.val = val
        self.next = None

# Define la clase CircularLinkedList
class CircularLinkedList:
    # El constructor de la clase CircularLinkedList
    def __init__(self) -> None:
        ''' Inicializador '''  
        # Inicializa la cabeza de la lista como None
        self.head:Node|None = None

    # Método para insertar un nodo al inicio de la lista
    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        # Crea un nuevo nodo
        new_node = Node(val)
        # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            # Si no, recorre la lista hasta el último nodo
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            # Inserta el nuevo nodo al inicio de la lista
            last_node.next = new_node
            new_node.next = self.head
            self.head = new_node

    # Método para insertar un nodo al final de la lista
    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        # Crea un nuevo nodo
        new_node = Node(val)
        # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            # Si no, recorre la lista hasta el último nodo
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            # Inserta el nuevo nodo al final de la lista
            last_node.next = new_node
            new_node.next = self.head

    # Método para eliminar un nodo al inicio de la lista
    def headRemove(self) -> None:
        ''' Remover el elemento al inicio de la lista '''
        # Si la lista está vacía, no hace nada
        if self.head is None:
            return
        else:
            # Si no, recorre la lista hasta el último nodo
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next
            # Elimina el nodo al inicio de la lista
            last_node.next = self.head.next
            self.head = self.head.next

    # Método para recorrer la lista e imprimir los valores de los nodos
    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
        # Si la lista está vacía, no hace nada
        if self.head is None:
            return
        else:
            # Si no, recorre la lista e imprime los valores de los nodos
            current_node = self.head
            while True:
                print(current_node.val)
                current_node = current_node.next
                if current_node == self.head:
                    break

# La parte principal del programa
if __name__ == '__main__':
    # Crea una instancia de CircularLinkedList
    lista_circular = CircularLinkedList()

    # Genera casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

    # Llena la lista con los valores de la lista_tradicional
    for elemento in lista_tradicional:
        lista_circular.tailInsert(elemento)

    # Imprime la lista
    lista_circular.traverse()

    # Añade un nuevo elemento al final de la lista
    n = False
    lista_circular.tailInsert(n)

    # Añade un nuevo elemento al inicio de la lista
    n = 'Estructuras'
    lista_circular.headInsert(n)

    # Elimina el primer elemento de la lista
    lista_circular.headRemove()
    # Imprime la lista de nuevo
    lista_circular.traverse()
