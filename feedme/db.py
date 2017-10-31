#! /usr/bin/env python3
import sqlite3 as sql
import os

def convert_options(option_list):
    return ';;'.join(option_list)

def db_operation(operation):

    def db_wrap(*args, **kwargs):
        if not os.path.isdir("data/"):
            os.mkdir("data/")
        name = args[0].replace(" ", "")
        db = sql.connect('data/{0}.db'.format(name))
        curse = db.cursor()
        
        operation(*args, curse, **kwargs)
        
        db.commit()
        db.close()

    return db_wrap

@db_operation
def create_database(establishment, curse):
    curse.execute("CREATE TABLE general (obtain text, payment text)")
    curse.execute("CREATE TABLE items (item_name text, option_set text)")
    curse.execute("CREATE TABLE options (set_name text, set_options text)")

@db_operation
def clear_database():
    pass

@db_operation
def read_database():
    pass

@db_operation
def add_data(establishment, data, curse, tables=['general', 'items', 'options']):
    if 'general' in tables:
        for method in data['obtain']:
            curse.execute("INSERT INTO general ('obtain') VALUES (?)", (method,))
        for method in data['payment']:
            curse.execute("INSERT INTO general ('payment') VALUES (?)", (method,))
    if 'items' in tables:
        for item in data['items'].keys():
            curse.execute("INSERT INTO items VALUES (?,?)",
                          (item,
                           data['items'][item]))
    if 'options' in tables:
        for set_name in data['options'].keys():
            set_options = convert_options(data['options'][set_name])
            curse.execute("INSERT INTO options VALUES (?,?)",
                          (set_name,
                           set_options))

example_dict = {'obtain' : ['delivery', 'carryout'],
                'payment': ['credit', 'cash', 'debit'],
                'items'  : {'cheese pizza' : 'optset1',
                            'pepperoni piz' : 'optset1',
                            'diet coke' : 'optset0',
                            'garlic knots' : 'optset2'},
                'options': {'optset0': [],
                            'optset1': ['no cheese', '10-inch', 'pineapple'],
                            'optset2': ['no sauce']}
                }
    
#create_database("example")
#add_data("example", example_dict)
