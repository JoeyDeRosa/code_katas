"""parenthetics code-kata."""


def parenthetics(string):
    """Return 1, 0, or -1 depending on the string input."""
    queue = []
    for i in string:
        if i is '(':
            queue += [i]
        if i is ')':
            if len(queue) < 1:
                return -1
            queue.pop(0)
    if len(queue) > 0:
        return 1
    return 0
