"""
Tiger Sachse
"""
import os.path
import json

def card_validity_check(ccnumber):
    """
    Checks whether credit card number is valid.
    First checks for non-digit characters and filters out
    spaces. Then it builds a string, ccnum, in reverse.
    Finally it checks the string using the Luhn algorithm.
    Returns true if card number passes all tests, returns
    false otherwise.
    """
    ccnum = ""
    for x in str(ccnumber):
        if not x.isdigit():
            if x == " ":
                continue
            else:
                return False
        ccnum = x + ccnum

    sum = 0
    ccnum_length = len(ccnum)

    if ccnum_length not in range(15,17):
        return False

    for count in range(0,ccnum_length):
        num = int(ccnum[count])
        if count % 2 != 0:
            num *= 2
            if num > 9:
                num -= 9
        sum += num

    if sum % 10 == 0:
        return True
    else:
        return False

def alias_create(name, restaurant, quantity, options_tuple, flag):

    alias_dict = {"restaurant":restaurant,
                    "quantity":quantity,
                    "options":options_tuple,
                    "flag":flag}

    if not os.path.isfile("aliases.list"):
        print("file doesnt exist")
        with open("aliases.list","w") as f:
            aliases_dict = {name:alias_dict}
            f.write(json.dumps(aliases_dict))

    else:
        try:
            with open("aliases.list","r") as f:
                aliases_dict = json.loads(f.read())
                key_test = aliases_dict[name]
                print("key_test")
                print("bad key")

        except KeyError:
            print("keyerror")
            with open("aliases.list","r+") as f:
                aliases = json.loads(f.read())
                aliases[name] = alias_dict
                f.write(json.dumps(aliases))




def alias_retrieve():
    pass


"""
###########################################
#print(card_validity_check("5364 5870 1178 5834"))
######################################
"""

alias_create("one","pap","food","tup","-d")
alias_create("two","pap","food","tup","-d")
alias_create("three","pap","food","tup","-d")



with open("aliases.list","r") as f:
    test_dict = json.loads(f.read())
    print(test_dict)
    
    
    
    
    
    