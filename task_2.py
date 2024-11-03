import turtle

# Налаштування екрану та черепашки
screen = turtle.Screen()
screen.title("Фрактал 'Дерево Піфагора'")
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Налаштування черепашки
t = turtle.Turtle()
t.speed(0)  # Максимальна швидкість малювання
t.left(90)  # Початкова орієнтація черепашки вгору
t.color("brown")

# Функція для малювання дерева
def draw_pythagoras_tree(t, branch_length, level, angle=30):
    if level == 0:
        return

    # Малюємо гілку
    t.forward(branch_length)
    
    # Рекурсія для правої гілки
    t.right(angle)
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1, angle)
    
    # Повертаємося до основи і виконуємо рекурсію для лівої гілки
    t.left(2 * angle)
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1, angle)
    
    # Повертаємося до початкової позиції гілки
    t.right(angle)
    t.backward(branch_length)

# Запитуємо у користувача рівень рекурсії
try:
    recursion_level = int(input("Введіть рівень рекурсії для 'дерева Піфагора' (рекомендується від 3 до 10): "))
except ValueError:
    recursion_level = 5  # Встановлюємо рівень за замовчуванням, якщо введення некоректне

# Починаємо малювання дерева
draw_pythagoras_tree(t, 100, recursion_level)

# Завершення програми
turtle.done()
