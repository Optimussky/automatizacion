# Ejercicio 1007 Tomar los valores menores a 100 de una lista, y luego sumar a cada uno 10 unidades

print("""
      Tomar los valores menores a 100 de una lista, y luego sumar a cada uno 10 unidades
      """)
numeros = [150, 250, 103, 50, 10, 330, 25, 67]

menores_100 = sorted(numeros)
print(f"Lista original {numeros}")
print(f"Lista ordenada {menores_100}")
menores_100 = filter(lambda n: n < 100, numeros)
#print(f"Numeros menores a 100 {list(sorted(menores_100))}")
menores_100 = sorted(menores_100)
resultado = list(map(lambda n: n + 10, menores_100))

#resultado = list(map(lambda n: n + 10, menores_100))
print(f"Números < a 100 {resultado}")
