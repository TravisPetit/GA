#def case_3_4_2(A1c, A2c, A3c):
#    """ Returns the two sets Aic, Ajc such that |Aic & Ajc| > |A1c & A2c & A3c| + 2 """
#    if len(A1c & A2c) > len(A1c & A2c & A3c) + 2:
#        return A1c, A2c
#    if len(A1c & A3c) > len(A1c & A2c & A3c) + 2:
#        return A1c, A3c
#    if len(A2c & A3c) > len(A1c & A2c & A3c) + 2:
#        return A2c, A3c
#    print("something went wrong")

def case_3_4_2_1(A1c, A2c, A3c):
    temp = len(A1c & A2c & A3c) + 1
    return len(A1c & A2c) > temp and len(A1c & A3c) > temp and len(A2c & A3c) > temp
