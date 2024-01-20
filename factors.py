#!/usr/bin/python3
import sys


def factorize_number(n):
    for i in range(2, n):
        if n % i == 0:
            return (i, n)


if len(sys.argv) != 2:
    print("Usage: python factors.py <file>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as file:
    for line in file:
        number = int(line.strip())
        factors = factorize_number(number)
        print(f"{number}={factors[0]}*{factors[1]}")
