#! /usr/bin/env python3
import json

establishments = {}

def new_establishment(name, delivery_methods, pay_methods, items):
    establishments[name] = {'delivery methods': delivery_methods,
                            'pay methods': pay_methods,
                            'items': items}


def new_personal(name, address, payment_info):
    personal = {'name': name,
                'address': address, 
                'payment info': payment_info}
    return personal

personal = new_personal(
        'Tiger',
        {'default': ['1108 Choctaw St.', 'Jupiter, FL', '33458'],
         'address2': ['12336 Golden Knight Circle',
             'Orlando, FL',
             '32817',
             'Apt #29-105-A']},
        {'card number':'1234123412341234',
         'expires':'8/21',
         'CVC':'800'})
new_establishment('papa johns',
                  ['delivery', 'carryout'],
                  ['cash', 'visa', 'check', 'venmo'],
                  {'cheese pizza' : ['pepperoni', 'onions',
                                     'anchovies', 'sausage',
                                     'green peppers'],
                   'garlic knots' : ['no sauce'],
                   'soda' : ['diet coke',
                             'diet pepsi',
                             'sprite']})

with open('establishments.json', 'w') as f:
    json.dump(establishments, f)


with open('personal.json', 'w') as f:
    json.dump(personal, f)
