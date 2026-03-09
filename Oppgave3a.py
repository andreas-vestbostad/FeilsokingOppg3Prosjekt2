import numpy as np

def initialPositions3a(gridSize, N_p, alpha = None):
    initialPositions = []
    for position in range(gridSize):
        for _ in range(int(round(N_p/gridSize))):
            initialPositions.append(position)
    return np.array(initialPositions)