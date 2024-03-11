# Ingreso de datos 
radio_km = float(input("Ingrese el radio en Kilómetros: "))
constante_gravitacional = float(input("Ingrese la constante g: "))

# Conversión de unidades
radio_m = radio_km * 1000

# Cálculo de la velocidad de escape
velocidad_escape = (2 * constante_gravitacional * radio_m)**0.5

# Mostrar resultado
print(f"La velocidad de Escape es {velocidad_escape:.1f} [m/s]")
