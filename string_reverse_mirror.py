'''My code from reverse and mirrir kata.'''


def reverse_and_mirror(s1, s2):
    '''String2 is reversed and casefliped, string1 is reversed, casefliped, and mirrored.'''
    string1 = s1[::-1].swapcase() + s1.swapcase()
    string2 = s2[::-1].swapcase()
    return string2 + '@@@' + string1
