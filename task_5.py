import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def generate_color(index, total_steps):
    """Генерує колір, який поступово змінюється від темного до світлого."""
    intensity = hex(int(50 + (205 * index / total_steps)))[2:].zfill(2)
    return f"#{intensity}96F0"  # Відтінок блакитного кольору, що змінюється від темного до світлого

def color_nodes_dfs(root, tree, total_steps):
    stack = [root]
    step = 0

    while stack:
        node = stack.pop()
        if node:
            # Змінюємо колір вузла залежно від порядку відвідування
            node.color = generate_color(step, total_steps)
            tree.nodes[node.id]['color'] = node.color
            step += 1
            
            # Додаємо дітей у стек для обходу в глибину (правий спершу, щоб лівий був на вершині)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def color_nodes_bfs(root, tree, total_steps):
    queue = deque([root])
    step = 0

    while queue:
        node = queue.popleft()
        if node:
            # Змінюємо колір вузла залежно від порядку відвідування
            node.color = generate_color(step, total_steps)
            tree.nodes[node.id]['color'] = node.color
            step += 1
            
            # Додаємо дітей у чергу для обходу в ширину
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def draw_final_tree(tree, pos, labels):
    plt.ion()  # Увімкнути інтерактивний режим
    final_colors = [tree.nodes[node]['color'] for node in tree.nodes]
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, node_color=final_colors, node_size=2500, with_labels=True)
    plt.ioff()  # Вимкнути інтерактивний режим після відображення
    plt.show()  # Відобразити фінальний стан графіка

# Створення дерева
root = Node(10)
root.left = Node(15)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(100)
root.right.right = Node(40)

# Візуалізація
tree = nx.DiGraph()
pos = {root.id: (0, 0)}
tree = add_edges(tree, root, pos)

# Отримуємо мітки вузлів
labels = {node: tree.nodes[node]['label'] for node in tree.nodes}

# Вибір методу обходу
total_steps = len(tree.nodes)
# Виконуємо обхід у глибину (DFS) або обхід у ширину (BFS)
# print("Візуалізація обходу в глибину (DFS):")
# color_nodes_dfs(root, tree, total_steps)  # Для обходу в глибину (DFS)

# Або для обходу в ширину (BFS):
print("Візуалізація обходу в ширину (BFS):")
color_nodes_bfs(root, tree, total_steps)

# Відображення фінального графіка
draw_final_tree(tree, pos, labels)
