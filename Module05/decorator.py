
def decorator(func):
    def wrapper():
        print("avant")
        func()
        print("apres")
    return wrapper


@decorator
def say_hello():
    print("bonjour")

say_hello()