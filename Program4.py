# WAP to declare global variable.

counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Counter after increment: {counter}")

def reset_counter():
    global counter
    counter = 0
    print(f"Counter after increment: {counter}")

# Calling functions

increment_counter()
increment_counter()
reset_counter()
increment_counter()
