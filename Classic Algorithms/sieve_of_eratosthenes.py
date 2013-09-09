#!/usr/bin/env python2.7
"""
 Sieve of Eratosthenes - The sieve of Eratosthenes is one of the most efficient
 ways to find all of the smaller primes (below 10 million or so).

 Author: Dan Granillo <dan.granillo@gmail.com>
 
"""

def genNums(x):
    nums = []
    if x >= 2:
        nums = range(2, x+1)
    else:
        print 'X must be no smaller than 2'
    return nums

def sortNums(nums):
    primes = []
    composites = []
    poss_primes = [2]
    for i in nums:
        for j in nums:
            if j > i:
                if j % i == 0:
                    composites.append(j)
                else:
                    poss_primes.append(j)
    for x in poss_primes:
        if x not in composites and x not in primes:
            primes.append(x)
    print 'primes:', primes

if __name__ == "__main__":
    sortNums(genNums(int(raw_input('Enter x: '))))