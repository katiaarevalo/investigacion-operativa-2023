from scipy.optimize import linprog

#Problema MAXIMIZACIÓN ----> MAXIMIZAR Z 5x1 + 8x2 + 6x3
# Una empresa produce tres tipos de productos metálicos: A, B y C. 
# 
# Variables del problema:
# x1: Cantidad de productos A. 
# x2: Cantidad de producto B.
# x3: Cantidad de productos C.
# x4: Horas de mano de obra. 
# x5: Cantidad materia prima para A. 
# x6: Cantidad materia prima para B. 
# x7: Cantidad materia prima C. 
# x8: Limite superior en la producción total de productos. 
# x9: Limite superior en la cantidad de horas de trabajo disponibles. 
# 
# RESTRICCIÓN: 
#           2x1+4x2+3x3 ≤ x4 (Restricción de mano de obra)
#           3x1+2x2+5x3 ≤ x5 (Restricción de máquinas)
#           x6 ≤ 5x1 (Materia prima para A)
#           2x7 ≤ 6x2 (Materia prima para B)
#           3x8 ≤ 4x3 (Materia prima para C)
#           x1+x2+x3 ≤ x9 (Límite en la producción total)
#           x4 ≤ x10 (Límite en la cantidad de horas de trabajo)          
#           x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 >= 0 (No negatividad)

# PASO 1. Definir coeficientes de la función objetivo.
coef_fun = [-5, -8, -6, 0, 0, 0, 0, 0, 0, 0]

# PASO 2. Trabajar con restricciones.
m_coef_restric = [
    [2, 4, 3, -1, 0, 0, 0, 0, 0, 0],  # 2x1 + 4x2 + 3x3 ≤ x4 (Restricción de mano de obra)
    [3, 2, 5, 0, -1, 0, 0, 0, 0, 0],  # 3x1 + 2x2 + 5x3 ≤ x5 (Restricción de máquinas)
    [0, 0, 0, 0, -5, 1, 0, 0, 0, 0],  # x6 ≤ 5x1 (Materia prima para A)
    [0, -6, 0, 0, 0, 0, 2, 0, 0, 0],  # 2x7 ≤ 6x2 (Materia prima para B)
    [0, 0, -4, 0, 0, 0, 0, 3, 0, 0],  # 3x8 ≤ 4x3 (Materia prima para C)
    [1, 1, 1, 0, 0, 0, 0, 0, -1, 0],  # x1 + x2 + x3 ≤ x9 (Límite en la producción total)
    [0, 0, 0, 1, 0, 0, 0, 0, 0, -1],  # x4 ≤ x10 (Límite en la cantidad de horas de trabajo)
]

# PASO 3. Resultados de las restricciones.
m_resultado_restric = [0, 0, 0, 0, 0, 0, 0]

# DEFINIR LOS LÍMITES DE CADA VARIABLE.
limites = [(0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None), (0, None)]

# Resolviendo el problema de programación lineal
result = linprog(coef_fun, A_ub=m_coef_restric, b_ub=m_resultado_restric, bounds=limites, method='highs')

# Imprimiendo los resultados
print("Cantidad A: ", round(result.x[0]))
print("Cantidad B: ", round(result.x[1]))
print("Cantidad C: ", round(result.x[2]))
print("Beneficio Máximo: ", -result.fun)  # La función objetivo ahora es positiva