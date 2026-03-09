import numpy as np
import scipy
from kjorSimuleringOppg3 import *
    
def initialPositions3e(grid, N_p): #Hentet fra oppgave b
    particles = []
    for particle in range(N_p):
        #Denne legger halvparten av partiklene i 0
        if particle < int(round(N_p/2)): 
            particles.append(0)
        #Og resten av partiklene i 100
        else: 
            particles.append(int(round(grid/2)))
    return np.array(particles)

# grid, initialPositions, beta_k, alpha, N_x, N_p, T_p, totalSteps

def runSimulation3b(T_pArray, grid, N_x, N_p, alpha, beta_k):
    jMeanValues = []
    print("Estimating the avarage of J for each time step... ")
    for T_p in T_pArray:               #Itererer gjennom de ulike tidsepokene
        jVals = runSimulationVectorized(grid, initialPositions3e, beta_k, alpha, N_x, N_p, int(T_p), 2 * int(T_p))
        jMeanValues.append(np.mean(jVals))
    print("Simulation completed\n")
    return np.array(jMeanValues)

#Definerer den analytisk løsningen
def analyticalSolution(alpha, T_p = 500, N_x = 200):
    lProduct = N_x/(4*T_p)
    rProduct = scipy.special.erfc(((alpha*N_x)/2)*np.sqrt(3/T_p)) - scipy.special.erfc((((1-alpha)*N_x)/2)*np.sqrt(3/T_p))
    analjAvg = lProduct * rProduct
    return analjAvg
