
# Lab 04: Loops
# Question 1: 


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# Question 2


n = int(input("Enter a number: "))

while n >= 0:
    print(n)
    n -= 1


# Question 3: 


base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1

for i in range(power):
    result = result * base

print("Result =", result)


# Question4

total = 0

for n in range(2, 1000):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        total += n

print("Sum =", total)


