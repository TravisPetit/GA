from functions import three_two_domination

def case_3_4_2_1(A1c, A2c, A3c):
    """ Returns True if |Aic & Ajc| <= |A1c & A2c & A3c| for all i!=j """
    temp = len(A1c & A2c & A3c) + 1
    return len(A1c & A2c) <= temp and len(A1c & A3c) <= temp and len(A2c & A3c) <= temp

def case_3_4_2_2(A1c, A2c, A3c):
    """ Returns True if there is an Aic, Ajc : |Aic & Ajc| > |A1c & A2c & A3c| + 2 """
    return three_two_domination(A1c, A2c, A3c) is not None

def case_3_4_3_1(A1c, A2c, A3c):
    """ Same as 3.4.2.1 """
    return case_3_4_2_1(A1c, A2c, A3c)

def case_3_4_3_2(A1c, A2c, A3c):
    """ Same as 3.4.2.2 """
    return case_3_4_2_2(A1c, A2c, A3c)
