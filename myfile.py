from functools import cache


def fib_slow(i: int):
    """Returns the i-th term in the fibonnacci sequence using recursive calculation"""
    if i <= 1:
        return i
    return fib_slow(i - 1) + fib_slow(i - 2)


def fib_fast(i: int):
    """Returns the i-th term in the fibonnacci sequence using tabular dynamic programming"""
    if i <= 1:
        return i
    
    a, b = 0, 1
    for _ in range(i - 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    i = int(input("Enter some i to compute the i-th fibonnaci number: "))
    print("It is:", fib_fast(i))
