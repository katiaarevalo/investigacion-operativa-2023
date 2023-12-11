from scipy.optimize import linprog

# RESTRICCIONES:    R1 = 60x1 + 24x2 ≤ 3000
#                   R2 = x1 + x2 > 65

# MNIMIZAR FUN:    MIN Z = 120 X1 + 200 X2

# PASO 1) COEFICIENTES FUNCIÓN OBJETIVO.
Coef = [120, 200] 

# PASO 2) TRABAJAR CON RESTRICCIONES          

# COEFICIENTES DE RESTRICCIONES
# POSITIVO -> LA RESTRICCIÓN TIENE "MENOR O IGUAL"
# NEGATIVO -> LA RESTRICCIÓN TIENE "MAYOR O IGUAL"

M_Rest = [[60, 24], [-1, -1]]

# RESULTADOS DE LAS RESTRICCIONES, MISMA REGLA ANTERIOR.
M_Coef = [3000, -65]

# DEFINO LOS LIMITES DE CADA VARIABLE. 
limites = [(23, None), (20, None)]

# Resolviendo el problema de programación lineal
result = linprog(Coef, A_ub=M_Rest, b_ub=M_Coef, bounds=limites, method='highs')

# Imprimiendo los resultados
print("Cantidad asig. ing: ", round(result.x[0]))
print("Cantidad asig. no ing: ", round(result.x[1]))
print("Minimas horas:", result.fun)  # La función objetivo ahora es positiva