print("\n<3<3<3<3<3<3<3<3<3<3<3<3<3<3")
print("Ejericio realizado por Vanessa\n")
print("Ejercicio 4: ¿Cuánto tardo en terminar una serie?")

serie = "Weak Hero"
temporadas = 2
episodios_por_temporada = 8
minutos_por_episodio = 40
horas_al_dia = 3

total_episodios = temporadas * episodios_por_temporada

total_minutos = total_episodios * minutos_por_episodio
total_horas = total_minutos / 60 

dias_necesarios = total_horas / horas_al_dia

print("\nResultados")
print(f"{serie} tiene {total_episodios} episodios")
print(f"Son {total_minutos} minutos en total")
print(f"Equivale a {total_horas:.1f} horas")
print(f"Viendo {horas_al_dia} horas diarias, la terminas en {dias_necesarios:.1f} días")
print("\n<3<3<3<3<3<3<3<3<3<3<3<3<3<3")