def case_3_4_2_1(A1c, A2c, A3c):
    """ Returns True if |Aic & Ajc| <= |A1c & A2c & A3c| for all i!=j """
    temp = len(A1c & A2c & A3c) + 1
    return len(A1c & A2c) <= temp and len(A1c & A3c) <= temp and len(A2c & A3c) <= temp

def case_3_4_2_2(A1c, A2c, A3c):
    """ Returns the Aic, Ajc such that |A1c & A2c| > |A1c & A2c & A3c| + 2 """
    temp = len(A1c & A2c & A3c) + 2
    if len(A1c & A2c) > temp:
        return A1c, A2c
    if len(A1c & A3c) > temp:
        return A1c, A3c
    if len(A2c & A3c) > temp:
        return A2c, A3c
    raise Exception("Case 3.4.2.2: no such set.")

case_3_4_2_2(set(),set(),set())
