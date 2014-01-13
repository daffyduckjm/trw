import numpy as np
import random

#trasa as array containing '<' or '>' or '^' or 'v'
#zwrot as '<' or '>' or '^' or 'v' what direction are we heading?
def tlumacz(trasa,zwrot):
    tl = []
    for krok in trasa:
        if krok == zwrot: pass
        else: 
            if zwrot=='^':
                if krok=='<': tl.append('lewo')
                if krok=='>': tl.append('prawo')
                if krok=='v': 
                    tl.append('lewo')
                    tl.append('lewo')
            if zwrot=='v':
                if krok=='<': tl.append('prawo')
                if krok=='>': tl.append('lewo')
                if krok=='^': 
                    tl.append('lewo')
                    tl.append('lewo')

            if zwrot=='<':
                if krok=='^': tl.append('prawo')
                if krok=='v': tl.append('lewo')
                if krok=='>': 
                    tl.append('lewo')
                    tl.append('lewo')

            if zwrot=='>':
                if krok=='v': tl.append('prawo')
                if krok=='^': tl.append('lewo')
                if krok=='<': 
                    tl.append('lewo')
                    tl.append('lewo')

        tl.append('prosto')
        zwrot=krok
    return tl

def losowa_trasa(dlugosc):
    trasa=[]
    for i in range(dlugosc): trasa.append(random.choice(['<','>','^','v']))
    return np.array(trasa)
