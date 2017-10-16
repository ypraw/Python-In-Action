
import sys


def trianglePattern(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            sys.stdout.write(" ")
        sys.stdout.write("#")

        if 1 < i <= n - 1:
            for k in range(1, 2 * i - 2):
                sys.stdout.write(" ")
            sys.stdout.write("#")
        elif i == n:
            for k in range(1, 2 * i - 1):
                sys.stdout.write("#")
        print()


# Call Method
trianglePattern(10)
