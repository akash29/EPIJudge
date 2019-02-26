from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.
    res_A = [0] * (len(A) + 1)
    to_sum = 1
    for i in range(len(A) - 1, -1, -1):
        sum_val = A[i] + to_sum
        sum_res = sum_val % 10
        res_A[i + 1] = sum_res
        to_sum = sum_val // 10

    if to_sum != 0:
        res_A[0] = to_sum
    else:
        res_A = res_A[1:]

    return res_A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
