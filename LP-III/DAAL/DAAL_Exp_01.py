'''
Madhur Jaripatke
Roll No. 52
BE A Computer
RMDSSOE, Warje, Pune
'''
'''
Write a program non-recursive and recursive program to calculate Fibonacci numbers
and analyze their time and space complexity. 
'''
# Non-Recursive Fibonacci Function
def fibonacci_non_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Recursive Fibonacci Function
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Time and Space Complexity Analysis
def analyze_complexity():
    print("\nNon-Recursive Fibonacci:")
    print("Time Complexity: O(n)")
    print("Space Complexity: O(1)")

    print("\nRecursive Fibonacci:")
    print("Time Complexity: O(2^n)")
    print("Space Complexity: O(n)")

# Example Usage
n = int(input('Enter a number: '))
print(f"Non-Recursive Fibonacci of {n} is: {fibonacci_non_recursive(n)}")
print(f"Recursive Fibonacci of {n} is: {fibonacci_recursive(n)}")

analyze_complexity()