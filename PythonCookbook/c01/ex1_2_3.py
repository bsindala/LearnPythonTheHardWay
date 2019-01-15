items = [1, 10, 7, 4, 5, 9]

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

sum(items)