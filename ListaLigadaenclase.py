# Definición de la clase Node
class Node:
    def __init__(self, val = None):
        ''' Inicializador '''
        # Cada nodo tiene un valor y un puntero al siguiente nodo
        self.val = val
        self.next = None

# Definición de la clase LinkedList
class LinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        # Una lista ligada tiene un contador de nodos, y punteros al primer y último nodo
        self.counter:int = 0
        self.head:Node|None = None
        self.tail:Node|None = None

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        # Crear un nuevo nodo
        new_node = Node(val)
        # El siguiente del nuevo nodo será el antiguo primer nodo
        new_node.next = self.head
        # El nuevo nodo se convierte en el primer nodo
        self.head = new_node
        # Si la lista estaba vacía, el nuevo nodo también es el último nodo
        if self.tail is None:
            self.tail = new_node
        # Incrementar el contador de nodos
        self.counter += 1

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        # Crear un nuevo nodo
        new_node = Node(val)
        # Si la lista está vacía, el nuevo nodo es el primer y último nodo
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            # Si no, el siguiente del antiguo último nodo es el nuevo nodo
            self.tail.next = new_node
            # Y el nuevo nodo se convierte en el último nodo
            self.tail = new_node
        # Incrementar el contador de nodos
        self.counter += 1
    
    def headRemove(self) -> None:
        ''' Remover el elemento al inicio de la lista '''
        # Si la lista está vacía, lanzar un error
        if self.head is None:
            raise ValueError('La lista está vacía')
        # Si no, el primer nodo pasa a ser el siguiente del antiguo primer nodo
        self.head = self.head.next
        # Si la lista queda vacía, también se actualiza el último nodo
        if self.head is None:
            self.tail = None
        # Decrementar el contador de nodos
        self.counter -= 1 

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
        # Comenzar con el primer nodo
        current = self.head
        # Mientras no se llegue al final de la lista
        while current is not None:
            # Imprimir el valor del nodo actual
            print(current.val)
            # Pasar al siguiente nodo
            current = current.next
