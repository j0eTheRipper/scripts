def fib(n, memory = {}):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    elif n in memory:
        return memory[n]
    else:
        memory[n] = fib(n - 1, memory) + fib(n - 2, memory)
        return memory[n]
