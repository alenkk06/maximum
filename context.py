'''import time
class Running:
    def __init__(self):
        self.start=None

    def __enter__(self):
        self.start=time.time()
        #return 19

    def __exit__(self,exc_type,exc_val,exc_tb):
        t=time.time()-self.start
        print(f'Время работы кода:{t}')

        if exc_type is TypeError:
            return True

with Running() as t1:
    listt=[x for x in range (1000000)]
    #print(t1)
    listt-='s'''


import random

class RandomIter:
    def __init__(self,limit):
        self.limit=limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit==0:
            raise StopIteration
        self.limit-=1
        return random.randint(0,100)

rand_iter=RandomIter(10)
print(iter(rand_iter))

for i in rand_iter:
    print(i)
