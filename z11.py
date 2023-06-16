"""class A:
    def public(self):
        return 42

    def _private(self):
        return 'test'

    def __protect(self):
        return True

    def wrapper_protect(self):
        return self.__protect()

a =A()

print(a.public())
print(a._private())
print(a.wrapper_protect())"""

from datetime import datetime

def timeit(func):
    def wrapper(val):
        start=datetime.now()
        res=func(val)
        end=datetime.now()
        print(f'time:{end-start}')
        return res

    return wrapper
@timeit
def get_list_1(val):
    return[x for x in range(val) if x%2==0]

@timeit
def get_list_2(val):
    new_list = []
    for x in range(val):
        if x % 2 == 0:
            new_list.append(x)
        return new_list
    

val=1000000

a=(get_list_1(val))
b=(get_list_2(val))
      
