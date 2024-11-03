import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_heap_edges(graph, nodes, pos):
    n = len(nodes)
    for i, node in enumerate(nodes):
        if node is not None:
            # Додаємо вузол до графу
            graph.add_node(node.id, color=node.color, label=node.val)
            
            # Лівий дочірній вузол
            left_index = 2 * i + 1
            if left_index < n and nodes[left_index] is not None:
                graph.add_edge(node.id, nodes[left_index].id)
                pos[nodes[left_index].id] = (pos[node.id][0] - 1 / 2 ** (i + 1), pos[node.id][1] - 1)
            
            # Правий дочірній вузол
            right_index = 2 * i + 2
            if right_index < n and nodes[right_index] is not None:
                graph.add_edge(node.id, nodes[right_index].id)
                pos[nodes[right_index].id] = (pos[node.id][0] + 1 / 2 ** (i + 1), pos[node.id][1] - 1)
    return graph

def draw_heap(heap):
    tree = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}  # Позиція кореня
    tree = add_heap_edges(tree, heap, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення бінарної купи
heap = [
    Node(10),  # Корінь
    Node(15),
    Node(30),
    Node(40),
    Node(50),
    Node(100),
    Node(40)
]

# Відображення бінарної купи
draw_heap(heap)
