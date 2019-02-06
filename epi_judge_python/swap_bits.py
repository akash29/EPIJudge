from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    if x >> i & 0x1 != x >> j &0x1:
        x^=1<<j | 1<<i
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits))
