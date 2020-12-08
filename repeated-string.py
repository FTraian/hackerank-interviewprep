#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    if n < len(s):
        return count_As(s, n)
    else:
        repetitions = n // len(s)
        return repetitions * count_As(s, len(s)) + count_As(s, n % len(s))


def count_As(s, n):
    counter = 0
    for c in range(0, n):
        if s[c] == 'a':
            counter += 1
    return counter


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
