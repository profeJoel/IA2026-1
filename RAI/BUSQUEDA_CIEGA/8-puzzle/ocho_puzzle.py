import math
from nodo import nodo_estado
from collections import deque
import sys
sys.setrecursionlimit(500000)

#def ordenar_por_heuristica(e):
#    return e.get_distancia()

class ocho_puzzle:

    estado_final = [nodo_estado("12345678H", None, "Final", None)]

    def __init__(self, EI):
        self.estado_inicial = nodo_estado(EI, None, "Inicial", 0)
        #self.calcular_heuristica(self.estado_inicial)
        self.estado_actual = None
        self.descubiertos = []
        self.por_explorar = deque()

    def es_final(self):
        return self.estado_actual in self.estado_final

    def esta_descubierto(self, e):
        return e in self.descubiertos

    def mostrar_estado_actual(self):
        print("Estado Actual")
        print(f"[{self.estado_actual.get_nivel()}]")
        print(self.estado_actual.get_valor()[:3] + "\n" + self.estado_actual.get_valor()[3:6] +"\n"+ self.estado_actual.get_valor()[6:] + "\n")

    
    def mostrar_estado(self, e):
        print("Estado:")
        print(f"[{e.get_nivel()}]")
        print(e.get_valor()[:3] + "\n" + e.get_valor()[3:6] +"\n"+ e.get_valor()[6:] + "\n")

    def mover_a(self, direccion):
        #encontrar el espacio vacío
        posicion_espacio = self.estado_actual.get_valor().find("H")

        # Up
        if direccion == "UP":
            if posicion_espacio < 3:
                return "illegal"
            else:
                # nueva posicion del estación en -3 que se refiere a la posicion de arrriba en el string
                aux = self.estado_actual.get_valor()[posicion_espacio-3]
        # Down

        if direccion == "DOWN":
            if posicion_espacio > 5:
                return "illegal"
            else:
                # nueva posicion del estación en +3 que se refiere a la posicion de abajo en el string
                aux = self.estado_actual.get_valor()[posicion_espacio+3]

        # Left

        if direccion == "LEFT":
            if posicion_espacio in [0,3,6]:
                return "illegal"
            else:
                # nueva posicion del estación en -1 que se refiere a la posicion de izquierda en el string
                aux = self.estado_actual.get_valor()[posicion_espacio-1]

        # Right

        if direccion == "RIGHT":
            if posicion_espacio in [2,5,8]:
                return "illegal"
            else:
                # nueva posicion del estación en +1 que se refiere a la posicion de derecha en el string
                aux = self.estado_actual.get_valor()[posicion_espacio+1]
        
        # Hacer el intercambio entre posiciones
        nuevo_estado = self.estado_actual.get_valor().replace("H","#")
        nuevo_estado = nuevo_estado.replace(aux, "H")
        nuevo_estado = nuevo_estado.replace("#", aux)
        # tenemos el string del nuevo estado
        return nuevo_estado

    def buscar_padres(self, e):
        if e.get_padre() == None:
            print(f"\n{e.get_accion()}: Nivel {e.get_nivel()}")
            self.mostrar_estado(e)
        else:
            self.buscar_padres(e.get_padre())
            print(f"\n{e.get_accion()}: Nivel {e.get_nivel()}")
            self.mostrar_estado(e)

    def algoritmo_anchura(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        self.descubiertos.append(self.estado_actual)
        movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]

        while not self.es_final():
            print(f"Iteración : {iteracion}\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover_a(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not estado_temporal.get_valor() == "illegal" and not self.esta_descubierto(estado_temporal):
                    self.descubiertos.append(estado_temporal)
                    self.por_explorar.append(estado_temporal)
                
            print(f"Elementos Descubiertos: {len(self.descubiertos)}\n")
            print(f"Elementos Por Explorar: {len(self.por_explorar)}\n")

            #Paso al siguiente estado
            self.estado_actual = self.por_explorar.popleft()

            iteracion += 1

        # Mostrar el último estado explorado
        print(f"Iteración : {iteracion}\n")
        self.mostrar_estado_actual()

        # Mostrar la Solucion
        self.buscar_padres(self.estado_actual)
        print("\nResumen Algoritmo por Anchura\n")
        print(f"Elementos Descubiertos: {len(self.descubiertos)}\n")
        print(f"Elementos Por Explorar: {len(self.por_explorar)}\n")
        print(f"Iteración : {iteracion}\n")
    
    def add_profundidad(self, s):
        while s.__len__() > 0:
            e = s.pop()
            self.descubiertos.append(e)
            self.por_explorar.appendleft(e)

    def algoritmo_profundidad(self):
        iteracion = 1
        self.estado_actual = self.estado_inicial
        self.descubiertos.append(self.estado_actual)
        #movimientos = ["UP", "DOWN", "LEFT", "RIGHT"]
        #movimientos = ["DOWN", "RIGHT", "UP", "LEFT"]
        movimientos = ["DOWN","UP", "RIGHT","LEFT"]

        sucesores = deque()

        while not self.es_final():
            print(f"Iteración : {iteracion}\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover_a(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not estado_temporal.get_valor() == "illegal" and not self.esta_descubierto(estado_temporal):
                    sucesores.append(estado_temporal)
                
            # Paso de intercambio para quedar al frente de la cola
            self.add_profundidad(sucesores)
                
            print(f"Elementos Descubiertos: {len(self.descubiertos)}\n")
            print(f"Elementos Por Explorar: {len(self.por_explorar)}\n")

            #Paso al siguiente estado
            self.estado_actual = self.por_explorar.popleft()

            iteracion += 1

        # Mostrar el último estado explorado
        print(f"Iteración : {iteracion}\n")
        self.mostrar_estado_actual()

        # Mostrar la Solucion
        self.buscar_padres(self.estado_actual)
        print("\nResumen Algoritmo por Profundidad\n")
        print(f"Elementos Descubiertos: {len(self.descubiertos)}\n")
        print(f"Elementos Por Explorar: {len(self.por_explorar)}\n")
        print(f"Iteración : {iteracion}\n")
