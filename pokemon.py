# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 13:42:49 2016

@author: putanumonit
"""

import random

probs=[.08]*4+[.04]*8+[.02]*9+[.01]*9+[.005]*9+[.0025]*9+[.00125]*9+[.000625]*6+[.0003125]*3
plims = setlims(probs)
bigsim=sim(10000,plims)

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
        game_result=game(pl)
        maxturns.append(max(game_result))
    return maxturns
    
## Adds the functionality of returning the number of the last pokemon caught
def game2(pl):
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
    return [p, caught]
    
## Adds the functionality of returning the number and rarity type of the last pokemon caught   
def sim2(nsims, pl):
    simresult=[]
    for i in range(nsims):
        game_result=game2(pl)
        if game_result[0] < 57:
            ptype = "normal"
        elif game_result[0] < 63:
            ptype = "epic"
        else:
            ptype = "mystical"
        simresult.append([max(game_result[1]), game_result[0], ptype])
    return simresult
