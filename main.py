#Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random
import csv
import pandas as pd
#Function to define the next state based on the current cdf and prob r
def next_state(current, r):
    if (r <= current[0]):
        return 0
    else:
        for i in range(len(current)):
            if (i > 0):
                if (current[i-1] < r and current[i] >= r):
                    return i

#Set initial variables
P = np.array([[0, 0.3, 0, 0, 0, 0.7, 0, 0],
              [0, 0, 0.1, 0, 0.5, 0, 0, 0.4],
              [0, 0, 0, 0, 0.6, 0, 0, 0.4],
              [0.2, 0, 0, 0, 0, 0.6, 0.2, 0],
              [0, 0, 0, 0.3, 0.7, 0, 0, 0],
              [0.1, 0, 0.9, 0, 0, 0, 0, 0],
              [0.8, 0, 0, 0, 0, 0.2, 0, 0],
            [0, 0.2, 0, 0, 0.7, 0, 0, 0.1]])

#Optimizar obtencion de la cdf (pendiente)
cdf = []
for state in P:
    tmp = []
    acumulado = 0
    for i in range(len(state)):
        if (i==0):
            tmp.append(state[i])
            acumulado = state[i]
        else:
            acumulado = acumulado + state[i]
            tmp.append(acumulado)
        
    cdf.append(tmp)

#Steps
N = 10**3

#Estado inicial -> puede ser cualquiera
initial_state = 7

#Distribucion estacionaria
p_i = np.array([0,0,0,0,0,0,0,0])

#Se inicia desde el estado 0 => se le suma 1
p_i[initial_state] = 1

prev = initial_state

i = 0

#Save results to animate bar plot
f = open("./steady.csv", 'w')
wr = csv.writer(f)
wr.writerow(['index','0','1','2','3','4','5','6','7'])
while i < N:
    #Utilizar la cdf (cumulative function distribution) para definir el siguiente estado
    #if r<=F_i(0) => X siguiente = 0
    #if F_i(j-1) < r <= F_i(j) => X siguiente = j

    #Numero aleatorio distribuido uniformemente entre 0 y 1
    r = np.random.uniform(0,1)
    
    #Nuevo estado actual
    current = next_state(cdf[prev], r)
    #Sumar 1 al estado en el cual caimos dependiendo de lo decidido anteriormente
    p_i[current] += 1
    dist = p_i/N
    wr.writerow([i, dist[0], dist[1], dist[2], dist[3], dist[4], dist[5], dist[6], dist[7]])
    prev = current
    i += 1

f.close()

fig, ax = plt.subplots()
plt.bar(['0','1','2','3','4','5','6','7'], dist)
ax.set_title('Steady State Distribution')
ax.set_xlabel('State')
ax.set_ylabel('Prob')
plt.savefig("./steady-bar.png")

