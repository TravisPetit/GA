def case_3_4_2_1(A1c, A2c, A3c):
    """ Returns True if |Aic & Ajc| <= |A1c & A2c & A3c| for all i!=j """
    temp = len(A1c & A2c & A3c) + 1
    return len(A1c & A2c) <= temp and len(A1c & A3c) <= temp and len(A2c & A3c) <= temp
