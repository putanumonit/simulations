# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 13:42:49 2016

@author: yfalkovich
"""

import random

probs=[.1]*3+[.05]*6+[.025]*8+[.0125]*8+[.0064]*8+[.0032]*8+[.0016]*8+[.0008]*6+[.0004]*3
plims=[probs[1]]
for i in range(1,len(probs)):
    plims.append(plims[i-1]+probs[i])
    
def game(pl):
    caught = [0] * 58
    m=max(pl)
    turn = 0
    ncaught = 0
    while ncaught < 58:
        turn += 1
        x = random.uniform(0,m)
        p = 0
        while x>pl[p]:
            p += 1
        if caught[p] == 0:
            caught[p] = turn
            ncaught += 1
    return caught
    
def sim(nsims):
    maxturns=[]
    for i in range(nsims):
        game_result=game(plims)
        maxturns.append(max(game_result))
    return(float(sum(maxturns))/len(maxturns))
    