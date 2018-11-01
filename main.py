"""
File Name: main.py

Developer: Nicholas Nicodemus

Date last modified: 11/1/2018

Description: Retail Item Class

email address: nicknic86@yahoo.com
"""

class RetailItem:
    def __init__(self):
        self.item = 0
        self.description = 0
        self.units = 0
        self.price = 0

    def print_items(self):
        print(self.item,self.description,self.units,self.price)
      

print('Item','Description','Units in inventory','Price')

item_list = []

item1 = RetailItem()
item1.item = 'Item #1'
item1.description = 'Jacket'
item1.units = 12
item1.price = 59.95
item1.print_items()

item2 = RetailItem()
item2.item = 'Item #2'
item2.description = 'Designer Jeans'
item2.units = 40
item2.price = 34.95
item2.print_items()

item3 = RetailItem()
item3.item = 'Item #3'
item3.description = 'Shirt'
item3.units = 20
item3.price = 24.95
item3.print_items()

print(item_list)
    
