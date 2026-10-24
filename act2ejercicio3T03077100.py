print("\nEjercicio 3: ¿Cuánto escucho a mi artista favorito?")
print("\nMI ARTISTA FAVORITO\n")

artista = "EHYPEN"
canciones_por_dia = 10
duracion_promedio = 2.5  #minutos por canción

minutos_dia = canciones_por_dia * duracion_promedio
minutos_año = minutos_dia * 365
horas_año = minutos_año / 60
dias_año = horas_año / 24

print(f"Escuchas a {artista} {minutos_dia} minutos al día")
print(f"Al año son {minutos_año} minutos")
print(f"Eso equivale a {horas_año:.1f} horas")
print(f"¡0 sea {dias_año:.1f} días comletos escuchando a {artista}!\n") 