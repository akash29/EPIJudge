from test_framework import generic_test


def divide(x, y):
    # TODO - you fill in here.
    if x < y:
        return 0
    else:
        count = 0
        temp_y = y
        while x-y >= 0:
            temp_power = 0
            while x >= y:
                y <<= 1
                if y > x:
                    y >>= 1
                    break
                temp_power += 1

            x = x - y
            y = temp_y
            count += 1 << temp_power

        return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_divide.py",
                                       "primitive_divide.tsv", divide))
