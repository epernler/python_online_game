def p1_f1():
    return "P1_F1"


def p1_f2():
    return "P1_F2"


def p2_f1():
    return "P2_F1"


def p2_f2():
    return "P2_F2"


def delete_p():
    return "DELETE"


def default():
    return "Nothing bro"


switch_case = {
    1: p1_f1,
    2: p1_f2,
    3: p2_f1,
    4: p2_f2,
    5: delete_p,
    6: default
}


def switch(x):
    return switch_case.get(x, default)()


D_MSG = "CLIENT_DISCONNECTED"
