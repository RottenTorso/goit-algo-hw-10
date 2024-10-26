import pulp

# Створення проблеми лінійного програмування
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості вироблених "Лимонаду" та "Фруктового соку"
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Обмеження на ресурси
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
problem += 1 * lemonade <= 50, "Sugar_Constraint"
problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Цільова функція для максимізації загальної кількості вироблених продуктів
problem += lemonade + fruit_juice, "Total_Production"

# Розв'язання задачі
problem.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Lemonade: {pulp.value(lemonade)}")
print(f"Fruit Juice: {pulp.value(fruit_juice)}")