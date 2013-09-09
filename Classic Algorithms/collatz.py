#!/usr/bin/env python2.7
"""
 Collatz Conjecture - Start with a number n > 1. Find the number of steps it
 takes to reach 1 using the following process. If 'n' is even, divide by 2. If 
 'n' is odd, multiply by 3 and add 1.

Author: Dan Granillo <dan.granillo@gmail.com>

"""

class CollatzNumber(object):
    steps = 0
    def __init__(self, num):
        self.num = num

    def num_sort(self):
        while True:
            if self.num > 1:
                self.steps += 1
                if self.num % 2 == 0:
                    self.even_func(self.num)
                elif self.num % 2 == 1:
                    self.odd_func(self.num)
            else:
                break
        print self.steps

    def even_func(self, i):
        self.num = i / 2

    def odd_func(self, i):
        self.num = i * 3 + 1

if __name__ == '__main__':
    n = CollatzNumber(int(raw_input("Enter number: ")))
    n.num_sort()
