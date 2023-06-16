class Product:
    def __init__(self,name,weight,price):
        self.name=name
        self.weight=weight
        self.price=price

    def __add__(self,other):
        if isinstance (other,Product):
            return self.price+other.price
        elif isinstance (other,int):
            return self.price+other

product_1=Product('видеокарта' ,0.8, 60000)
product_2=Product('флешка' ,0.08, 500)

total_price=product_1+product_2
print(total_price)

new_price=product_1+1000
print(new_price)

