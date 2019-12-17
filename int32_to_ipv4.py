def int32_to_ip(int32):
    a=bin(int32)
    b=a[2:len(a)].zfill(32)
    return "{}.{}.{}.{}".format(int(b[0:8],2),int(b[8:16],2),int(b[16:24],2),int(b[24:32],2))