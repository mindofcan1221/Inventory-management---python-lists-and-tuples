#!/usr/bin/env python
# coding: utf-8

#inventory list that will contains list of tuples
inventory =[]
#add inventory function- adds an item to inventory 
def add_inventory(inventory,name,quantity,price):
    inventory.append((name,quantity,price))

#displays items within an inventory
def display_inventory(inventory):
    if inventory:
        for item in inventory:
            print(item)
    else:
        print("There is no item in the inventory.")

#function to display in tabular format
def display_formal(inventory):
    if inventory:
        print("Item Name \t\t Quantity \t Price")
        print("-"*50)
        for item in inventory:
            print(f"{item[0]}\t\t\t{item[1]}\t\t\t{item[2]}")
    else:
        print("There is no item to display")
            

#updates the price of an item
def update_inventoryprice(inventory,name,price):
    if inventory:
        count=0
        for item in inventory:
            if item[0]==name:
                inventory[count]=(inventory[count][0],inventory[count][1],price)
                break
            count+=1
    else:
        print("There are no items to be updated.")
    if count== len(inventory):
        print("The item is not found.")
    else:
        print(f"item {name} price is updted to {price}")
                


#updates the quantity of an item
def update_inventoryquanity(inventory,name,quantity):
    if inventory:
        count=0
        for item in inventory:
            if item[0]==name:
                inventory[count]=(inventory[count][0],quantity,inventory[count][2])
                break
            count+=1
    else:
        print("There are no items to be updated.")
    if count== len(inventory):
        print("The item is not found.")
    else:
        print(f"item {name} quantity is updated to {quantity}")
                

#delete an item from the inventory
def delete_iteminventory(inventory,itemname):
    if inventory:
        for item in inventory:
            if item[0]==itemname:
                del item
    else:
        print("No items in inventory.")

#function to calculate the total quantity within the inventory
def total_inventoryquantity(inventory):
    totalinventory=0
    if inventory:
        for item in inventory:
            totalinventory+=item[1]
        message="total inventory quantity="+totalinventory
    else:
        message="There are no items in the inventory."
    return message

#function to calculate the total price of items in the inventory
def total_inventoryprice(inventory):
    totalprice=0.0
    if inventory:
        for item in inventory:
            totalprice+= item[1]*item[2]
        message=" The total price of items in the inventory="+totalprice
    else:
        message=" There are no items within the inventory." 
    return message 







