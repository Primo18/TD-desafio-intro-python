# Ingreso de datos 
precio_suscripcion = float(input("Ingrese el precio de suscripción P: "))
num_usuarios = int(input("Ingrese el número de usuarios U: "))
gastos_totales = float(input("Ingrese los gastos totales GT: "))
utilidades_anterior = float(input("Ingrese las utilidades del año anterior Uanterior: "))

# Cálculo de utilidades actuales
utilidades_actuales = precio_suscripcion * num_usuarios - gastos_totales

# Calcular la razón entre utilidades actuales y del año anterior
razon_utilidades = utilidades_actuales / utilidades_anterior

# Mostrar resultado
print(f"Las utilidades actuales son: {utilidades_actuales}")
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon_utilidades:.2f}")
