# Q7 - Diagnose, Redesign and Validate

import time


# Generate data
def generate_items(n):
    return [f"Item {i}: Rs {i * 10}" for i in range(n)]


# Original method using +
def original_method(items):
    result = ""

    for item in items:
        result += item + "\n"

    return result


# Redesigned method using join()
def redesigned_method(items):
    return "\n".join(items) + "\n"


# Test different input sizes
sizes = [1000, 10000, 200000]

print("STRING BUILDING PERFORMANCE COMPARISON")
print("-" * 60)

for size in sizes:

    items = generate_items(size)

    # Original method
    start = time.perf_counter()
    original_result = original_method(items)
    original_time = time.perf_counter() - start

    # Redesigned method
    start = time.perf_counter()
    redesigned_result = redesigned_method(items)
    redesigned_time = time.perf_counter() - start

    print("\nNumber of Items:", size)

    print("Original Time:", round(original_time, 6), "seconds")

    print("Redesigned Time:", round(redesigned_time, 6), "seconds")

    print("Results Identical:", original_result == redesigned_result)

    if redesigned_time > 0:
        improvement = original_time / redesigned_time
        print("Speed Improvement Ratio:", round(improvement, 2))