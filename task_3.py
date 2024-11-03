import heapq

def dijkstra(graph, start):
    # Ініціалізуємо відстані до всіх вершин як нескінченність
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0  # Відстань до початкової вершини дорівнює 0
    priority_queue = [(0, start)]  # (відстань, вершина)
    
    while priority_queue:
        # Вибираємо вершину з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо поточна відстань більше, ніж збережена, пропускаємо обробку
        if current_distance > distances[current_vertex]:
            continue
        
        # Перевіряємо сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Якщо знайдено коротший шлях до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад графа у вигляді словника
# Кожна вершина пов'язана зі своїми сусідами та вагами ребер
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Запуск алгоритму Дейкстри з початкової вершини 'A'
start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

# Виведення найкоротших шляхів
print(f"Найкоротші відстані від вершини '{start_vertex}':")
for vertex, distance in distances.items():
    print(f"Відстань до {vertex}: {distance}")
