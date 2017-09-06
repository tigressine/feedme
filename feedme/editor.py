#!/usr/bin/env python3
from mitu import confirm_input, rinput, rprint
import os
import json
import pickle

class Order:
    """
    """
    def __init__(self, name, establishment):
        self.name = name
        self.establishment = establishment
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __add__(self, other):
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
    print("Enter establishment name or type 'list places' for a list")
    place = input("> ")

    while place not in places.keys():
        if place == 'list places':
            for key in places.keys():
                print(key)
        elif place == 'q':
            return
        else:
            print("Establishment not available")
        place = input("> ")

    if len(places[place]['delivery methods']) != 1:
        print("Enter delivery method or type 'list methods'")
        delivery_method = input("> ")

        while delivery_method not in places[place]['delivery methods']:
            if delivery_method == 'list methods':
                for method in places[place]['delivery methods']:
                    print(method)
            elif delivery_method == 'q':
                return
            else:
                print("Invalid delivery method")
            delivery_method = input("> ")
    else:
        delivery_method = places[place]['delivery methods']
        print("Only {} available. Selecting by default.".format(places[place]['delivery methods']))
    
    if len(personal) != 0:
        prompt="(Y/n): "
        ask="Deliver to default address? ({})".format(personal['address']['default'][0])
        if confirm_input(prompt, ask):
            address = personal['address']
        else:
            for address in personal['address']:
                print(personal['address'][address]) #fancy print

    


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

def load_places():
    try:
        with open(F_PLACES, 'r') as f:
            places = json.load(f)
    except FileNotFoundError:
        places = {}
    return places

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

F_PLACES = 'establishments.json'
F_ORDERS = 'orders.data'
F_PERSONAL = 'personal.json'

places = load_places()
orders = load_orders()
personal = load_personal()
main()
