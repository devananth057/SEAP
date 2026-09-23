"""Simple calculator application for DevOps CI assignment."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("DevOps CI Calculator")
    print("2 + 3 =", add(2, 3))

# Feature branch enhancement
print("Feature: calculator ready")
