'''from pprint import pprint
from typing import Iterator

mylist=[{'name':'телефон','brand':'realme','price':20000},
       {'name':'ноутбук','brand':'apple','price':35000},
       {'name':'наушники','brand':'jbl','price':3000}]

def item_price(item):
    return item['price']

print(sorted(mylist,key=item_price))
#сортировка по цене
pprint(sorted(mylist,key=lambda item:item['price']))

apple_list=list(filter(lambda item:item['brand']=='apple',mylist))
pprint(apple_list)

#позволяет применить действие ко всем элементам
mylist=['1','2','3','4','5']
mylist=list(map(int,mylist))
print(mylist)'''

names=['Alyona','Danila','Ira','Ivan']
surnames=['Panasenko','Bodrov','Ivanova','Petrov']

'''full_name_list=list(map(lambda name,surname:f'{name} {surname}',names,surnames))
print(full_name_list)

#функция позволяет получать не только элемент, но и его индекс
spisok=[]
for i,item in enumerate (mylist):
    spisok.append({i:item})
pprint(spisok)'''

for name,surname in zip(names,surnames):
    print(name,surname)
