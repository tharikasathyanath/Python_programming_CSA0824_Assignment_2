# Q5 - Functions, Parameters and Scope

# Buggy function
def add_item_buggy(item, order=[]):
    order.append(item)
    return order


# Correct function
def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


# Testing three customers
print("Buggy Function")
print(add_item_buggy("Tea"))
print(add_item_buggy("Vada"))

print("\nCorrect Function")

customer1 = add_item("Tea")
customer2 = add_item("Vada")
customer3 = add_item("Coffee")

print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)


# Positional and keyword arguments
def student(name, age=18):
    print("Name:", name)
    print("Age:", age)


student("Ravi")
student(name="Priya", age=19)


# Returning multiple values
def calculate_bill(amount):
    gst = amount * 0.05
    total = amount + gst
    return total, gst


total, gst = calculate_bill(500)

print("\nTotal Amount:", total)
print("GST:", gst)


# Global variable
x = 10

def global_example():
    global x
    x = 20

global_example()
print("\nGlobal Value:", x)


# Local variable
def local_example():
    y = 50
    print("Local Value:", y)

local_example()


# Nonlocal variable
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print("Count:", count)

    inner()
    inner()

outer()


# Display default values of buggy function
print("\nBuggy Function Defaults:")
print(add_item_buggy.__defaults__)