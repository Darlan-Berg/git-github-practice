# Desafio proposto pela branch solucao-b
# Complete a função abaixo usando iteração:

def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print("Fatorial de 5:", fatorial(5))
print("Implementação da branch solucao-b")