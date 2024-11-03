# Вихідні дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості в порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    chosen_items = {}

    for name, info in sorted_items:
        if budget >= info["cost"]:
            max_quantity = budget // info["cost"]
            chosen_items[name] = max_quantity
            total_calories += max_quantity * info["calories"]
            budget -= max_quantity * info["cost"]
    
    return chosen_items, total_calories

def dynamic_programming(items, budget):
    # Створюємо таблицю для зберігання максимальних калорій для різних бюджетів
    n = len(items)
    item_names = list(items.keys())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        
        for b in range(budget + 1):
            # Якщо ми не беремо цей предмет
            dp[i][b] = dp[i - 1][b]
            # Якщо ми можемо взяти цей предмет і отримати більше калорій
            if cost <= b:
                dp[i][b] = max(dp[i][b], dp[i][b - cost] + calories)
    
    # Відновлюємо оптимальний набір страв
    total_calories = dp[n][budget]
    chosen_items = {}
    b = budget
    
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:  # Якщо поточний предмет був обраний
            name = item_names[i - 1]
            cost = items[name]["cost"]
            calories = items[name]["calories"]
            quantity = 0
            
            # Визначаємо максимальну кількість цього предмета, яку ми можемо додати
            while b >= cost and dp[i][b] == dp[i][b - cost] + calories:
                b -= cost
                quantity += 1
            
            chosen_items[name] = quantity

    return chosen_items, total_calories

# Отримуємо бюджет від користувача
budget = int(input("Введіть бюджет: "))

# Виклик алгоритмів
print("Жадібний алгоритм:")
chosen_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Вибрані страви:", chosen_items_greedy)
print("Загальна калорійність:", total_calories_greedy)

print("Динамічне програмування:")
chosen_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Вибрані страви:", chosen_items_dp)
print("Загальна калорійність:", total_calories_dp)
