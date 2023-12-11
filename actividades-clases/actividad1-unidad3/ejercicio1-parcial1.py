from scipy.optimize import linprog

#RESTRICCIONES:         36 x1 + 30 x2 + 60 x3 <=4800
#                       20 x1 + 18 x2 + 25 x3 <= 2400
#                       3 x1 + 2 x2 + 5 x3 <= 375
# FUNCIÓN OBJETIVO:     Max Z --> 100 x1 + 80 x2 + 150 x3

# PASO 1) COEFICIENTES FUNCIÓN OBJETIVO.
#           MAX -> NEGATIVOS
#           MIN -> POSITIVOS

Coef = [-100, -80, -150]  # 7X1 + 4X2 + 3X3

# COEFICIENTES DE RESTRICCIONES
# POSITIVO -> LA RESTRICCIÓN TIENE "MENOR O IGUAL"
# NEGATIVO -> LA RESTRICCIÓN TIENE "MAYOR O IGUAL"

M_Rest = [[36, 30, 60], [20, 18, 25], [3, 2, 5]]

# RESULTADOS DE LAS RESTRICCIONES, MISMA REGLA ANTERIOR.
M_Coef = [4800, 2400, 375]

# DEFINO LOS LIMITES DE CADA VARIABLE. 
limites = [(0, None), (0, None), (0, None)]

# Resolviendo el problema de programación lineal
result = linprog(Coef, A_ub=M_Rest, b_ub=M_Coef, bounds=limites, method='highs')

# Imprimiendo los resultados
print("Cantidad camisas: ", round(result.x[0]))
print("Cantidad shorts: ", round(result.x[1]))
print("Cantidad pantalones: ", round(result.x[2]))
print("Ganancia maxima:", -result.fun)  # La función objetivo ahora es positiva
