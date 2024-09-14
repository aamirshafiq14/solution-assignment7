# Python Code for Numbers Exploration Tool

This Python script asks for the user's name and favorite numbers, then performs various operations such as checking for even/odd numbers, calculating squares, and summing the numbers. It also checks if the sum is a prime number using the `sympy` library.

## Name Input

```python
name = input('Enter your name: ')
```

## Favorite Numbers Input

```python
numbers = []
for number in range (3):
    number = int(input(f'Enter your favorite number: '))
    numbers.append(number)
print(f"\nHello {name.title()}, let's explore your favorite numbers.\n")
```

## Exploring numbers if they are Even or Odd

```python
for number in numbers:
    if number % 2 == 0:
        print(f'The number {number} is even.')
    else:
        print(f'The number {number} is odd.')
```

## Getting Numbers, their Squares & Sum

```python
for number in numbers:
    print(f"The number {number} and it's square is, {number**2}.")
numbers_sum = sum(numbers)
print(f"\nGreat! The sum of your favorite numbers is {numbers_sum}.\n")
```

## Checking If the Sum is Prime or not

```python
from sympy import isprime
if isprime(numbers_sum):
print(f'The {numbers_sum} is a prime number.')
else:
print(f'The number {numbers_sum} is not a prime number.')

```

## Output of Number Exploration Tool

```python
![Output of Number Exploration Tool](./Output%20of%20No.%20Exploration%20Tool.png)
```
