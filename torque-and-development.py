#!/bin/python3
# https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs


import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def buildLibraries(n, c_lib, cities):
    return n * c_lib


def visit_all_heighbours(i, n, edges, visited):
    total_roads = 0
    visited[i] = 2
    for edge in edges:
        if edge[0] - 1 == i and visited[edge[1] - 1] == 0:
            total_roads += 1
            total_roads += visit_all_heighbours(edge[1] - 1, n, edges, visited)
        if visited[edge[0] - 1] == 0 and edge[1] - 1 == i:
            total_roads += 1
            total_roads += visit_all_heighbours(edge[0] - 1, n, edges, visited)
    visited[i] = 1
    return total_roads


def buildRoads(n, c_lib, c_road, cities):
    total_cost = 0
    visited = [0] * n
    for i in range(0, n):
        if visited[i] == 0:
            total_cost += c_lib
            total_cost += visit_all_heighbours(i, n, cities, visited) * c_road
    return total_cost


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return buildLibraries(n, c_lib, cities)
    else:
        return buildRoads(n, c_lib, c_road, cities)

if __name__ == '__main__':
    # fptr = open(os.environ['console.out'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(str(result))
        # fptr.write(str(result) + '\n')

    # fptr.close()
