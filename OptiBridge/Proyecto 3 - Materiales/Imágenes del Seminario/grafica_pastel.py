import matplotlib.pyplot as plt

# Datos
tipos_error = ['Errores de Transcripción', 'Descuentos Incorrectos', 'Falta de Actualización', 'Otros']
frecuencia = [10, 5, 3, 2]
porcentajes = [50, 25, 15, 10]

# Crear la gráfica de pastel
plt.figure(figsize=(8, 8))
plt.pie(porcentajes, labels=tipos_error, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Distribución de Tipos de Errores en la Gestión Manual de Inventarios')

# Dibujar un círculo en el centro para hacer un donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.show()
