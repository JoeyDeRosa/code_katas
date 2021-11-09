'''My code for sum-of-nth-terms kata.'''


def series_sum(n):
    '''Add 1 divided by a div increasing by three for range n.'''
    if n == 0:
        return '0.00'
    acc = 0
    div = -2
    for i in range(n):
        div += 3
        acc += 1 / div
    acc = str(round(acc, 2))
    if len(acc) <= 3:
        acc += '0'
    return acc
