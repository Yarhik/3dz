def знайти_мінімальну_кількість_монет(сума):
    # Створимо масив для зберігання мінімальної кількості монет для кожної суми від 0 до сума.
    мін_кількість_монет = [float('inf')] * (сума + 1)
    
    # Базовий випадок: для суми 0 мінімальна кількість монет завжди дорівнює 0.
    мін_кількість_монет[0] = 0
    
    # Цикл для обчислення мінімальної кількості монет для кожної суми від 1 до сума.
    for поточна_сума in range(1, сума + 1):
        # Перебираємо всі доступні номінали монет.
        for номінал in [6, 3]:
            if поточна_сума >= номінал:
                # Оновлюємо мінімальну кількість монет для поточної суми,
                # якщо можна скористатися монетою номіналом 'номінал'.
                мін_кількість_монет[поточна_сума] = min(
                    мін_кількість_монет[поточна_сума],
                    мін_кількість_монет[поточна_сума - номінал] + 1
                )
    
    # Повертаємо мінімальну кількість монет для заданої суми.
    return мін_кількість_монет[сума]

# Сума, яку потрібно отримати
сума = 43

# Знайти мінімальну кількість монет для заданої суми
мін_кількість = знайти_мінімальну_кількість_монет(сума)

print(f"Мінімальна кількість монет для суми {сума} дорівнює {мін_кількість}.")
