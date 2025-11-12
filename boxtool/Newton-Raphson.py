import numpy as np
from scipy.optimize import root

# Sistema con término xy
def F(x):
    f1 = x[0]**2 + x[0]*x[1] + x[1]**2 - 1
    f2 = x[0]*x[1] - 0.25
    return [f1, f2]

# Valor inicial
x0 = [0.5, 0.5]

# Llamamos a root (usa por defecto el método 'hybr' tipo Newton)
sol = root(F, x0)

print("Solución aproximada:", sol.x)
print("Éxito:", sol.success)
print("Número de iteraciones:", sol.nfev)
