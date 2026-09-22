# Desafio proposto pela branch solucao-a
# Complete a função abaixo usando recursão:

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

print("Fatorial de 5:", fatorial(5))
print("Implementação da branch solucao-a")