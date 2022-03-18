def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@do_twice
def greeting(name):
    print(f"Hello there {name}!")

@do_twice
def countPotatoes():
    print("Counting my potatoes...")
    return 2

if __name__ == "__main__":
    print("Testing decorators in python")
    greeting("Cookie and cream!")
    countPotatoes()
