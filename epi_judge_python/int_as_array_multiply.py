from test_framework import generic_test


def multiply(num1, num2):
    # TODO - you fill in here.

    if num1[0] == 0 or num2[0] == 0:
        return [0]
    else:
        res_arr = [0] * (len(num1) + len(num2))

        final_sign = 1
        if num1[0] * num2[0] < 0:
            final_sign *= -1
        num1[0] = abs(num1[0])
        num2[0] = abs(num2[0])
        for i, j in enumerate(reversed(num1)):
            carry = 0
            for k, p in enumerate(reversed(num2)):
                res_index = (len(res_arr) - 1) - (i + k)
                sum_num = j * p + carry + res_arr[res_index]
                sum_val = sum_num % 10
                carry = sum_num // 10
                res_arr[res_index] = sum_val
                if k == len(num2) - 1 and carry > 0:
                    res_arr[res_index - 1] += carry

        if res_arr[0] == 0:
            res_arr = res_arr[1:]

        res_arr[0] = res_arr[0] * final_sign

        return  res_arr

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
