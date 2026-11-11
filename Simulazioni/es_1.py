import matplotlib.pyplot as plt
import numpy as np

# Valori intervallo
a = 0
b = 10

#Funzione
def f(x):
    return 3/1000 * x**2

# Valori massimo e minimo della funzione nell'intervallo [a, b]
y_max = f(b)
y_min = f(a)

#Hit or Miss
def hit_or_miss(f, a, b, y_max, n):
    hit = []
    while len(hit) < n:
        x = np.random.uniform(a, b)
        y = np.random.uniform(y_min, y_max)
        if y <= f(x):
            hit.append(x)
    return hit

#Metodo Cumulativo
def c(x):
    return 1/1000 * x**3  # Integrale della funzione f(x)

def c_inv(z):
    return (1000 * z) ** (1/3)  # Inversa della funzione cumulativa c(x)


def cumulative_method(n):
    z = np.random.uniform(0, 1, n)
    x = c_inv(z)
    return x


# Generazione dei punti hit or miss
n = 1000  # Numero di punti da generare
hit_points = hit_or_miss(f, a, b, y_max, n)
campioni_cumulativi = cumulative_method(n)

# Grafico dei punti generati con il metodo Hit or Miss
plt.figure(figsize=(10, 6))
plt.scatter(hit_points, [f(x) for x in hit_points], c='red', s=1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Metodo Hit or Miss')
plt.show()

# Grafico dei punti generati con il metodo Cumulativo
plt.figure(figsize=(10, 6))
plt.scatter(campioni_cumulativi, [f(x) for x in campioni_cumulativi], c='blue', s=1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Metodo Cumulativo')
plt.show()
