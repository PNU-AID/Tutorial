def func1():
    # 가변인자 사용
    def star(a, b, *c):
        print("a", a)
        print("b", b)
        print("c", c)
    
    star(1, 2, 3, 4, 5, 6, 7)
    
def func2():
    # 가변인자 사용
    def kwargs(num=10, **kwargs):
        print("num", num)
        print("kwargs", kwargs)
        
    tmp = {
        "name": "john",
        "age": 20
    }
    kwargs(**tmp)


if __name__ == "__main__":
    # func1()
    func2()