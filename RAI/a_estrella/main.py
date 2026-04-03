from grafo import grafo
from nodo import nodo
from a_estrella import a_estrella

if __name__ == "__main__":

    #mapa_1 = grafo("archivo_grafo.txt")
    #print(mapa_1)

    #origen = nodo(-3,4, "Origen")
    #destino = nodo(3, -2, "Destino")
    #destino = nodo(-1,-3, "Destino")
    #experimento = a_estrella(origen, destino, "archivo_grafo.txt")

    
    origen = nodo(8, 54, "Origen")
    destino = nodo(22, 32, "Destino")
    experimento = a_estrella(origen, destino, "100nodos-chatgpt.csv")
    print(experimento.tablero)
    experimento.init()