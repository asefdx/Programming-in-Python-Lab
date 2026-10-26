
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




