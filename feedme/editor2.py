#! /usr/bin/env python3
#REMOVE ME PLEASE
from mitu import confirm_input, rinput, rprint
import os
import sqlite3 as sql

def TEMPORARY_POPULATE_DATABASE():
    db = sql.connect("papa.db")
    curse = db.cursor()

    try:
        curse.execute('''CREATE TABLE papa (method text, items text)''')
    except:
        pass
    curse.execute('''INSERT INTO papa VALUES ('delivery', 'cheese pizza')''')
    db.commit()

################################################################################

def database():
    base = sql.connect("{}.db".format(establishment))
    cursor = base.cursor()
    

def query(cursor, establishment, column):
    base = sql.connect("{}.db".format(establishment))
    cursor = base.cursor()
    command = "SELECT {0} FROM {1}".format(column, establishment)
    
    return [row[0] for row in cursor.execute(command)]

TEMPORARY_POPULATE_DATABASE()################
newlist = query('papa', 'items')
newlist2 = query('papa', 'method')
print(newlist)
print(newlist2)
