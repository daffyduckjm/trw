import numpy as np
from random import choice
import time
import os

global mapa
mapa=np.chararray((5,5))


#########
dlugosc = 3
possible_moves=['<','>','^','v']
startowe_x = 4
startowe_y = 4

while (True):
	mapa[:]='b'
	mapa[np.random.randint(5),np.random.randint(5)]='C'
	mapa[np.random.randint(5),np.random.randint(5)]='N'
	mapa[np.random.randint(5),np.random.randint(5)]='P'
	mapa[np.random.randint(5),np.random.randint(5)]='H'
	mapa[startowe_x,startowe_y]='S'
	if ('C' in mapa) and ('N' in mapa) and ('P' in mapa) and ('H' in mapa) and ('S' in mapa): 
                break



#pozycja_startowa=(4,4)# Poczatkowa pozycja



def random_way(dlugosc):
        way=[]
	for i in range(dlugosc): way.append(choice(possible_moves))
	return np.array(way)


#def losowa_trasa(dlugosc):
#	trasa=[]
#	for i in range(dlugosc): trasa.append(np.random.choice(['<','>','^','v']))
#	return np.array(trasa)

def zakrety(way):
	zakretow=0
	if len(way)<2: return 0
	else:
		for i in range(len(way)-1):
			if (way[i]!=way[i+1]): zakretow+=1
	return zakretow

def jakosc(way):
	return len(way)+zakrety(way)

def show_map(x,y,i,wait):
    odczyt = mapa[x,y]
    mapa[x,y] = '*'
    time.sleep(wait)
    os.system('clear')
    print(i)
    print(mapa)
    mapa[x,y] = odczyt

    
### ruch po spirali # spirala nienawisci, spirala...
moves = np.array(['^','^','^','^','<','<','<','<', 'v', 'v', 'v', 'v', '>', '>', '>', '^', '^', '^', '<', '<', 'v', 'v','>', '^'])



# function sciezka - ruchy, ktore bedziemy wykonywac; mapa - mapa uzyta; wait - ile czasu miedzy robieniem ruchow
def moving(sciezka, mapa, wait):
    time.sleep(wait)
    os.system('clear')
    x = startowe_x
    y = startowe_y
    mapa[x,y] = '*'
    print(sciezka)
    print(mapa)
    mapa[x,y] = 'S'
    for i in sciezka:
        if i == '<' and y!=0:
            y-=1
            show_map(x,y,i,wait)
        elif i == '>' and y!=4: 
            y+=1
            show_map(x,y,i,wait)

        elif i == '^' and x!=0: 
            x-=1
            show_map(x,y,i,wait)
            
        elif i == 'v' and x!=4: 
            x+=1
            show_map(x,y,i,wait)
            
        else: 
            print('Talk to the wall')
            break
    time.sleep(wait)
    os.system('clear')
    print(sciezka)
    mapa[x,y] = '*'
    return(mapa)




#print(mapa)
#print(random_way(dlugosc))
#print('number of turns: '+str(zakrety(random_way(dlugosc))))
#print('jakosc trasy: '+str(jakosc(random_way(dlugosc))))

print(moving(moves, mapa, 1))
