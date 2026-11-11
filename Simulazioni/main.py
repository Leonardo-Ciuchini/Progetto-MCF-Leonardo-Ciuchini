import matplotlib.pyplot as plt
import numpy as np

# Funzione per generare un cammino casuale
from es_2 import random_walk

# Parametri del cammino casuale
n = 1000
s = 1.0
walkers = 5

# Grafico del cammino casuale
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
i = 1
while i <= walkers:
    passi, x, y = random_walk(n, s)
    passi_array = np.arange(passi + 1)
    r2 = x**2 + y**2
    ax1.plot(x, y, label=f'Cammino casuale {i}')
    ax2.plot(passi_array, r2, label=f'Cammino casuale {i}')
    i += 1
ax1.legend()
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Cammini casuali')
ax2.set_xlabel('Passi')
ax2.set_ylabel('R^2')
ax2.set_title('Distanza dal centro')
plt.show()
