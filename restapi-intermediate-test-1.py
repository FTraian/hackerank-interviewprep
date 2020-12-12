#!/bin/python3

import math
import os
import random
import re
import sys
import requests


#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

def get_draws_for(score, year):
    total = 0
    page = 1
    data = getAPIData(year, page, score)
    while len(data['data']) > 0:
        total += len(data['data'])
        page += 1
        data = getAPIData(year, page, score)
    return total


def getAPIData(year, page, goals):
    return requests.get('https://jsonmock.hackerrank.com/api/football_matches'
                        + '?year=' + str(year)
                        + '&page=' + str(page)
                        + '&team1goals=' + str(goals)
                        + '&team2goals=' + str(goals)
                        ).json()


def getNumDraws(year):
    total = 0
    for score in range(0, 11):
        total += get_draws_for(score, year)
    return total


if __name__ == '__main__':
    year = int(input())
    print(getNumDraws(year))