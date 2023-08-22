
# 1
def func1():
    a = 'hello'
    b = 'world'

    print(f"{a} {b}!")


# 2
def func2():
    a = 3
    b = 1.234567

    print(f"{a:04d} {b:.3f}!")
    
# 3
def func3():
    a = '\thello'
    print(a)
    print(f"{a!r}")

if __name__ == "__main__":
    func1()
    # func2()
    # func3()