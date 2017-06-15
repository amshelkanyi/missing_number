def find_missing(A , B):
    add_A = sum(A)
    add_B = sum(B)

    if add_A == add_B:
        return 0
    if add_A > add_B:
        return add_A-add_B
    else:
        return add_B-add_A
