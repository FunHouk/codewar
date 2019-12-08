def cakes(recipe, available):
    l1 = list()
    for item in recipe:
        if item in available:
            n = available[item] // recipe[item]
            l1.append(n)
        else:
            l1.append(0)
    return min(l1)
