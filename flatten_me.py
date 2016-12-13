'''My code for the Flatten Me code kata.'''


def flatten_me(lst):
    '''Turn a list with lists inside it into a single list.'''
    flat = []
    for i in lst:
        if type(i) is list:
            for x in i:
                flat.append(x)
        else:
            flat.append(i)
    return flat
