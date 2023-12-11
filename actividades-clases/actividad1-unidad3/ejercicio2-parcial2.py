from scipy.optimize import linprog

# RESTRICCIONES:    R1 = x1 + x2 <= 50.000 
#                   R2 = 8X1 + 4X2 <= 300.000
#                   R3 = X2 <= 30.000 

# MNIMIZAR FUN:    MAX Z  10X1 + 6X2 

# PASO 1) COEFICIENTES FUNCIÓN OBJETIVO.
Coef = [-10, -6] 

# PASO 2) TRABAJAR CON RESTRICCIONES          

# COEFICIENTES DE RESTRICCIONES
# POSITIVO -> LA RESTRICCIÓN TIENE "MENOR O IGUAL"
# NEGATIVO -> LA RESTRICCIÓN TIENE "MAYOR O IGUAL"

M_Rest = [[1, 1], [8, 4], [0, 1]]

# RESULTADOS DE LAS RESTRICCIONES, MISMA REGLA ANTERIOR.
M_Coef = [50000, 300000, 30000]

# DEFINO LOS LIMITES DE CADA VARIABLE. 
limites = [(0, None), (0, None)]

# Resolviendo el problema de programación lineal
result = linprog(Coef, A_ub=M_Rest, b_ub=M_Coef, bounds=limites, method='highs')

# Imprimiendo los resultados
print("Cantidad asig. ing: ", round(result.x[0]))
print("Cantidad asig. no ing: ", round(result.x[1]))
print("Minimas horas:", -result.fun)  # La función objetivo ahora es positiva