import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch

# Configuración de la figura
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Funciones para dibujar elementos
def draw_circle(ax, center, radius, text):
    circle = Circle(center, radius, edgecolor='black', facecolor='lightblue', linewidth=2)
    ax.add_patch(circle)
    ax.text(center[0], center[1], text, fontsize=10, ha='center', va='center')

def draw_square(ax, bottom_left, size, text):
    square = Rectangle(bottom_left, size, size, edgecolor='black', facecolor='lightgreen', linewidth=2)
    ax.add_patch(square)
    center = (bottom_left[0] + size / 2, bottom_left[1] + size / 2)
    ax.text(center[0], center[1], text, fontsize=10, ha='center', va='center')

def draw_arrow(ax, start, end, text='', color='black'):
    arrow = FancyArrowPatch(start, end, arrowstyle='->', mutation_scale=20, linewidth=1.5, color=color)
    ax.add_patch(arrow)
    if text:
        mid_point = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
        ax.text(mid_point[0], mid_point[1], text, fontsize=9, ha='center', va='center')

# Coordenadas de los elementos
positions = {
    'accion1': (5, 8),
    'inspeccion1': (5, 6),
    'accion2': (5, 4),
    'inspeccion2': (5, 2),
    'efluente1': (2, 6),
    'efluente2': (8, 2)
}

# Dibujar elementos
draw_circle(ax, positions['accion1'], 0.5, 'Acción 1')
draw_square(ax, (positions['inspeccion1'][0]-0.5, positions['inspeccion1'][1]-0.5), 1, 'Inspección 1')
draw_circle(ax, positions['accion2'], 0.5, 'Acción 2')
draw_square(ax, (positions['inspeccion2'][0]-0.5, positions['inspeccion2'][1]-0.5), 1, 'Inspección 2')

# Dibujar flechas entre elementos
draw_arrow(ax, (positions['accion1'][0], positions['accion1'][1]-0.5), (positions['inspeccion1'][0], positions['inspeccion1'][1]+0.5))
draw_arrow(ax, (positions['inspeccion1'][0], positions['inspeccion1'][1]-0.5), (positions['accion2'][0], positions['accion2'][1]+0.5))
draw_arrow(ax, (positions['accion2'][0], positions['accion2'][1]-0.5), (positions['inspeccion2'][0], positions['inspeccion2'][1]+0.5))
draw_arrow(ax, (positions['inspeccion2'][0], positions['inspeccion2'][1]-0.5), (positions['accion1'][0], positions['accion1'][1]+0.5), text='Iteración', color='blue')

# Dibujar efluentes
draw_arrow(ax, (positions['inspeccion1'][0]-0.5, positions['inspeccion1'][1]), (positions['efluente1'][0]+0.3, positions['efluente1'][1]), text='Efluente 1', color='red')
draw_arrow(ax, (positions['inspeccion2'][0]+0.5, positions['inspeccion2'][1]), (positions['efluente2'][0]-0.3, positions['efluente2'][1]), text='Efluente 2', color='red')

# Dibujar efluentes (círculos)
draw_circle(ax, positions['efluente1'], 0.3, 'Efluente 1')
draw_circle(ax, positions['efluente2'], 0.3, 'Efluente 2')

# Guardar y mostrar el diagrama
plt.savefig('diagrama_proceso_iterativo.png', bbox_inches='tight')
plt.show()
