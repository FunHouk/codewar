recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
l1 = list()
for item in recipe:
    n = available[item] // recipe[item]
    l1.append(n)
    
print (min(l1)) 