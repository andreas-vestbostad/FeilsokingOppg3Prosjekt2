import numpy as np
from kjorSimuleringOppg3 import *

#Definerer initialverdiene for oppgave 3b
def initialPositions3b(grid, N_p):
    particles = []
    for particle in range(N_p):
        #Denne legger halvparten av partiklene i 0
        if particle < int(round(N_p/2)): 
            particles.append(0)
        #Og resten av partiklene i 100
        else: 
            particles.append(int(round(grid/2)))
    return np.array(particles)

#Run funksjonen for oppgave 3b
def runSimulation3b(T_pArray, grid, N_x, N_p, beta_k, alpha):
    jAvarageValues = []
    print("Estimating the avarage of J for each time step... ")
    for T_p in T_pArray: #Kjører runSimulation for de ulike tidsepokene
        jVals = runSimulationVectorized(grid, initialPositions3b, beta_k, alpha, N_x, N_p, T_p, T_p * 2)
        jAvarageValues.append(np.mean(jVals))
    print("Simulation completed\n")
    #Returnerer et np.array med alle gjennomsnitsstrømningene for de ulike tidsepokene
    return np.array(jAvarageValues) 