"""mitu (methods for interactive terminal utilities)

A collection of methods that may be useful when building interactive terminal
elements in programs. Check individual descriptions to discover which methods
are most useful to you.

Author: Tiger Sachse
Initial Release: 08/16/2017
Current Release: 08/16/2017
Version: 1.0.0
License: GPLv3
"""
import re
from termcolor import cprint

def confirm_input(prompt="> ", ask="Is this correct? (Y/n)"):
    """Confirm input by soliciting a yes or no from user.
    
    Relies on rinput() method to validate response.
    """
    print(ask)
    valid = ['y', 'Y', 'yes', 'Yes', 'n', 'N', 'no', 'No']

    while True:
        i = rinput(prompt, valid)
        if i in valid[:4]:
            return True
        elif i in valid[4:]:
            return False
        else:
            break


def rinput(prompt, valid, escape=['q'], invalid="Invalid input.", regex=False):
    """Return user input only if within a valid list.

    Useful to restrict user input to a certain range of integers, for example.
    Accepts regular expressions in the valid list parameter if the regex
    parameter is set to True. User can escape the while loop using characters
    defined in the escape parameter (by default just 'q'). If user input is
    invalid, the invalid string parameter is printed to the screen and the user
    is prompted for input again.
    """
    while True:
        i = input(prompt)
        if regex:
            for pattern in valid:
                if re.search(pattern, i):
                    return i
        elif i in valid:
            return i
        
        if i in escape:
            break
        print(invalid)


def generate_template(align, width, fill_char=''):
    """Return template formatted with method parameters.

    Returned template is intended to be passed into rprint.
    """
    alignments = {'left': '<',
                  'right': '>',
                  'center': '^'}
    template = '{{:{fill_char}{align}{width}}}'.format(fill_char=fill_char,
                                                       align=alignments[align],
                                                       width=width)
    return template


def rprint(templates, strings, spacing, color=None):
    """Print formatted columns to screen.

    For each template in templates, a column of a set width is printed to the
    screen. This column width is defined in the spacing list parameter. The
    printed line can be colored by passing a color name as the color parameter.
    Color availability is based on termcolor's color support and only colors
    supported by termcolor will work.

    Current termcolor colors:
    grey, red, green, yellow, blue, magenta, cyan, white
    """
    for each in zip(templates, strings, spacing):
        line = each[0].format(each[1][:each[2]], width=each[2])
        if not color:
            print(line, end='')
        else:
            cprint(line, color, end='')
    print('')
