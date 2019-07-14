def next_item(s, item):
    it = iter(s)
    next(iter(x for x in it if x == item), None)
    return next(it, None)