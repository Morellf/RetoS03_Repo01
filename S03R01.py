# S03R01 JM Orellana

notas = [0, 0, 0, 0, 0]
xnota = 0
sumanotas = 0
unota = 0
dnota = 0

while xnota < 5:
    print(f"Ingrese nota {xnota+1}: ", end="")
    notas[xnota] = int(input())
    xnota = xnota + 1

dnota = notas[0]
unota = notas[0]

for x in range(0, len(notas)):
    if notas[x] < dnota:
        dnota = notas[x]

    if notas[x] > unota:
        unota = notas[x]
    
    sumanotas = sumanotas + notas[x]

print(f"El promedio de las notas es: {sumanotas/len(notas)}")
print(f"La nota menor es: {dnota}")
print(f"La nota mayor es: {unota}")

