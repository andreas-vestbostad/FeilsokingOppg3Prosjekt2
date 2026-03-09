import numpy as np
import scipy
from kjorSimuleringOppg3 import *

#Definerer initialverdiene for oppgave 3c (lik som oppgave b)
def initialPositions3c(grid, N_p):
    particles = []
    for particle in range(N_p):
        #Denne legger halvparten av partiklene i 0
        if particle < int(round(N_p/2)): 
            particles.append(0)
        #Og resten av partiklene i 100
        else: 
            particles.append(int(round(grid/2)))
    return np.array(particles)

#Definerer den analytisk løsningen
def analyticalSolution(alpha, T_p = 500, N_x = 200):
    lProduct = N_x/(4*T_p)
    rProduct = scipy.special.erfc(((alpha*N_x)/2)*np.sqrt(3/T_p)) - scipy.special.erfc((((1-alpha)*N_x)/2)*np.sqrt(3/T_p))
    analjAvg = lProduct * rProduct
    return analjAvg

#Kjører sumuleringer for vær verdi av alpha
def runSimulation3c(alphaArray, beta_k, T_p, N_x, N_p, grid):
    jMeanValues = []
    for alpha in alphaArray:
        jVals = runSimulationVectorized(grid, initialPositions3c, beta_k, alpha, N_x, N_p, T_p, 2 * T_p)
        jMeanValues.append(np.mean(jVals))
    return jMeanValues
