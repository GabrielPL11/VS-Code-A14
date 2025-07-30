import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# ----------------------------------
# 1. Preparación de los Datos
# ----------------------------------

# Datos de PIB
pib_data = {
    'Trimestre': ['Q1 2024', 'Q2 2024'],
    'PIB (B MX)': [6.58, 6.58 * 1.0506],  # Incremento del 5.06%
    'Crecimiento vs Trimestre Anterior (%)': [None, 5.06],
    'Crecimiento vs Año Anterior (%)': [None, 2.27]
}

pib_df = pd.DataFrame(pib_data)

# Datos del Censo Económico 2019
censo_2019_data = {
    'Estado': ['Estado de México', 'Nuevo León', 'Jalisco', 'Querétaro', 'Otros'],
    'Unidades Económicas': [37, 33, 29, 25, 137],
    'Producción Bruta (M MX)': [0, 2962, 0, 2564, 2590],
    'Ingresos Totales (M MX)': [0, 3223, 0, 2748, 5255]
}

censo_2019_df = pd.DataFrame(censo_2019_data)

# ----------------------------------
# 2. Creación de los Gráficos
# ----------------------------------

# Configuración general de la figura
fig, axs = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Resumen Económico de la Industria Manufacturera en México (2014-2024)', fontsize=20, weight='bold', y=0.95)

# 1. Gráfico de PIB
ax_pib = axs[0, 0]
bars = ax_pib.bar(pib_df['Trimestre'], pib_df['PIB (B MX)'], color=['#1f77b4', '#ff7f0e'])

# Añadir etiquetas de crecimiento
for idx, row in pib_df.iterrows():
    if row['Trimestre'] == 'Q2 2024':
        ax_pib.text(idx, row['PIB (B MX)'] + 0.1, f"+{row['Crecimiento vs Trimestre Anterior (%)']}% QoQ\n+{row['Crecimiento vs Año Anterior (%)']}% YoY",
                   ha='center', va='bottom', fontsize=10, fontweight='bold', color='green')

ax_pib.set_title('Producto Interno Bruto (PIB)', fontsize=14, weight='bold')
ax_pib.set_ylabel('PIB (B MX)', fontsize=12)
ax_pib.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.2f}'))
ax_pib.grid(axis='y', linestyle='--', alpha=0.7)

# 2. Gráfico de Unidades Económicas por Estado
ax_unidades = axs[0, 1]
bars_unidades = ax_unidades.bar(censo_2019_df['Estado'], censo_2019_df['Unidades Económicas'], color='#2ca02c')

# Añadir etiquetas de valor
for bar in bars_unidades:
    height = bar.get_height()
    ax_unidades.annotate(f'{height}',
                         xy=(bar.get_x() + bar.get_width() / 2, height),
                         xytext=(0, 3),  # 3 puntos de desplazamiento
                         textcoords="offset points",
                         ha='center', va='bottom', fontsize=10, color='black')

ax_unidades.set_title('Unidades Económicas por Estado (Censo 2019)', fontsize=14, weight='bold')
ax_unidades.set_ylabel('Número de Unidades', fontsize=12)
ax_unidades.grid(axis='y', linestyle='--', alpha=0.7)

# 3. Gráfico de Producción Bruta por Estado
ax_produccion = axs[1, 0]
bars_produccion = ax_produccion.bar(censo_2019_df['Estado'], censo_2019_df['Producción Bruta (M MX)'], color='#d62728')

# Añadir etiquetas de valor
for bar in bars_produccion:
    height = bar.get_height()
    if height > 0:
        ax_produccion.annotate(f'{height}',
                               xy=(bar.get_x() + bar.get_width() / 2, height),
                               xytext=(0, 3),  # 3 puntos de desplazamiento
                               textcoords="offset points",
                               ha='center', va='bottom', fontsize=10, color='black')

ax_produccion.set_title('Producción Bruta por Estado (Censo 2019)', fontsize=14, weight='bold')
ax_produccion.set_ylabel('Producción Bruta (M MX)', fontsize=12)
ax_produccion.grid(axis='y', linestyle='--', alpha=0.7)

# 4. Gráfico de Ingresos Totales por Estado
ax_ingresos = axs[1, 1]
bars_ingresos = ax_ingresos.bar(censo_2019_df['Estado'], censo_2019_df['Ingresos Totales (M MX)'], color='#17becf')

# Añadir etiquetas de valor
for bar in bars_ingresos:
    height = bar.get_height()
    if height > 0:
        ax_ingresos.annotate(f'{height}',
                             xy=(bar.get_x() + bar.get_width() / 2, height),
                             xytext=(0, 3),  # 3 puntos de desplazamiento
                             textcoords="offset points",
                             ha='center', va='bottom', fontsize=10, color='black')

ax_ingresos.set_title('Ingresos Totales por Estado (Censo 2019)', fontsize=14, weight='bold')
ax_ingresos.set_ylabel('Ingresos Totales (M MX)', fontsize=12)
ax_ingresos.grid(axis='y', linestyle='--', alpha=0.7)

# Ajuste de diseño para evitar superposiciones
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Mostrar la figura
plt.show()
