"""
1. Напишіть програму для перетворення висоти
(вказується окремо у футах (1 фут = 30,48 см) і дюймах (1 дюйм = 2,54 см)
у сантиметри. Приклад вхідних данних: feet = 10 inches = 5.
Вихідні данні просто число, або print(your_answer + "cm") це
виведе вашу відповідь у строковому форматі і в кінець додасть cm.

def height_to_cm(feet, inches):
    feet_to_cm = feet * 30.48
    inches_to_cm = inches * 2.54
    total_cm = feet_to_cm + inches_to_cm
    return total_cm

# Запит введення висоти від користувача
feet = int(input("Введіть кількість футів: "))
inches = int(input("Введіть кількість дюймів: "))

height_cm = height_to_cm(feet, inches)
print(str(height_cm) + "cm")
"""

"""
2. Напишіть програму сумування перших n натуральних чисел. 
Результатом має бути ціле число. Де n - ми просто обираємо довільно, 
об'являємо його на початку. Наприклад n_count = 10


n_count = user_input = int(input("Введи ціле натуральне число будь ласка: "))
# Об'являємо значення n


# Обчислення суми перших n натуральних чисел
sum_natural = (n_count * (n_count + 1)) // 2

print("Сума перших", n_count, "натуральних чисел:", sum_natural)
"""

"""
3. У вас є список list_of_values = [10, 5, 12, 25, 13, 6, 4, 22, 106, 94, 46] 
Виведіть всі елементи, результат ділення на 4, яких буде більше 5. 
Легенькі задачки. Щоб трішки пощупати руками те про що ми говорили
"""

list_of_values = [10, 5, 12, 25, 13, 6, 4, 22, 106, 94, 46]

for value in list_of_values:
    if value / 4 >= 5:
        print(value, 'good boy. How did you know?')
    elif value / 4 < 5:
        print(value, 'це капелюх')
    else:
        print('івф')
        ddssssss