def func1():
    a = [1, 2, 3, 4, 5]
    b = [x**2 for x in a]
    c = {x: x+10 for x in a}
    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    func1()