import pandas as pd
import matplotlib.pyplot as plt
import string

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")

#Análisis de sentimiento de las reseñas
#TAREA 5: Extraer el sentimiento de las opiniones de los clientes.
#Pasos: Divida la columna Revisar para separar el nombre del revisor y el comentario.
#       Realizar un análisis básico de sentimientos (contar las apariciones de palabras positivas como amor, genial, bueno frente a palabras negativas como malo, disgusto).
#       Genere una nube de palabras o un gráfico circular de sentimienAtos.
#       Visualización: 🥧 Gráfico de pastel o circular (críticas positivas vs. negativas)

df_pen_sales["Review"] = df_pen_sales["Review"].fillna("")
positive_words = ["love", "great", "good", "amazing", "excellent", "best"]
negative_words = ["bad", "poor", "dislike", "terrible", "worst", "disappointed", "unfortunately"]

def preprocess_text(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    return text.split()

pos, neg = 0, 0
for review in df_pen_sales["Review"]:
    words = preprocess_text(review)
    pos += sum(w in positive_words for w in words)
    neg += sum(w in negative_words for w in words)

plt.figure(figsize=(6, 6))
plt.pie([pos, neg], labels=["Positive", "Negative"], colors=['skyblue','red'],
        explode=(0,0), autopct="%1.1f%%", startangle=140)
plt.title("Análisis de sentimiento de las reseñas")
plt.show()
