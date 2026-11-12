# Q4 - String Building Using +, join() and f-string

import time


items = [f"Call {i}: Rs {i * 2}" for i in range(1000)]


# Method 1: Using +=
def build_plus(items):
    text = ""

    for item in items:
        text += item + "\n"

    return text


# Method 2: Using join()
def build_join(items):
    return "\n".join(items) + "\n"


# Method 3: Using f-string
def build_fstring(items):
    parts = []

    for item in items:
        parts.append(f"{item}\n")

    return "".join(parts)


# Performance measurement
start = time.perf_counter()
a = build_plus(items)
time_plus = time.perf_counter() - start

start = time.perf_counter()
b = build_join(items)
time_join = time.perf_counter() - start

start = time.perf_counter()
c = build_fstring(items)
time_fstring = time.perf_counter() - start


print("Plus and join same:", a == b)
print("Join and f-string same:", b == c)

print("Plus time:", time_plus)
print("Join time:", time_join)
print("F-string time:", time_fstring)