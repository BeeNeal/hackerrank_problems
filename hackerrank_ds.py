import os
import sys

# given a list of strings, and list of queries, find how many times each
# of those queries appear in the string

def findSuffix(collections, queryString):

    # for q in queryString.split():
    #     print collections.count(q)
    # return

    values = {}
    for _ in range(int(raw_input())):
        values[raw_input()] += 1
    for _ in range(int(raw_input())):
        print(values[raw_input()])

def arrayManipulation(n, queries):

    # would be better to calculate the overlapping indices rather than actually
    # change the list, since only need to return the max
    
    start_lst = [0] * n
# queries here are list of lists

    for q in queries:
        # make first pos zero index
        start_i = q[0] - 1
        fin_i = q[1]
        update = q[2]

        for i in range(start_i, fin_i):
            start_lst[i] += update
    return max(start_lst)

    # updated_indices = {}
    # for i in range(1, n + 1):
    #     updated_indices[i] = updated_indices.get(updated_indices[i], 1) + 1

    # for i in range()
        # remember, 0 index is pos 1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    # fptr.write(str(result) + '\n')

    # fptr.close()
