import matplotlib.pyplot as plt
import numpy as np

def random_walk(n, s):
    passi = 0
    x = [0.0]
    y = [0.0]
    while passi < n:
        phi = np.random.uniform(0, 2 * np.pi)

        delta_x = s * np.cos(phi)
        delta_y = s * np.sin(phi)

        x.append(x[-1] + delta_x)
        y.append(y[-1] + delta_y)

        passi += 1

    return passi, np.array(x), np.array(y)



