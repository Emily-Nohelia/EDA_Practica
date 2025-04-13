import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

df_pen_sales["Purchase Date"] = pd.to_datetime(df_pen_sales ["Purchase Date"])

# Crear una columna con el mes y año para agrupar las ventas
df_pen_sales ["Year-Month"] = df_pen_sales ["Purchase Date"].dt.to_period("M")

# Contar el número de ventas por mes
monthly_sales = df_pen_sales .groupby("Year-Month").size()

# Graficar las tendencias de ventas a lo largo del tiempo
plt.figure(figsize=(10, 6))
monthly_sales.plot(marker='o', linestyle='-', color='b')
plt.title("Tendencias de ventas a lo largo del tiempo (por mes)", fontsize=14)
plt.xlabel("Fecha (Año-Mes)", fontsize=12)
plt.ylabel("Número de Ventas", fontsize=12)
plt.grid(alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
