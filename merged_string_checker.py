
def is_merge(s, part1, part2):
    a1 = []
    a2 = []
    if len(s) != len(part1) + len(part2) or sorted(s) != sorted(part1+part2) :
        return False
    else:
        for i in part1:
            n = s.index(i)
            a1.append(n)
        for j in part2:
            m = s.index(j)
            a2.append(m)
    if a1 != sorted(a1) or a2 !=sorted(a2):
        return False
    else:
        return True

print (is_merge('codewars', 'code', 'wars'))

