import networkx as nx
import matplotlib.pyplot as plt

def dibujar_grafo_cadena_suministro():
    # Crear un grafo dirigido para representar la cadena de suministro
    G = nx.DiGraph()

    # Agregar nodos con roles en la cadena de suministro
    nodos = ["Proveedor", "Fabricante", "Distribuidor", "Minorista", "Consumidor"]
    G.add_nodes_from(nodos)

    # Conectar los nodos para mostrar el flujo de la cadena de suministro
    aristas = [("Proveedor", "Fabricante"), ("Fabricante", "Distribuidor"),
               ("Distribuidor", "Minorista"), ("Minorista", "Consumidor")]
    G.add_edges_from(aristas)

    # Configurar la disposición de los nodos
    pos = nx.spring_layout(G)

    # Dibujar el grafo
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=4000, edge_color='k', linewidths=1, font_size=15)
    
    # Mostrar el gráfico
    plt.show()

# Llamar a la función para dibujar el grafo
dibujar_grafo_cadena_suministro()


def dibujar_grafo_cadena_suministro_avanzado():
    # Crear un grafo dirigido para representar la cadena de suministro
    G = nx.DiGraph()

    # Agregar nodos con atributos adicionales
    nodos = [("Proveedor", {"capacidad": 1000}),
             ("Fabricante", {"capacidad": 500}),
             ("Distribuidor", {"capacidad": 700}),
             ("Minorista", {"capacidad": 300}),
             ("Consumidor", {"capacidad": 10})]
    G.add_nodes_from(nodos)

    # Conectar los nodos mostrando atributos adicionales como el tiempo de entrega
    aristas = [("Proveedor", "Fabricante", {"tiempo": 2}),
               ("Fabricante", "Distribuidor", {"tiempo": 1}),
               ("Distribuidor", "Minorista", {"tiempo": 1}),
               ("Minorista", "Consumidor", {"tiempo": 1})]
    G.add_edges_from(aristas)

    # Configurar la disposición de los nodos y tamaños basados en la capacidad
    pos = nx.spring_layout(G)
    tamaños = [G.nodes[nodo]['capacidad'] * 10 for nodo in G.nodes]

    # Dibujar el grafo con tamaños y etiquetas personalizadas para las aristas
    nx.draw(G, pos, with_labels=True, node_size=tamaños, node_color='lightblue', edge_color='k', linewidths=1, font_size=15)
    etiquetas_aristas = nx.get_edge_attributes(G, 'tiempo')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas_aristas)

    # Mostrar el gráfico
    plt.show()

# Llamar a la función para dibujar el grafo avanzado
dibujar_grafo_cadena_suministro_avanzado()
