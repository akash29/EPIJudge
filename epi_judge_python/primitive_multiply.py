from test_framework import generic_test


def multiply(x, y):
    # TODO - you fill in here.
    old_x = x
    while y:
        temp = old_x
        while temp:
            carry = x & temp
            x ^= temp
            temp = carry << 1

        y = subtract(y, 1)

    return x


def subtract(x, y):
    while y:
        borrow = ~x & y
        x ^= y
        y = borrow << 1
    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
