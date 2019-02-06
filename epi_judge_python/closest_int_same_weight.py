from test_framework import generic_test


def closest_int_same_bit_count(x):
    # TODO - you fill in here.
    lsb = x & 1
    temp = x
    count = 1
    while temp:
        if temp >> 1 & 1 == lsb:
            count += 1
            temp >>= 1
        else:
            break
    x ^= 1 << count | 1 << (count-1)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
