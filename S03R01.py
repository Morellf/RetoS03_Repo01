# S03R01 JM Orellana

notas = [0, 0, 0, 0, 0]
xnota = 0
sumanotas = 0
unota = 0
dnota = 0

while xnota < 5:
    while True:
        try:
            notas[xnota] = int(input(f"Ingrese nota {xnota+1}: "))
            break
        except ValueError:
            print('Debe ingresar un número. Intente nuevamente...')
    
    if xnota == 0:
        dnota = notas[0]
        unota = notas[0]
    else:
        if notas[xnota] < dnota:
            dnota = notas[xnota]

        if notas[xnota] > unota:
            unota = notas[xnota]
    
    sumanotas = sumanotas + notas[xnota]
    xnota = xnota + 1

print(f"El promedio de las notas es: {sumanotas/len(notas)}")
print(f"La nota menor es: {dnota}")
print(f"La nota mayor es: {unota}")

