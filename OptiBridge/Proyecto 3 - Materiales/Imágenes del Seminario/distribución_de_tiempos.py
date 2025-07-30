import matplotlib.pyplot as plt

# Datos
actividades = [
    'Actualización Manual del Inventario',
    'Búsqueda y Localización de Productos',
    'Procesamiento de Órdenes de Compra',
    'Verificación y Corrección de Inventario',
    'Gestión de Proveedores'
]
tiempos = [60, 50, 16, 4, 9]  # en horas (2 días = 16 horas)

# Crear la gráfica de barras
plt.figure(figsize=(10, 6))
bars = plt.bar(actividades, tiempos, color='skyblue')

# Añadir etiquetas y título
plt.xlabel('Actividades')
plt.ylabel('Tiempo Total Mensual (Horas)')
plt.title('Distribución del Tiempo en Actividades de Inventario')
plt.xticks(rotation=45, ha='right')

# Añadir etiquetas de valor encima de las barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, height, f'{height}', ha='center', va='bottom')

plt.tight_layout()
plt.show()
