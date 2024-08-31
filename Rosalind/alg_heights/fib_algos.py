import math

def fib(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))

def rabbit_offspring(months, growth_rate):
    parrent, child = 1, 1
    for itr in range(months-1):
        child, parrent = parrent, parrent + (child * growth_rate)

    return child, parrent