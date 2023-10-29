#!/usr/bin/python3

import sys


# Function to factorize a number
def factorize(n):
    if n <= 1:
        warning = "Invalid input:"
        print(f"{warning} {n} is not a valid natural number greater than 1.")
        return
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if len(factors) == 1:
        print(f"{factors[0]}=1*{factors[0]}")
    else:
        p, q = factors[0], 1
        for factor in factors[1:]:
            q *= factor
        print(f"{p*q}={p}*{q}")


def main(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                number = int(line.strip())
                factorize(number)
    except FileNotFoundError:
        print(f"Error: Unable to open file {filename}")
    except ValueError:
        print(f"Invalid input: {line.strip()} is not a valid natural number.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
    else:
        main(sys.argv[1])
