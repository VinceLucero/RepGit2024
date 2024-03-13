print("bienvenido")

total=25

while total>1:
    quitar=int(input("Ingresa los cerillos a quitar:"))
    total=total-quitar
    print("quedan",total,"cerillos")
    if quitar==1:
      print("la computadora quita 2 cerillos")
      total=total-2
      print("quedan",total,"cerillos")
    else:
      print("la computadora quita 1 cerillo")
      total=total-1
      print("quedan",total,"cerillos")
    

print("perdiste")