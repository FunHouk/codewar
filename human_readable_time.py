def make_readable(seconds):

    h = seconds // 3600
    b = seconds - h * 3600
    m =  b // 60
    s = b - m * 60

    return  "%02d:%02d:%02d" % (h, m, s)    
print(make_readable(358999))