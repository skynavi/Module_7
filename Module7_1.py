class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        prod_file = open(self.__file_name, 'r')
        products = prod_file.read()
        prod_file.close()
        return products

    def add(self, *products):
        prod_file = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in self.get_products():
                prod_file.write(str(product) + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        prod_file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
