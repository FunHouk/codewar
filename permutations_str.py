import itertools
def permutations(string):
    res = itertools.permutations(string)
    print (res)
    return [''.join(str) for str in (set(res))]

permutations('aabb')