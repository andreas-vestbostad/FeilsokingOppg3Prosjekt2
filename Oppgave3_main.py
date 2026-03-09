#importerer bibloteker på nytt så jeg ikke må kjøre hele koden
import matplotlib.pyplot as plt 
import scipy
import numpy as np
import random
from kjorSimuleringOppg3 import *
from Oppgave3a import *
from Oppgave3b import *
from Oppgave3c import *
from Oppgave3e import *

# Oppgave 3a 
# Konstanter
alpha = 0.8                     #Angir formen på potensial funksjonen
N_x   = 100                     #Periode på potensialfunksjonen
beta_k = 1000                   #Proposjonal med forholdet mellom temperaturen og potensialet

#Tid
T_p   = 500                     #1 Tidsperiode
totalSteps = 20*T_p              #Totalt antall steg
cycles = int(totalSteps/(2*T_p)) #Antall syklusser
timeStepsPerCycle = 2 * T_p     #Antall tidsstep per cyklus

#Partikler oppgave 3a
N_p = 12 * N_x

#Område
grid = 200                      #Lengde på område

#Initial posisjoner for oppgave 3a


#Generer J-verdier med alpha = 0.8
print("Computing Simulation 1...")
jVals08 = runSimulationVectorized(grid, initialPositions3a, beta_k, alpha, N_x, N_p, T_p, totalSteps)
print("Simulation completed. \n")

# Konverter til numpy array for enkel slicing
alpha08JArray = np.array(jVals08)   #Numpy array av j-verdiene med alpha lik 0.8
print("Simulering med alpha = 0.8")
print("Syklys index (n):| Gjennomsnitlig J-verdi")

for n in range(cycles):
    startId = n * timeStepsPerCycle
    endId = (n+1) * timeStepsPerCycle

    jMean = np.mean(alpha08JArray[startId:endId])

    print(f"{n:^16} | {jMean:18.6e}")


#Generer J-verdier med alpha = 0.1
alpha = 0.1
print("\nSimulation 2")
jVals01 = runSimulationVectorized(grid, initialPositions3a, beta_k, alpha, N_x, N_p, T_p, totalSteps)

#Gjør det samme med alpha = 0.1
alpha01JArray = np.array(jVals01)   #Numpy array av j-verdiene med alpha lik 0.1
print("Simulering med alpha = 0.1")
print("Syklys index (n):| Gjennomsnitlig J-verdi")

for n in range(cycles):
    startId = n * timeStepsPerCycle
    endId = (n+1) * timeStepsPerCycle

    jMean = np.mean(alpha01JArray[startId:endId])

    print(f"{n:^16} | {jMean:18.6e}")
"""

# Oppgave 3b 
# Konstanter
alpha = 0.8                     #Angir formen på potensial funksjonen
N_x   = 100                     #Periode på potensialfunksjonen
beta_k = 1000                   #Proposjonal med forholdet mellom temperaturen og potensialet

#Tid
T_pArray = np.arange(1, 1001, 20)    #Liste med ulike tidsepoker
totalSteps = 20 * T_pArray           #Totalt antall steg

#Partikler oppgave 3a
N_p = 40 * N_x

#Område
grid = 200                      #Lengde på område

jVals = runSimulation3b(T_pArray, grid, N_x, N_p, beta_k, alpha)    

plt.plot(T_pArray, jVals)
plt.title("Plotting for 3b: ")
plt.xlabel("Ulike tidsteg")
plt.ylabel("Gjennomsnitlig forflytninger")
plt.grid()
plt.show()

"""
#Oppgave 3 c og d
#Konstanter
T_p = 500  #Antall tidssteg per halve periode

#Område
grid = 200 #Lengde på grid
N_x = 100  #Lengde per periode

#Antall partikler
N_p = 12 * N_x

#Definerer alpha som array
alphaArray = np.linspace(0, 1, 50)
beta_k = np.array([0.01, 1, 2, 3, 4, 5, 10, 1000])

# kjør simuleringene
print("Simulating particle stream...")
jAlpha = runSimulation3c(alphaArray, beta_k[7], T_p, N_p, N_x, grid)
print("Simulation completed \n")

# For alle beta k til oppgave d)
print("Simulating particle stream for different beta_k-values...")
jAlpha1 = runSimulation3c(alphaArray, beta_k[0], T_p, N_p, N_x, grid)
jAlpha2 = runSimulation3c(alphaArray, beta_k[1], T_p, N_p, N_x, grid)
jAlpha3 = runSimulation3c(alphaArray, beta_k[2], T_p, N_p, N_x, grid)
jAlpha4 = runSimulation3c(alphaArray, beta_k[3], T_p, N_p, N_x, grid)
jAlpha5 = runSimulation3c(alphaArray, beta_k[4], T_p, N_p, N_x, grid)
jAlpha6 = runSimulation3c(alphaArray, beta_k[5], T_p, N_p, N_x, grid)
jAlpha7 = runSimulation3c(alphaArray, beta_k[6], T_p, N_p, N_x, grid)
print("Simulation completed \n")

# analytisk løsning
jAnal = analyticalSolution(alphaArray)

plt.figure(figsize=(10, 6))

# Plot simulert data
plt.plot(alphaArray, jAlpha, 'o', label='Simulert (Vektorisert)', markersize=4)

# Plot for ulike beta_k
plt.plot(alphaArray, jAlpha1, label="$\\beta_k = 0.01$")
plt.plot(alphaArray, jAlpha2, label="$\\beta_k = 1$")
plt.plot(alphaArray, jAlpha3, label="$\\beta_k = 2$")
plt.plot(alphaArray, jAlpha4, label="$\\beta_k = 3$")
plt.plot(alphaArray, jAlpha5, label="$\\beta_k = 4$")
plt.plot(alphaArray, jAlpha6, label="$\\beta_k = 5$")
plt.plot(alphaArray, jAlpha7, label="$\\beta_k = 10$")

# Plot analytisk data
plt.plot(alphaArray, jAnal, '-', label='Analytisk løsning', linewidth=2)

plt.axhline(0, color='black', linestyle='--', alpha=0.3) # Null-linje
plt.title(r"Strøm $J_{avg}$ som funksjon av asymmetri $\alpha$", fontsize=14)
plt.xlabel(r"Asymmetriparameter $\alpha$", fontsize=12)
plt.ylabel(r"Gjennomsnittlig strøm $J$", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

"""
#Oppgave 3e
#Konstanter
T_pArray = np.linspace(80, 1500, 20) #20 tidsteg mellom 80 og 1500
N_x = 10                        #Lengde på perioden
alpha = 0.8                     #Satt alpha til samme verdi som i oppgave b
beta_k = 1000                   #Satt beta_k til samme verdi som i oppgave b
N_p = 40 * N_x

#Område
grid = 20 #20 i lengde på området

jVals = runSimulation3b(T_pArray, grid, N_x, N_p, alpha, beta_k)
jAnal = analyticalSolution(alpha, T_pArray, N_x)

plt.plot(T_pArray, jVals, label = "Simulering")
plt.plot(T_pArray, jAnal, label = "Analytisk løsning")
plt.title("Plotting for 3b: ")
plt.xlabel("Ulike tidsteg")
plt.ylabel("Gjennomsnitlig forflytninger")
plt.legend()
plt.grid()
plt.show()
"""