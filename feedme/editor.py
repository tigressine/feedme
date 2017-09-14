#!/usr/bin/env python3
from mitu import confirm_input, rinput, rprint
import os
import json
import pickle

class Order:
    """
    """
    def __init__(self, name, establishment, delivery_method, address):
        self.name = name
        self.establishment = establishment
        self.delivery_method = delivery_method
        self.address = address
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __add__(self, other):####
        if self.establishment != other.establishment:
            raise TypeError("orders are from different establishments")
        name = '{0} and {1}'.format(self.name, other.name)
        new_order = Order(name, self.establishment)
        for item in (self.items + other.items):
            new_order.add_item(item)
        return new_order

class Item:
    """
    """
    def __init__(self, name, options):
        self.name = name
        self.options = options
########################################

def command_help():
    header()
    print("help: help menu")
    print("n: new order")

def command_order_new():
    header()
    order = create_new_order()
    order.add_item(input_item())
    print("Add more items, or finish order? (Type 'add' or 'finish')")
    question = rinput("> ", ['add', 'finish'])
    while question == 'add':
        order.add_item(input_item())
        print("Add more items, or finish order? (Type 'add' or 'finish')")
        question = rinput("> ", ['add', 'finish'])






def create_new_order():
    print("Enter a name for the order (e.g. 'favorite pizza')")
    name = input("> ")

    print("Enter establishment name or type 'list'")
    valid = list(establishments.keys()) + ['list']
    establishment = rinput("> ",
                           valid,
                           invalid="Establishment not available")
    while establishment == 'list':
        for each in establishments.keys():
            print(each)
        establishment = rinput("> ",
                               valid,
                               invalid="Establishment not available")

    if len(establishments[establishment]['delivery methods']) != 1:
        print("Enter delivery method or type 'list'")
        valid = establishments[establishment]['delivery methods'] + ['list']
        method = rinput("> ", valid, invalid="Invalid delivery method")
        while method == 'list':
            for each in establishments[establishment]['delivery methods']:
                print(each)
            method = rinput("> ", valid, invalid="Invalid delivery method")
    else:
        print("Only {} available. Selecting by default.".format(
            establishments[establishment]['delivery methods']))
        method = establishments[establishment]['delivery methods']
    
    if len(personal) != 0:
        prompt="(Y/n): "
        ask="Deliver to default address? ({})".format(
            personal['address']['default'][0])
        if confirm_input(prompt, ask):
            address = personal['address']
        else:
            for address in personal['address']:
                print(personal['address'][address]) #fancy print##unfinished
    return Order(name, establishment, method, address)
    
def input_item():
    print("Type the name of the item you'd like to add, or type 'list'")
    valid = list(items.keys()) + ['list']
    item = rinput("> ", valid)
    while item == 'list':
        for each in items.keys():
            print(each)
        item = rinput("> ", valid)

    print("Which options would you like to add for the item? Leave blank " +
          "for no options.")
    valid = items[item][1::] + ['list', '']
    options = rinput("> ", valid)
    while options == 'list':
        for each in items[item][1::]:
            print(each)
        options = rinput("> ", valid)
    return Item(item, options)
    
def command_quit():
    header()
    if confirm_input(ask="Are you sure you'd like to quit? (Y/n)"):
        os.system('clear')
        quit()
    else:
        header()

def header():
    os.system('clear')
    text = "FeedMe"
    print(text)

def load_establishments():
    try:
        with open(F_ESTABLISHMENTS, 'r') as f:
            establishments = json.load(f)
    except FileNotFoundError:
        establishments = {}
    return establishments

def load_orders():
    try:
        with open(F_ORDERS, 'rb') as f:
            orders = pickle.load(f)
    except FileNotFoundError:
        orders = []
    return orders

def load_personal():
    try:
        with open(F_PERSONAL, 'r') as f:
            personal = json.load(f)
    except FileNotFoundError:
        personal = {}
    return personal

def main():
    valid = {'h':command_help,
             'n':command_order_new,
             'q':command_quit}
    header()
    
    while True:
        print("What would you like to do? ('help' for a list of commands)")
        command = rinput("> ", valid.keys())
        valid[command]()
###################################################

F_ESTABLISHMENTS = 'data/establishments.json'
F_ORDERS = 'data/orders.data'
F_PERSONAL = 'data/personal.json'

items = {'cheeze': ['lipstick'], 'pepeer': ['nomayo','mayo'], 'suasage': []}
establishments = load_establishments()
orders = load_orders()
personal = load_personal()
main()
