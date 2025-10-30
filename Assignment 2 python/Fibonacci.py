# Write a program that takes a number n and prints the first n numbers in the Fibonacci sequence.
# Use both Recursion and regular method

# Fibonacci sequence using iterative method

def fibonacci_iterative(n):
    a = 0
    b = 1
    print("Fibonacci sequence using iterative method")

    for i in range(n):
        print(a, end = " ")
        a, b = b, a + b


# Fibonacci sequence using iterative method

def fibonacci_recursive(n, a=0, b=1, count=0):
    if count <n:
        print(a, end = " ")
        fibonacci_recursive(n, b, a+b, count +1)

n = int(input("Enter how many fibonacci number to print:"))

fibonacci_iterative(n)

print("\nFibonacci sequence using recursive method:")
fibonacci_recursive(n)