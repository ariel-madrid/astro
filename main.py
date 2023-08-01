#Imports
import numpy as np
import matplotlib.pyplot as plt
def lehmer(seed):
    #m es igual a 2^31-1
    m = 2147483647
    a = 48271

    X = (a*seed)%m 

    #r se encuentra entre 0 y 1
    r = X/m

    return X, r

#Set initial variables
P = np.array([[0, 0.3, 0, 0, 0, 0.7, 0, 0],
              [0, 0, 0.1, 0, 0.5, 0, 0, 0.4],
              [0, 0, 0, 0, 0.6, 0, 0, 0.4],
              [0.2, 0, 0, 0, 0, 0.6, 0.2, 0],
              [0, 0, 0, 0.3, 0.7, 0, 0, 0],
              [0.1, 0, 0.9, 0, 0, 0, 0, 0],
              [0.8, 0, 0, 0, 0, 0.2, 0, 0],
              [0, 0.2, 0, 0, 0.7, 0, 0, 0.1]])

#Steps
N = 10**2

#Estado inicial
initial_state = 0

#Distribucion estacionaria
p_i = np.array([0,0,0,0,0,0,0,0])

#Se inicia desde el estado 0 => se le suma 1
p_i[initial_state] = 1
prev = initial_state

i = 0
x = 432155
while i < N:
    x, r = lehmer(x)
    #if r<=F_i(0) => X siguiente = 0
    #if F_i(j-1) < r <= F_i(j) => X siguiente = j

    #Cambiar criterio de estado actual
    current = np.random.choice([0,1,2,3,4,5,6,7], p=P[prev])

    #Sumar 1 al estado en el cual caimos dependiendo de lo decidido anteriormente
    p_i[current] += 1
    prev = current
    i += 1

#Distribucion estacionaria
dist = p_i/N
print(dist)
plt.plot(np.arange(0,8),dist)
plt.show()