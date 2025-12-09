'''1. Gráfico de Barras Horizontales - Turismo

Título: Distribución de turistas por provincia en Costa Rica, año 2024.
Tipo de serie: Serie geográfica.

Descripción:
El gráfico de barras horizontales se utiliza para representar series cualitativas o geográficas, 
donde las categorías son lugares o regiones. Este formato facilita la lectura de etiquetas largas
y permite comparar de manera visual las diferencias entre provincias.'''

import matplotlib.pyplot as plt
import seaborn as sns

provincias = ["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"]
turistas = [8500, 7200, 4600, 5100, 9800, 7700, 6400]

sns.set_palette(["#0c232f", "#304b72", "#55939f", "#559f88", "#d1d1ad"])
plt.barh(provincias, turistas)
plt.title("Distribución de turistas por provincia en Costa Rica, 2024")
plt.xlabel("Cantidad de turistas")
plt.ylabel("Provincia")
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos originales
provincias = ["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"]
turistas = [8500, 7200, 4600, 5100, 9800, 7700, 6400]

# Crear DataFrame y ordenar de mayor a menor
df = pd.DataFrame({'Provincia': provincias, 'Turistas': turistas})
df_ordenado = df.sort_values(by='Turistas', ascending=False)

# Estilo y gráfico
sns.set_palette(["#0c232f", "#304b72", "#55939f", "#559f88", "#d1d1ad"])
plt.barh(df_ordenado['Provincia'], df_ordenado['Turistas'])
plt.gca().invert_yaxis()  # Para que la provincia con más turistas quede arriba
plt.title("Distribución de turistas por provincia en Costa Rica, 2024")
plt.xlabel("Cantidad de turistas")
plt.ylabel("Provincia")
plt.show()

'''2. Gráfico de Barras Verticales - Comercio

Título: Ventas por tipo de producto en Costa Rica, año 2024.
Tipo de serie: Serie cuantitativa discreta.

Descripción:
Este tipo de gráfico representa valores numéricos asociados a categorías discretas.
 Es útil para observar y comparar las ventas por tipo de producto dentro de un período determinado.'''

productos = ["Electrónicos", "Ropa", "Alimentos", "Hogar", "Juguetes"]
ventas = [450, 320, 610, 270, 180]

sns.set_palette(["#304b72", "#55939f", "#559f88", "#d1d1ad", "#0c232f"])
plt.bar(productos, ventas)
plt.title("Ventas por tipo de producto en Costa Rica, 2024")
plt.ylabel("Ventas (en miles ₡)")
plt.xlabel("Producto")
plt.show()

'''3. Gráfico de Barras Simples - Educación

Título: Promedio de calificaciones por grupo en la asignatura de Matemática, Colegio UCR, 2024.
Tipo de serie: Serie cuantitativa discreta.

Descripción:
Las barras simples muestran una sola variable comparada entre diferentes categorías. 
En este caso, se utiliza para representar el promedio de calificaciones por grupo.'''

grupos = ["A", "B", "C", "D"]
promedios = [85, 78, 92, 80]

sns.barplot(x=grupos, y=promedios, palette=["#55939f", "#559f88", "#304b72", "#d1d1ad"])
plt.title("Promedio de calificaciones por grupo, Colegio UCR, 2024")
plt.ylabel("Promedio")
plt.xlabel("Grupo")
plt.show()

'''4. Gráfico de Barras Apiladas - Marketing 

Título: Distribución de clientes regulares y VIP por sucursal en Costa Rica, 2024. 
 Tipo de serie: Serie geográfica. 

Descripción: 
 El gráfico de barras apiladas permite representar la composición interna de cada categoría,
mostrando la proporción de subgrupos dentro del total. '''

import numpy as np

sucursales = ["San José", "Alajuela", "Cartago"]
regulares = np.array([120, 90, 70])
vip = np.array([30, 25, 15])

plt.bar(sucursales, regulares, color="#304b72", label="Regulares")
plt.bar(sucursales, vip, bottom=regulares, color="#55939f", label="VIP")
plt.title("Clientes regulares y VIP por sucursal, Costa Rica, 2024")
plt.xlabel("Sucursal")
plt.ylabel("Cantidad de clientes")
plt.legend()
plt.show()

'''5. Gráfico de Barras Agrupadas - Género Laboral

Título: Ventas por sexo en la empresa XYZ, año 2024.
Tipo de serie: Serie cuantitativa.

Descripción:
Este gráfico compara dos o más variables dentro de las mismas categorías.
Es ideal para visualizar diferencias entre grupos (por ejemplo, hombres y mujeres).'''

departamentos = ["Norte", "Sur", "Este", "Oeste"]
hombres = [230, 180, 210, 190]
mujeres = [200, 150, 250, 170]
x = np.arange(len(departamentos))
ancho = 0.35

plt.bar(x - ancho/2, hombres, width=ancho, color="#304b72", label="Hombres")
plt.bar(x + ancho/2, mujeres, width=ancho, color="#559f88", label="Mujeres")
plt.xticks(x, departamentos)
plt.title("Ventas por sexo en la empresa XYZ, 2024")
plt.xlabel("Departamento")
plt.ylabel("Ventas (miles ₡)")
plt.legend()
plt.show()

'''6. Gráfico de Pirámide - Demografía

Título: Población por edad y género en Costa Rica, año 2024.
Tipo de serie: Serie geográfica.

Descripción:
La pirámide poblacional compara dos grupos opuestos (por ejemplo, hombres y mujeres) distribuidos por rangos de edad.'''

edades = ["0-14", "15-29", "30-44", "45-59", "60+"]
hombres = [1200, 1500, 1300, 900, 600]
mujeres = [-x for x in [1100, 1400, 1350, 950, 700]]

plt.barh(edades, hombres, color="#304b72", label="Hombres")
plt.barh(edades, mujeres, color="#55939f", label="Mujeres")
plt.title("Población por edad y género en Costa Rica, 2024")
plt.xlabel("Población")
plt.legend()
plt.show()

'''7. Gráfico de Pastel - Economía 

Título: Participación de mercado por empresa en Costa Rica, año 2024. 
 Tipo de serie: Serie cualitativa. 

Descripción: 
 El gráfico circular muestra proporciones de un total, expresadas como porcentajes. 
 Es útil para representar distribución de mercado o estructura de costos. '''

empresas = ["Empresa A", "Empresa B", "Empresa C", "Empresa D"]
participacion = [35, 25, 20, 20]

plt.pie(participacion, labels=empresas, autopct="%1.1f%%", colors=["#304b72", "#55939f", "#559f88", "#d1d1ad"])
plt.title("Participación de mercado por empresa, Costa Rica, 2024")
plt.show()

'''8. Gráfico de Barras 100% - Opinión Pública

Título: Distribución porcentual de respuestas “Sí” y “No” por cantón, Costa Rica, 2024.
Tipo de serie: Serie geográfica.

Descripción:
Este tipo de gráfico compara la composición relativa (100%) de diferentes grupos. 
No representa valores absolutos, sino proporciones.'''

cantones = ["San José", "Cartago", "Alajuela"]
si = [60, 70, 50]
no = [40, 30, 50]

plt.bar(cantones, si, color="#55939f", label="Sí")
plt.bar(cantones, no, bottom=si, color="#304b72", label="No")
plt.title("Respuestas 'Sí' y 'No' por cantón, Costa Rica, 2024")
plt.ylabel("Porcentaje (%)")
plt.legend()
plt.show()

'''9. Gráfico Lineal - Finanzas 

Título: Ventas mensuales de la empresa XYZ en Costa Rica, año 2024. 
 Tipo de serie: Serie cronológica. 

Descripción: 
 El gráfico lineal muestra la evolución de una variable en el tiempo,
permitiendo observar tendencias o fluctuaciones. '''

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
ventas = [80, 95, 100, 90, 110, 120, 115, 130, 125, 140, 135, 150]

plt.plot(meses, ventas, marker="o", color="#304b72")
plt.title("Ventas mensuales de la empresa XYZ, Costa Rica, 2024")
plt.xlabel("Mes")
plt.ylabel("Ventas (miles ₡)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

'''10. Gráfico de Araña - Recursos Humanos

Título: Evaluación de competencias laborales en la empresa XYZ, Costa Rica, 2024.
Tipo de serie: Serie cuantitativa multivariable.

Descripción:
El gráfico de araña o radar permite comparar múltiples variables simultáneamente en un formato radial.
 Es útil para visualizar perfiles o desempeños.'''

import numpy as np

competencias = ["Comunicación", "Trabajo en equipo", "Liderazgo", "Innovación", "Responsabilidad"]
valores = [8, 9, 7, 6, 9]
valores += valores[:1]
angulos = np.linspace(0, 2 * np.pi, len(valores))

fig, ax = plt.subplots(subplot_kw={'polar': True})
ax.plot(angulos, valores, color="#55939f", linewidth=2)
ax.fill(angulos, valores, color="#55939f", alpha=0.3)
ax.set_xticks(angulos[:-1])
ax.set_xticklabels(competencias)
plt.title("Evaluación de competencias laborales, Empresa XYZ, 2024")
plt.show()
