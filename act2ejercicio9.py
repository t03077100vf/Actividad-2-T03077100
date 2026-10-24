print("\n<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3")
print("Ejercicio 9: Tienda de mascotas interactiva")
print("TIENDA DE MASCOTAS DE Vanessa")

mascota = input("\n¿Qué mascota quieres adoptar?")

precio_mascota = float(input(f"¿Cuánto cuesta el/la {mascota}? $"))
precio_croquetas = float(input("¿Cuánto cuesta un mes de croquetas? $"))
meses = int(input("¿Para cuántos meses quieres croquetas? "))

costo_croquetas = precio_croquetas * meses

total = precio_mascota + costo_croquetas 

print("\n<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3")
print("Ticket de compra")

print(f"Mascota: {mascota} ${precio_mascota:.2f}")
print(f"Croquetas por {meses} meses: ${costo_croquetas:2.f}")
print(f"\nTOTAL A PAGAR: ${total:.2f}\n")
print("\n<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3")

