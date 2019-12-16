def parse_molecule (formula):
    n = filter(str.isalpha,formula)
    return ''.join(list(n))


magnesium_hydroxide = 'Mg(OH)2'
print (parse_molecule(magnesium_hydroxide))