#!/bin/python3

import math
import os
import random
import re
import sys
import requests

#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#


def add_goals(data, home):
    total = 0
    for g in data:
        if home:
            total += int(g['team1goals'])
        else:
            total += int(g['team2goals'])
    return total


def get_goals(competition, year, winner, home):
    total = 0
    page = 1
    if home:
        team_param = '&team1='
    else:
        team_param = '&team2='
    json = requests.get('https://jsonmock.hackerrank.com/api/football_matches?'
                        + 'competition=' + competition
                        + '&year=' + str(year)
                        + team_param + winner
                        + '&page=' + str(page)).json()
    data = json['data']
    while len(data) > 0:
        total += add_goals(data, home)
        page += 1
        data = requests.get('https://jsonmock.hackerrank.com/api/football_matches?'
                            + 'competition=' + competition
                            + '&year=' + str(year)
                            + team_param + winner
                            + '&page=' + str(page)).json()['data']
    return total


def getWinnerTotalGoals(competition, year):
    winner = competition_winner(competition, year)
    total = get_goals(competition, year, winner, True)
    total += get_goals(competition, year, winner, False)
    return total


def competition_winner(competition, year):
    json = requests.get('https://jsonmock.hackerrank.com/api/football_competitions?'
                        + 'name=' + competition
                        + '&year=' + str(year)).json()
    return json['data'][0]['winner']


if __name__ == '__main__':
    competition = "La Liga"
    year = 2012
    print(getWinnerTotalGoals(competition, year))