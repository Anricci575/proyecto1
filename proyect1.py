class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def eliminar_nodo(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                return
            actual = actual.siguiente

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaDoblementeEnlazada()
lista.insertar_al_final(1)
lista.insertar_al_final(2)
lista.insertar_al_final(3)
lista.mostrar_lista()  # Salida: 1 <-> 2 <-> 3 <-> None
lista.eliminar_nodo(2)
lista.mostrar_lista()  # Salida: 1 <-> 3 <-> None