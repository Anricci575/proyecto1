class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, dato):
        nuevo_nodo = NodoCircular(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def mostrar_lista(self):
        if not self.cabeza:
            return
        actual = self.cabeza
        while True:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("(vuelve al inicio)")

# Ejemplo de uso
lista_circular = ListaCircular()
lista_circular.insertar_al_final(10)
lista_circular.insertar_al_final(20)
lista_circular.insertar_al_final(30)
lista_circular.mostrar_lista()  # Salida: 10 -> 20 -> 30 -> (vuelve al inicio)