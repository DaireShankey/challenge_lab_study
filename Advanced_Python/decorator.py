# decorators.py

# Define a decorator to log function execution
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Use the decorator with a simple function
@log_execution
def multiply(a, b):
    return a * b

# Call the decorated function
multiply(5, 3)
