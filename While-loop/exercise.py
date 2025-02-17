# 1. Print numbers from 1 to 10
# Task: Use a while loop to print numbers from 1 to 10.
from unicodedata import digit

print("Task 1: Print numbers from 1 to 10")
i = 1
while i <= 10:
    print(i)
    i += 1



# 2. Sum of the first 10 natural numbers
# Task: Calculate the sum of numbers from 1 to 10 using a while loop.


print("Task 2: Sum of the first 10 natural numbers")

sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1

print("Sum:", sum)  # Replace ... with the result



# 3. Print even numbers from 1 to 20
# Task: Use a while loop to print only even numbers from 1 to 20.


print("Task 3: Print even numbers from 1 to 20")
i = 2
while i <=20:
    print(i)
    i +=2

# 4. Reverse countdown from 10 to 1
# Task: Print numbers in reverse order: 10, 9, ..., 1.
print("Task 4: Countdown from 10 to 1")
i = 10
while i >= 1:
    print(i)
    i -= 1

# 5. Multiplication table (user input)
# Task: Ask the user for a number and print its multiplication table up to 10.


print("Task 5: Multiplication Table")
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f'{num} * {i} = {num * i}')
    i += 1



# 6. "Guess the Number" game
# Task: The program picks a number, and the user keeps guessing until they get it right.



print("Task 6: Guess the Number Game")
print("Task 6: Guess the Number Game")
import random
# Исправлено название переменной
secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f'Congratulations! You guessed the number in {attempts} attempts.')
        break





# 7. Print the digits of a number in reverse order
# Task: Given the number 12345, print its digits one by one in reverse order.



print("Task 7: Print digits of a number in reverse order")
num = 12345
i = 1

while num > 0:
    digit = num % 10
    print(digit)
    num = num // 10


# 8. Count the number of digits in a number
# Task: Find out how many digits are in the number 98765.


print("Task 8: Count the number of digits")
num = 98765
count = 0
while num > 0:
    num = num // 10
    count += 1
print(f'The number has {count} digits.')




# 9. Find the factorial of a number
# Task: Compute the factorial of 5 using a while loop.


print("Task 9: Factorial of a number")
num = 5
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print(f'The factorial of {num} is {fact}')


# 10. Print the first 10 Fibonacci numbers
# Task: Print the first 10 numbers in the Fibonacci sequence (0, 1, 1, 2, 3, 5...).


print("Task 10: Fibonacci Series (First 10 numbers)")

''''Шаги выполнения:
Переменные:

n = 10 — мы хотим вывести 10 чисел Фибоначчи.
a, b = 0, 1 — это первые два числа в последовательности Фибоначчи (0 и 1). Эти переменные будут хранить два числа,
 которые нам нужны для вычислений в каждой итерации.
count = 0 — это счётчик, который будет отслеживать, сколько чисел Фибоначчи уже выведено. Мы хотим вывести 10 чисел,
 поэтому он будет увеличиваться на 1 с каждой итерацией.
Цикл while:

Мы начинаем цикл while, который будет выполняться, пока count не станет равным 10 (то есть пока не выведем 10 чисел).
Условие while count < n: означает, что цикл будет работать до тех пор, пока count меньше 10.
Внутри цикла:

print(a, end=" ") — выводит текущее значение переменной a (первое число в последовательности на текущей итерации)
 и добавляет пробел между числами, а не новую строку.
a, b = b, a + b — вот здесь происходит самое важное:
Сначала a получает значение переменной b (то есть, текущее второе число последовательности).
b получает значение a + b (сумма текущих двух чисел, то есть следующее число последовательности).
Таким образом, на каждой итерации a и b обновляются, и в следующий раз мы будем работать с новыми значениями.
Увеличиваем счётчик:

count += 1 — после каждой итерации увеличиваем счётчик count на 1, чтобы отслеживать количество выведенных чисел.
Пример работы:

На первой итерации:
a = 0, b = 1 — выводим 0, обновляем a и b:
a, b = b, a + b → a = 1, b = 1.
На второй итерации:
a = 1, b = 1 — выводим 1, обновляем a и b:
a, b = b, a + b → a = 1, b = 2.
На третьей итерации:
a = 1, b = 2 — выводим 1, обновляем a и b:
a, b = b, a + b → a = 2, b = 3.
И так далее, пока не выведем 10 чисел.'''


fib_num = 10 # Количество чисел Фибоначчи
a,b = 0,1 # Первые два числа последовательности

count = 0

while count < fib_num:
    print(a, end=' ')
    a,b  = b,a + b
    count +=1


