from scipy.optimize import linprog

# RESTRICCIONES:    R1 = X1 + 2X2 + 2X3 ≤ 30
#                   R2 = 2X1 + X2 + 2X3 ≤ 45
# MAXIMIZAR FUN:    Z = 7X1 + 4X2 + 3X3 

# 1) REFLEJAR LA FUNCIÓN OBJETIVO.
# En este caso la función objetivo es Z = 7X1 + 4X2 + 3X3, debo considerar los coeficientes.
# Si necesito MAXIMIZAR colocaré los coeficientes NEGATIVOS.
# Si necesito MINIMIZAR colocaré los coeficientes POSITIVOS. 

# PASO 1) COEFICIENTES FUNCIÓN OBJETIVO.
Coef = [-7, -4, -3]  # 7X1 + 4X2 + 3X3

# PASO 2) TRABAJAR CON RESTRICCIONES          R1 = X1 + 2X2 + 2X3 ≤ 30
#                                             R2 = 2X1 + X2 + 2X3 ≤ 45

# COEFICIENTES DE RESTRICCIONES
# POSITIVO -> LA RESTRICCIÓN TIENE "MENOR O IGUAL"
# NEGATIVO -> LA RESTRICCIÓN TIENE "MAYOR O IGUAL"

M_Rest = [[1, 2, 2], [2, 1, 2]]

# RESULTADOS DE LAS RESTRICCIONES, MISMA REGLA ANTERIOR.
M_Coef = [30, 45]

# DEFINO LOS LIMITES DE CADA VARIABLE. 
limites = [(0, None), (0, None), (0, None)]

# Resolviendo el problema de programación lineal
result = linprog(Coef, A_ub=M_Rest, b_ub=M_Coef, bounds=limites, method='highs')

# Imprimiendo los resultados
print("Cantidad cerveza rubia: ", round(result.x[0]))
print("Cantidad cerveza negra: ", round(result.x[1]))
print("Cantidad cerveza de baja graduación: ", round(result.x[2]))
print("Ganancia maxima:", -result.fun)  # La función objetivo ahora es positiva

