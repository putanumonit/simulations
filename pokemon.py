# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 13:42:49 2016

@author: putanumonit
"""

import random

probs=[.1]*3+[.05]*6+[.025]*8+[.0125]*8+[.0064]*8+[.0032]*8+[.0016]*8+[.0008]*6+[.0004]*3
probs2=[.1]*1+[.08]*3+[.04]*8+[.02]*8+[.01]*8+[.0064]*8+[.0032]*8+[.0016]*8+[.0008]*8+[.0004]*4
probs3=[.08]*4+[.04]*8+[.02]*9+[.01]*9+[.005]*9+[.0025]*9+[.00125]*9+[.000625]*6+[.0003125]*3

## Creates a list of probability bucket limits based on the bucket probabilities in probs
def setlims(pr):
    pl=[pr[1]]
    for i in range(1,len(pr)):
        pl.append(pl[i-1]+pr[i])
    return pl

## Simulates a single game of consecutive pokemon observations 
def game(pl):
    n = len(pl)
    caught = [0] * n
    m=max(pl)
    turn = 0
    ncaught = 0
    while ncaught < n:
        turn += 1
        x = random.uniform(0,m)
        p = 0
        while x>pl[p]:
            p += 1
        if caught[p] == 0:
            caught[p] = turn
            ncaught += 1
    return caught

## Simulates several games, returns a list of the turn numbers each game took    
def sim(nsims, pl):
    maxturns=[]
    for i in range(nsims):
        game_result=game(plims)
        maxturns.append(max(game_result))
    return maxturns
    
