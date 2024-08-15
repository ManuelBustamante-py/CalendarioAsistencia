import os
import json
from calendario import calendario_clases

# Archivo JSON donde se guarda la asistencia
archivo_json = 'registro_asistencia.json'

# Cargar asistencias desde el archivo JSON
def cargar_asistencias(archivo_json):
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r') as file:
            return json.load(file)
    return {}

def calcular_porcentaje_asistencia(calendario, asistencias):
    porcentajes = {}
    
    for asignatura, fechas in calendario.items():
        total_clases = len(fechas)
        asistido = sum(1 for fecha in fechas if fecha.strftime('%Y-%m-%d') in asistencias.get(asignatura, []))
        porcentaje = (asistido / total_clases) * 100
        porcentajes[asignatura] = porcentaje
    
    return porcentajes

# Cargar asistencias desde el archivo JSON
asistencias = cargar_asistencias(archivo_json)

# Calcular el porcentaje de asistencia
porcentajes_asistencia = calcular_porcentaje_asistencia(calendario_clases, asistencias)

# Mostrar resultados
for asignatura, porcentaje in porcentajes_asistencia.items():
    print(f"Asistencia en {asignatura}: {porcentaje:.2f}%")

def calcular_dias_restantes(calendario, asistencias):
    dias_restantes = {}
    
    for asignatura, fechas in calendario.items():
        asistido = len(asistencias.get(asignatura, []))
        dias_restantes[asignatura] = len(fechas) - asistido
    
    return dias_restantes

dias_restantes = calcular_dias_restantes(calendario_clases, asistencias)

print("\nDías restantes de clases para cada asignatura:")
for asignatura, dias in dias_restantes.items():
    print(f"{asignatura}: {dias} día(s) restante(s)")
