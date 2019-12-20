import math
def who_is_next(names, r):
    if r <= len(names):
        return names[r-1]
    else:    
        temp = num = n = 0
        while num < r:
            n += 1
            temp = num
            num += len(names)*2**(n-1)
        return names[int((r-temp-1)/(2**(n-1)))]


    

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print (who_is_next(names,67))