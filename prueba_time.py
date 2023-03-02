import time

# Obtiene la fecha y hora actual
fecha_hora_actual = time.localtime()

# Formatea la fecha y hora actual en un string legible
fecha_hora_actual_str = time.strftime("%Y-%m-%d %H:%M:%S", fecha_hora_actual)

# Imprime la fecha y hora actual
print("La fecha y hora actual es:", fecha_hora_actual_str)