import networkx as nx
import matplotlib.pyplot as plt

class Componente:
    def __init__(self, id, nombre, tipo, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio

    def __repr__(self):
        return f"{self.nombre} (ID: {self.id}, Tipo: {self.tipo}, Cantidad: {self.cantidad}, Precio: ${self.precio})"

def dibujar_cadena_suministro():
    # Crear un grafo dirigido para simular la cadena de suministro en blockchain
    G = nx.DiGraph()

    # Crear un componente como nodo raíz
    componente = Componente('001', 'Componente A', 'Electrónico', 100, 120.00)
    
    # Agregar el nodo del componente
    G.add_node(componente, subset=0)

    # Definir los actores de la cadena con descripciones
    actores = {
        "Proveedor": "Proporciona materias primas.",
        "Fabricante": "Procesa materias y produce componentes.",
        "Distribuidor": "Distribuye componentes a diversas ubicaciones.",
        "Minorista": "Vende componentes al consumidor final.",
        "Consumidor": "Adquiere y usa el componente final."
    }

    # Agregar nodos de actores y describir flujos (edges)
    posiciones = {'Proveedor': (0, 0), 'Fabricante': (1, 0), 'Distribuidor': (2, 0),
                  'Minorista': (3, 0), 'Consumidor': (4, 0)}
    posiciones[componente] = (2, 1)  # Posición del componente en el gráfico
    
    for actor, descripcion in actores.items():
        G.add_node(actor, description=descripcion)
        G.add_edge(componente, actor, transaction="Envío de información y verificación de autenticidad.")

    # Dibujar el grafo
    pos = {**posiciones, componente: (2, 1)}
    labels = {node: node if isinstance(node, Componente) else f"{node}\n{G.nodes[node]['description']}" for node in G.nodes}
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=3500, node_color='skyblue', edge_color='k')
    edge_labels = nx.get_edge_attributes(G, 'transaction')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green')

    plt.title("Simulación de Cadena de Suministro en Blockchain")
    plt.show()

# Ejecutar la función para visualizar la cadena
dibujar_cadena_suministro()
