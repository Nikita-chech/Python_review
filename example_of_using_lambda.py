digs = [int(x) for x in input().split()]


def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

print(*filter_lst(digs))
print(*filter_lst(digs, lambda x: x < 0))
print(*filter_lst(digs, lambda x: x >= 0))
print(*filter_lst(digs, lambda x: 3 <= x <= 5))
