#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#

"""
A widget manufacturer is facing unexpectedly high demand for its new product,. They would like to satisfy as many customers as possible. Given a number of widgets available and a list of customer orders, what is the maximum number of orders the manufacturer can fulfill in full?

Function Description

Complete the function filledOrders in the editor below. The function must return a single integer denoting the maximum possible number of fulfilled orders.

filledOrders has the following parameter(s):

    order :  an array of integers listing the orders

    k : an integer denoting widgets available for shipment

Constraints

1 ≤ n ≤  2 x 105

1 ≤  order[i] ≤  109

1 ≤ k ≤ 109

Sample Input For Custom Testing

2

10

30

40

Sample Output

2
"""

def filledOrders(order, k):
    # Write your code here
    total = 0
    for i, v in enumerate(sorted(order)):
        if total + v <= k:
            total += v
        else:
            return i
    else:
        return len(order)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    order_count = int(input().strip())

    order = []

    for _ in range(order_count):
        order_item = int(input().strip())
        order.append(order_item)

    k = int(input().strip())

    result = filledOrders(order, k)

    fptr.write(str(result) + '\n')

    fptr.close()
