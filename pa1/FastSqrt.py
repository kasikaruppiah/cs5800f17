# Uses python3

# Algorithm:
#	1. Read the user input
#	2. Run the Babylonian method to find the square root of the algorithm
# Analysis:
#	1. Running Time:log n
#	2. Space Complexity: O(1)

# returns the square root of the input


def getSquareRoot(n):
    guess = 1
    while abs(pow(guess, 2) - n) > 0.01:
        guess = (guess + n / guess) / 2

    return guess


if __name__ == '__main__':
    # Read the user input from system input
    n = float(input())
    print(getSquareRoot(n))
