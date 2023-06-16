#генератор с условием
a=[i for i in range(14)if i%3==0]

#генератор с циклом
a=[i**j for i in range(3) for j in range(3)]

#тернарный if:значение1 if условие else значение2
a=17
b=23
d=a if a>b else b
print(d)
