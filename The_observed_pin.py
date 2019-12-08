import itertools
def get_pins(observe):
    likely_num = {'1':[1,2,4],'2':[1,2,3,5],'3':[2,3,6],'4':[1,4,5,7],'5':[2,4,5,6,8],'6':[3,5,6,9,],'7':[4,7,8],'8':[5,7,8,9,0],'9':[6,8,9],'0':[0,8]}
    num = []
    p_num = []
    for i in observe:
        num.append(likely_num[i])
    result_num = list(itertools.product(*num))
    for pin in result_num:
        for n in pin:
            p_num.append(str(n))
    result = ["".join(p_num[i:i+len(observe)]) for i in range(0, len(p_num), len(observe))]
        
    #p_num = "".join(p_num)
    #print (p_num)
    #    for n in pin:
    #        p_num.append(n)
    #    pin_num = "\""+str(p_num)+"\""
    #    p_num.append(pin_num)
    return result

print (get_pins ('1217'))