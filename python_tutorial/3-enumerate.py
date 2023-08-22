def func1():
    a = ['a', 'b', 'c', 'd']
    for i in range(len(a)):
        print(i, a[i])

def func2():
    a = ['a', 'b', 'c', 'd']
    for i, a_ele in enumerate(a):
        print(i, a_ele)
if __name__ == "__main__":
    # func1()
    func2()