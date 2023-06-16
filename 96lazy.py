import time
import contextlib

'''#строгие вычисления
my_iter = [time.sleep(x) for x in range(1,3)]
print(my_iter)

#ленивые вычисления
my_iter2 = (time.sleep(x) for x in range(1,3))
print(my_iter2)


#ленивые вычисления в виде функции
def my_laza_calc(items):
    yield from items

items = ['Яблоко', 'Банан', 'Груша']

for i in  my_laza_calc(items):
    print(i)

my_file = open('96lazy.txt', 'w')

my_file.write('Write some info...')

my_file.close()

with open('96lazy.txt','w') as my_file:
    my_file.write('Write some info...')
    print(my_file.closed)

print(my_file.closed)

#переворачивание строки с контекстным менеджером
@contextlib.contextmanager
def str_reverse(my_str):
    print('Входим в контекстный менеджер:')
    yield my_str[::-1]
    print('выходим из контекстного менеджера')

with str_reverse('hello,world') as reversed_str:
    print(f'выполняется код:{reversed_str}')

spisok=(x**2 for x in range(1000000))
print(spisok)'''

def gen():
    for x in range(1000000):
        yield x**2
for x in gen():
    print(x)


    


