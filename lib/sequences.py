

def print_fibonacci(length):
    fibonacci_list = []
    for n in range(length):
        fibonacci_list.append(n)
        if n >= 2:
            fibonacci_list[n] = fibonacci_list[n-2] + fibonacci_list[n-1]
        
    print(fibonacci_list)
        