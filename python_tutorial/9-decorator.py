def wrapper(func):
    def inner_func(*args, **kwargs):
        func(*args, **kwargs)
    return inner_func

@wrapper
def func1(name):
    print(f"{name}")

if __name__ == "__main__":
    func1("Tom")
    # func2()