import timeit
import random
import string


strings = string.digits + string.ascii_lowercase
data = ''
for _ in range(100000):
    data += random.choice(strings)
data = data.encode("utf8")
memoryview_data = memoryview(data)

def run_test1():
    for i in range(100):
        chunk = data[i:i+10000]
    

def run_test2():
    for i in range(100):
        chunk = memoryview_data[i:i+10000]

def func1():
    result = timeit.timeit(
        stmt="run_test1()",
        globals=globals(),
        number=100) / 100
    print(f"{result:.9f}sec")
        
def func2():
    result = timeit.timeit(
        stmt="run_test2()",
        globals=globals(),
        number=100) / 100
    print(f"{result:.9f}sec")
    
if __name__ == "__main__":
    func1()
    func2()