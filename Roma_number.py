roman=('IV')
a = 0
i=0
Roma = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for i in range(len(roman)):
    if  i != int(len(roman)-1) :
        if Roma[roman[i]] < Roma[roman[i+1]] :
            a -= Roma[roman[i]]
        else :
            a += Roma[roman[i]]
    else :
        a += Roma[roman[i]]
    i += 1

def solution(roman):
    dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += dict[c]
        elif last > dict[c]:
            total -= dict[c]
        else:
            total += dict[c]
        last = dict[c]
    return total   