#!/usr/bin/env python2.7
"""
 Product Inventory Project - Create an application which manages an inventory of
 products. Create a product class which has a price, id, and quantity on hand.
 Then create an inventory class which keeps track of various products and can
 sum up the inventory value.
 
 Author: Dan Granillo <dan.granillo@gmail.com>

"""

class Product(object):
    num_products = 0
    def __init__(self, name, qty, price):
        self.price = price
        self.name = name
        self.qty = qty
        self.pid = Product.num_products + 1
        Product.num_products += 1

    def update_qty(self, qty):
        self.qty += qty
    
    def print_product(self):
        print "We have %s %s at $%s" %(self.qty, self.name, self.price)

class Inventory(object):
    def __init__(self):
        self.products = []
    
    def add(self, product):
        self.products.append(product)
        print "%s %s added to inventory with PID:%s" %(product.qty,
                product.name, product.pid)
    
    def print_inventory(self):
        value = 0
        for item in self.products:
            value += item.price * item.qty
            print "Inventory value = $%.02f" %(value)

if __name__ == '__main__':
    bananas = Product("banana", 5, 10.00)
    apples = Product("apple", 25, 3.00)
    cherries = Product("cherry", 100, 4.00)

    i = Inventory()

    i.add(bananas)
    i.add(apples)
    i.add(cherries)
    
    i.print_inventory()
