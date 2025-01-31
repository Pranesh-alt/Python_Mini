num = int(10)
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")



n = int(3)
total = sum(range(1, n+1))
print(f"Sum is: {total}")




n = int(8)
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b






def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

num = int(6)
print(f"Factorial is: {factorial(num)}")





text = input("Enter a string: ")
if text == text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")







a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)
print(f"The largest number is: {largest}")





vowels = "aeiouAEIOU"
text = "Pranesh"
count = sum(1 for char in text if char in vowels)
print(f"Number of vowels: {count}")




num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")




text = input("Enter a string: ")
reversed_text = text[::-1]
print(f"Reversed string: {reversed_text}")







numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
total = sum(numbers)
print(f"Sum of the list elements: {total}")





print("hello world!")