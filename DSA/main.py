#Ayaan Bajwa 
#Asignment 1 (Data Structures and Algorithems)
#Student ID: 100864399

import random
import time

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price 
        self.category = category 
        
def load_data(file_path):
    prod = []
    with open (file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            product = Product(int(data[0]), data[1], float(data[2]), data[3])
            prod.append(product)
    return prod

def print_products(prod):
    for product in prod:
        print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

product_data = load_data('product_data.txt')
product_array = product_data.copy()
product_linked_list = product_data.copy()

def insert_prod(data_structure, new_product):
    data_structure.append(new_product)
    
def update_prod(data_structure, product_id, new_data):
    for product in data_structure:
        if product.product_id == product_id:
            product.name = new_data['name']
            product.price = new_data['price']
            product.category = new_data['category']
            break
        
def del_prod(data_structure, product_id):
    data_structure[:] = [product for product in data_structure if product.product_id != product_id]
    
def search_prod(data_structure, key, value):
    return [product for product in data_structure if getattr(product, key) == value]

def bubble_sort(product, key='price'):
    bub = len(product)
    for i in range(bub):
        for j in range(0, bub-i-1):
            if getattr(product[j], key) > getattr(product[j+1], product[j], key):
                product[j], product[j+1] = product[j+1], product[j]

def time_sort_algorithem(algorithem, products):
    start_time = time.time()
    algorithem(products)
    end_time = time.time()
    return end_time - start_time

def main():
    file_path = 'product_data.txt'

    product_data = load_data(file_path)
    product_array = product_data.copy()
    product_linked_list = product_data.copy()
    
    new_product= Product(101, 'New Product', 25.99, 'Electronics')
    insert_prod(product_array, new_product)
    
    update_data = {'name': 'Updated Product', 'price': 29.99, 'category': 'Home Appliances'}
    update_prod(product_linked_list, 102, update_data)
    
    delete_product_id = 103
    del_prod(product_data, delete_product_id)
    
    search_key = 'category'
    search_value = 'Electronics'
    search_result = search_prod(product_data, search_key, search_value)
    
    bubble_sort(product_data)
    
    print("Product Data: ")
    print_products(product_data)
    
    print('\nProduct Array:')
    print_products(product_array)
    
    print("\nProduct Linked List:")
    print_products(product_linked_list)

if __name__ == "__main__":
    main()
    
    
    
    
