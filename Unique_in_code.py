def unique_in_order(iterable):
    c = []
    pre = None
    for value in iterable:
        if value != pre:
            c.append(value)
            pre = value
    return c