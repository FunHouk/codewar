def first_non_repeating_letter(string):
    str = string.lower()    
    for n,item in enumerate(str):
        if str.count(item) == 1 :
            return string[n]
    return ''