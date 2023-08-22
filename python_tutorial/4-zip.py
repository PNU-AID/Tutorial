from itertools import zip_longest

def func1():
    a = ['a', 'b', 'c', 'd']
    b = ['e', 'f', 'g', 'h']
    for i, j in zip(a, b):
        print(i, j)

def func2():
    a = ['a', 'b', 'c', 'd']
    b = ['e', 'f', 'g', 'h', 'i', 'j']
    for i, j in zip(a, b):
        print(i, j)

def func3():
    a = ['a', 'b', 'c', 'd']
    b = ['e', 'f', 'g', 'h', 'i', 'j']
    for i, j in zip_longest(a, b):
        print(i, j)
        
if __name__ == "__main__":
    # func1()
    # func2()
    func3()