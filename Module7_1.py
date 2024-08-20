from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):
    def __init__(self):
        print('init shop')

    __file_name = 'products.txt'

    def get_products(self):
        prod = open(Shop.__file_name, 'r')
        pprint(prod.read())
        prod.close()

    def add(self, *products):
        for i in range(len(products)):
            prod1 = products[i]
            #print(prod1)
            prod = open(Shop.__file_name, 'a')
            prod.write(str(prod1))
            #prod.write(f'{products[i]}')
            prod.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
