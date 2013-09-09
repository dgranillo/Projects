#!/usr/bin/env python2.7
"""
 Closest Pair Problem - The closest pair of points problem or closest pair
 problem is a problem of computational geometry. Given 'n' points in metric
 space, find a pair of points with the smallest distance between them

Author: Dan Granillo <dan.granillo@gmail.com>

"""

import random
import math

my_points = []
d_points = {}
d_distances = {}
sorted_d = []

def gen_points():
    for i in range(100): # Creating points to play with
        x = random.randrange(-100,100)
        y = random.randrange(-100,100)
        z = random.randrange(-100,100)
        my_points.append((x, y, z))
    for i in range(len(my_points)): # Dictionary of points to give each a name
        d_points[i] = my_points[i]

def get_distance(point_a, point_b):
    x1 = point_a[0]
    y1 = point_a[1]
    z1 = point_a[2]
    x2 = point_b[0]
    y2 = point_b[1]
    z2 = point_b[2]

    d = math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return d

def get_distances(dictionary):
    d_length = len(dictionary.values())
    for i in range(d_length-1):
        for j in range (i+1,d_length):
            d_distances[dictionary[i], dictionary[j]] = get_distance(dictionary[i],dictionary[j])

def sort_distances(distances):
    for key, value in sorted(distances.iteritems(), key = lambda (k,v):(v,k)):
        sorted_d.append("%s, %.03f" %(key, value))
    return sorted_d[0]

if __name__ == '__main__':
    gen_points()
    get_distances(d_points)
    print sort_distances(d_distances)
