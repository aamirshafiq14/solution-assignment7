name = input('Enter your name: ')
numbers = []
for number in range (3):
    number = int(input(f'Enter your favorite number: '))
    numbers.append(number)
print(f"\nHello {name.title()}, let's explore your favorite numbers.\n")
for number in numbers:
    if number % 2 == 0:
        print(f'The number {number} is even.')
    else:
        print(f'The number {number} is odd.')
for number in numbers:
    print(f"The number {number} and it's square is, {number**2}.")
numbers_sum = sum(numbers)
print(f"\nGreat! The sum of your favorite numbers is {numbers_sum}.\n")
from sympy import isprime
if isprime(numbers_sum):
    print(f'The {numbers_sum} is a prime number.')
else:
    print(f'The number {numbers_sum} is not a prime number.')