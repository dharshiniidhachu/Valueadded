def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

num_terms = int(input("Enter the number of terms: "))

result = fibonacci_series(num_terms)

print("Fibonacci series:", result)
