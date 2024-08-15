from datetime import datetime, timedelta

# Días de la semana y asignaturas
asignaturas = {
    "Apps Moviles": ["Lunes", "Miércoles"],
    "Ingles": ["Lunes", "Martes", "Miércoles", "Jueves"],
    "Calidad de software": ["Martes", "Jueves"],
    "Estadistica": ["Lunes", "Jueves"],
    "Arquitectura": ["Viernes", "Martes"],
    "Etica": ["Viernes"],
}

# Convertir días a números
dias_semana = {
    "Lunes": 0,
    "Martes": 1,
    "Miércoles": 2,
    "Jueves": 3,
    "Viernes": 4,
}

# Rango de fechas
inicio_clases = datetime(2024, 8, 12)
fin_clases = datetime(2024, 12, 23)

# Obtener feriados en Chile
def obtener_feriados():
    feriados = ["2024-08-15","2024-09-17","2024-09-18","2024-09-19","2024-09-20",
                "2024-09-21","2024-10-12","2024-10-31","2024-11-01","2024-11-15",
                "2024-12-24","2024-12-25"]  
    feriados = [datetime.strptime(fecha, "%Y-%m-%d") for fecha in feriados]
    return feriados

# Generar calendario de clases
def generar_calendario(asignaturas, inicio, fin, feriados):
    calendario = {asignatura: [] for asignatura in asignaturas}

    fecha_actual = inicio
    while fecha_actual <= fin:
        if fecha_actual.weekday() < 5 and fecha_actual not in feriados:  # Excluir fines de semana y feriados
            for asignatura, dias in asignaturas.items():
                if fecha_actual.weekday() in [dias_semana[dia] for dia in dias]:
                    calendario[asignatura].append(fecha_actual)
        fecha_actual += timedelta(days=1)

    return calendario

# Guardar el calendario en un archivo de log
def guardar_calendario_en_txt(calendario):
    with open('calendario_clases.txt', 'w') as file:
        for asignatura, fechas in calendario.items():
            file.write(f"{asignatura}:\n")
            for fecha in fechas:
                file.write(f"  - {fecha.strftime('%Y-%m-%d')}\n")
    print("El calendario ha sido guardado en 'calendario_clases.txt'.")

# Ejecutar funciones
feriados = obtener_feriados()
calendario_clases = generar_calendario(asignaturas, inicio_clases, fin_clases, feriados)

# Guardar calendario en archivo de texto
guardar_calendario_en_txt(calendario_clases)
