import random
import pandas as pd
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_simulations=100000):
    # Словник для підрахунку появи кожної суми
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Імітація кидання двох кубиків
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_count[dice_sum] += 1
    
    # Обчислення ймовірностей
    probabilities = {sum_value: (count / num_simulations) * 100 for sum_value, count in sums_count.items()}
    
    # Конвертація результатів у DataFrame для зручності
    results_df = pd.DataFrame(list(probabilities.items()), columns=["Сума", "Ймовірність (%)"])
    
    return results_df

# Кількість симуляцій
num_simulations = 1000
results_df = monte_carlo_simulation(num_simulations)

# Виведення таблиці ймовірностей
print("Ймовірність кожної суми при киданні двох кубиків:")
print(results_df)

# Візуалізація результатів
plt.figure(figsize=(10, 6))
plt.bar(results_df["Сума"], results_df["Ймовірність (%)"], color="skyblue")
plt.xlabel("Сума")
plt.ylabel("Ймовірність (%)")
plt.title(f"Ймовірності сум при киданні двох кубиків (симуляція Монте-Карло, {num_simulations} ітерацій)")
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
