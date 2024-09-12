import numpy as np
a = np.array([[0.52 , 0.2 , 0.25], 
              [0.30 , 0.5 , 0.2], 
              [0.18	,0.3	,0.55]]) 
b = np.array([4800, 5810, 5690])

try:
    x = np.linalg.solve(a, b)
    print("Metros cúbicos que se deben transportar desde cada cantera:")
    print(f"Cantera 1: {x[0]:.2f} m^3")
    print(f"Cantera 2: {x[1]:.2f} m^3")
    print(f"Cantera 3: {x[2]:.2f} m^3")
except np.linalg.LinAlgError:
    print("La matriz es singular y no se puede invertir. Verifica los datos.")


