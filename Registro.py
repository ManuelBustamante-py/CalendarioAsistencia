import os
import json
from datetime import datetime
from Asistencia import calendario_clases

# Archivo JSON donde se guardará la asistencia
archivo_json = 'registro_asistencia.json'

# Cargar asistencias desde el archivo JSON
def cargar_asistencias(archivo_json):
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r') as file:
            return json.load(file)
    return {}

# Guardar asistencias en el archivo JSON
def guardar_asistencias(asistencias, archivo_json):
    with open(archivo_json, 'w') as file:
        json.dump(asistencias, file, indent=4)

# Registrar asistencia diaria
def registrar_asistencia_diaria(calendario, archivo_json):
    # Obtener la fecha actual
    hoy = datetime.now().strftime('%Y-%m-%d')
    
    # Verificar si hay clases hoy
    clases_hoy = {asignatura: fechas for asignatura, fechas in calendario.items() if hoy in [fecha.strftime('%Y-%m-%d') for fecha in fechas]}
    
    if not clases_hoy:
        print("Hoy no tienes clases.")
        return
    
    # Cargar asistencias existentes
    asistencias = cargar_asistencias(archivo_json)
    
    # Registrar asistencia
    for asignatura in clases_hoy.keys():
        asistencia = input(f"¿Asististe a {asignatura} hoy? (si/no): ").strip().lower()
        if asistencia == "si":
            if asignatura not in asistencias:
                asistencias[asignatura] = []
            asistencias[asignatura].append(hoy)
    
    # Guardar asistencia en el archivo JSON
    guardar_asistencias(asistencias, archivo_json)
    print(f"Asistencia registrada para {hoy}.")

# Registrar asistencia diaria
registrar_asistencia_diaria(calendario_clases, archivo_json)
