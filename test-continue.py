# terms:
# 7
num: int = int(input('Enter a number:'))
save: int = num
sum_digit: int = 0
print(num, ': ', end=' ')
while num > 0:
    ahadot: int = num % 10
    sum_digit += ahadot
    num = num // 10
    print(f'{ahadot}{' + ' if num > 0 else ' '}', end=' ')
print('=', sum_digit)
print()

# 8
num_int: int = int(input('Enter two digit number:'))
ahadot: int = num_int % 10
asarot: int = num_int // 10
new_number: int = ahadot * 10 + asarot * 1
print(new_number)
print()

# 9
number: int = int(input('Enter a number:'))
print('even' if number % 2 == 0 else 'odd')
print()

# 11
age: int = int(input('Enter your age:'))
height: int = int(input('Enter your height'))
if 8 <= age <= 18 and height > 100:
    print('Allowed to enter')
else:
    print('NOT allow to enter')
print()

# loops:
# 3
n: int = int(input('Enter a number:'))
for i in range(0, n + 1, 2):
    print(i, end=' ')
print()

# 4
max_num: int = int(input('Enter max:'))
den: int = int(input('Enter den:'))
for i in range(den, max_num + 1):
    if i % den == 0:
        print(i, end=' ')
print()

# data
# 4
num1: int = int(input('Enter the first number:'))
num2: int = int(input('Enter the second number:'))
result = 0
for _ in range(num2):
    result += num1
print('The result is:', result)
print()

# 5
num1: int = int(input('Enter the first number:'))
num2: int = int(input('Enter the second number:'))
result = 1
for _ in range(num2):
    result *= num1
print('The result is:', result)
print()

# 6
num: str = (input('Enter a number:'))
digit: str = input('Enter a digit:')
if digit in num:
    print(True)
else:
    print(False)
print()

# 8
number: int = int(input('Enter a number:'))
if number < 2:
    print(f'{number} is not a prime number')
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
if is_prime:
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')
print()
