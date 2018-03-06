# Uses python3

import sys
import math

# Algorithm:
# 	1. Store the X, Y coordinates and gold G at each Point
# 	2. Using dynamic programming(memoization techinque) find the max gold Charle can make at each point starting from 1st point till that point
#	3. Recursively find out all the maximum gold values
#	4. return the maximum gold that charlie can make starting from 1st point and reaching Nth point
# Analysis:
# 	1. Running Time: O(N^2)
# 	2. Space Complexity: O(N)
#		Input X Coordinate: O(N)
#		Input Y Coordinate: O(N)
#		Input Gold at Point: O(N)
#		Max Gold Array: O(N)
#		Temp Gold Array: O(N)


# Function to find the eucledianDistance
def eucledianDistance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


# Function to calculate the maximum amount of gold Charlie can make
def maxGold(N, X, Y, G):
    # initialize an empty gold array
    gold = []
    # append G[0] when the user just traverses 1st point
    gold.append(G[0])

    for i in range(1, N):
        tempGold = []
        for j in range(0, i + 1):
            # if i & j are equal find the max of the tempGold
            if i == j:
                gold.append(max(tempGold))
            # else add the gold at the ith point to max gold collected at jth point and subtract the eucledian distance between i & j
            else:
                tempGold.append(
                    gold[j] + G[i] - eucledianDistance(X[j], Y[j], X[i], Y[i]))

    # return the max gold collected starting from 1 to N
    return gold[N - 1]


# main method
if __name__ == '__main__':
    # read user input
    input = sys.stdin.read()
    # split the input based on white space characters
    data = list(map(int, input.split()))
    # move the first value the number of points to N
    N = data[0]
    # move all the X coordinates to X
    X = data[1::3]
    # move all the Y coordinates to Y
    Y = data[2::3]
    # move all the Gold hidden at the coordinate to G
    G = data[3::3]

    # find the maximum gold that Charlie can make and print it rounded to 6 digits after decimal
    print(round(maxGold(N, X, Y, G), 6))