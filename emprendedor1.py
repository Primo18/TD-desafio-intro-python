# Ingreso de datos 
precio_suscripcion = float(input("Ingrese el precio de suscripción P: "))
num_usuarios = int(input("Ingrese el número de usuarios U: "))
gastos_totales = float(input("Ingrese los gastos totales GT: "))

# Cálculo de utilidades
utilidades = precio_suscripcion * num_usuarios - gastos_totales

# Mostrar resultado
print(f"Las utilidades del proyecto son: {utilidades}")
