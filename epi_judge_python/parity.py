from test_framework import generic_test


def parity(x):
    # TODO - you fill in here.
    num_count = 0
    while x:
        num_count += x&1
        x>>=1
    return 0 if num_count%2 == 0 else 1



if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
