def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[0] + 'ay' if word.isalpha() else word for word in lst])

print (pig_it('Hello World !'))
