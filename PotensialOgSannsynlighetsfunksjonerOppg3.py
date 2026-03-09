import numpy as np

#Må se gjennom denne på nytt slik at jeg forstår den
def potensialOppg3(x, alpha, N_x, potensialType):
    if potensialType:
        return np.zeros_like(np.atleast_1d(x), dtype=float)
    
    # Tving x til å være en numpy array med en gang
    x = np.atleast_1d(x)
    x_mod = x % N_x
    
    # Lag en tom array med floats
    pot = np.zeros(x.shape, dtype=float)
    
    # Den slake bakken (oppover fra 0 til alpha*N_x)
    # Vi bruker / (alpha * N_x) for å normalisere til høyde 1.0
    mask_slak = (x_mod >= 0) & (x_mod <= alpha * N_x)
    pot[mask_slak] = x_mod[mask_slak] / (alpha * N_x)
    
    # Den bratte bakken (nedover fra alpha*N_x til N_x)
    mask_bratt = (x_mod > alpha * N_x) & (x_mod < N_x)
    pot[mask_bratt] = (N_x - x_mod[mask_bratt]) / ((1 - alpha) * N_x)
    
    return pot

#Skriver en ny probability funksjon som er lettere å normalisere: 
def probabilitiesOppg3(grid, beta_k, alpha, N_x, potensialType = True):
    #Beregner potensialet på nåverende posisjon samt potensialet til høyre og venstre 
    #som vi kaller pluss og minus likt som i oppgaveteksten
    currentPotensial = potensialOppg3(grid, alpha, N_x, potensialType)
    #Bruker np.roll for å efektivisere koden
    plussPotensial = np.roll(currentPotensial, -1)
    minusPotensial = np.roll(currentPotensial, 1)   

    #Beregner telleren eller vektene for P(x), P(x)+ og P(x)-
    #clipper exponentene for å unngå oveflow, 27.02. gjøres utregningen hver simulering.
    weightPluss = np.exp(np.clip(-beta_k * (plussPotensial - currentPotensial), -700, 700))
    weightMinus = np.exp(np.clip(-beta_k * (minusPotensial - currentPotensial), -700, 700))
    weigthCurrentPosition = np.ones_like(grid) # e^0 = 1

    #Beregner totalen altspå neveneren
    totalWeight = weightMinus + weightPluss + weigthCurrentPosition

    #Returnerer selve P(x), P(x)+ og P(x)- i ett np.array()
    return np.array([weightPluss/totalWeight, weigthCurrentPosition/totalWeight, weightMinus/totalWeight])