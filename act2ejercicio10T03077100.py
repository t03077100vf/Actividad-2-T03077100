print("\n<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3")
print("Ejercicio 10: Reto final, ¿soy viral?")
print("CALCULADORA DE ENGAGEMENT HECHO POR Vanessa")

usuario = input("\nTu usuario de Instagram/TikTok: @")

seguidores = int(input("¿Cuántos seguidores tienes? "))
likes = int(input("¿Cuántos likes tuvo tu último post? "))
comentarios = int(input("¿Cuántos comentarios tuvo? "))


interacciones = likes + comentarios 

engagement = (interacciones / seguidores) + 100

print(f"\n<3<3<3<3<3<3<3<3<3<3<3<3 RESULTADOS DE @{usuario} <3<3<3<3<3<3<3<3<3<3<3<3")
print(f"Interacciones totales: {interacciones}")
print(f"Engagement: {engagement:.2f}%")
print("\nDato: en redes, un engagement arriba de 3% ya se considera bueno")
print("\n<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3")