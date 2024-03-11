# Ingreso de datos 
precio_suscripcion_normal = float(input("Ingrese el precio de suscripción para usuarios normales P: "))
num_usuarios_normal = int(input("Ingrese el número de usuarios normales Unormal: "))
num_usuarios_premium = int(input("Ingrese el número de usuarios premium Upremium: "))
gastos_totales = float(input("Ingrese los gastos totales GT: "))

# Cálculo de utilidades considerando usuarios premium
utilidades = (precio_suscripcion_normal * num_usuarios_normal + 1.5 * precio_suscripcion_normal * num_usuarios_premium) - gastos_totales

# Mostrar resultado
print(f"Las utilidades del proyecto son: {utilidades}")
