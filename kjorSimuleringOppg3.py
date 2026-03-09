import numpy as np
from PotensialOgSannsynlighetsfunksjonerOppg3 import *

#Vi brukte vektorisering av numpy objekter for å kjøre koden raskere. 
def runSimulationVectorized(grid, initialPositions, beta_k, alpha, N_x, N_p, T_p, totalSteps):
    #initialiserer startposisjonene i ett numpy array
    positions = initialPositions(grid, N_p)
    
    jVals = []
    
    # 2. Forhåndsberegn sannsynligheter for HELE gridet (0 til grid_size-1)
    gridIndex = np.arange(grid)     #Grid index for at grid ikke skal være ett tall = 200, men en array fra 0 til 200
    #Definerer de ulike sannsynlighetene nå slik at vi kun beregner dem en gang
    probabilitiesFlatPotensial = probabilitiesOppg3(gridIndex, beta_k, alpha, N_x, True)
    probabilitiesVaryingPotensial = probabilitiesOppg3(gridIndex, beta_k, alpha, N_x, False)

    for timeStep in range(totalSteps):
        # Bestem hvilken fase vi er i
        potType = (timeStep // T_p) % 2 == 0
        current_probs = probabilitiesFlatPotensial if potType else probabilitiesVaryingPotensial
        
        # Vi henter ut sannsynlighetene for de indeksene der partiklene faktisk står
        pPlus_all = current_probs[0, positions]
        pStay_all = current_probs[1, positions] #Feilen ligger her pStay blir en array av 1
        #Men current_probs er ikke en array konstant lik 1. 
        
        # Trekk tilfeldige tall for alle partikler samtidig
        outcomes = np.random.rand(N_p)
        
        # 5. Bestem bevegelser (vektorisert)
        steps = np.zeros(N_p, dtype=int)
        steps[outcomes < pPlus_all] = 1
        steps[(outcomes >= pPlus_all) & (outcomes < pPlus_all + pStay_all)] = 0
        steps[outcomes >= pPlus_all + pStay_all] = -1
        
        # 6. Beregn strømmen J(t) for dette tidsskrittet
        nPlus = np.sum(steps == 1)
        nMinus = np.sum(steps == -1)
        jVals.append((nPlus - nMinus) / N_p)
        
        if timeStep == 700:
            #print("Brake point") #Bra punkt å stoppe i debuggeren
            pass

        # 7. OPPDATER POSISJONER (i NumPy-arrayen)
        positions = (positions + steps) % grid
        
    return jVals