# Q6 - Recursion and Memoisation

import sys
from functools import lru_cache

calls = 0


# Normal recursive function
def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Recursive function with memoisation
calls = 0

@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


# Iterative method
def ways_loop(n):
    if n <= 1:
        return 1

    a = 1
    b = 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


# Answers from 1 to 6
print("Answers from 1 to 6")

for i in range(1, 7):
    print(i, "steps:", ways_memo(i))


# Compare normal recursion and memoisation
calls = 0
print("\nNaive Result:", ways_naive(25))
print("Naive Calls:", calls)

calls = 0
ways_memo.cache_clear()

print("\nMemoised Result:", ways_memo(25))
print("Memoised Calls:", calls)


# Iterative result for 1000 steps
print("\nIterative Result for 1000 steps:")
print(ways_loop(1000))


# Recursion limit
print("\nCurrent Recursion Limit:")
print(sys.getrecursionlimit())


# Memoisation for 1000 steps
try:
    print("\nMemoised Result for 1000 steps:")
    print(ways_memo(1000))

except RecursionError:
    print("Recursion limit exceeded. Use iterative method.")