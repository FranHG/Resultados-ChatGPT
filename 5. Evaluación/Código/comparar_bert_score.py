import os
import pandas as pd
from bert_score import score
from bert_score import BERTScorer
import matplotlib.pyplot as plt
import argparse
from datetime import datetime

# -------------------- PARSE ARGUMENTOS --------------------
parser = argparse.ArgumentParser(description="Evaluador de requisitos y referencias con BERTScore")

parser.add_argument('--reqfile', type=str, required=True, help='Archivo Excel de requisitos')
parser.add_argument('--reffile', type=str, required=True, help='Archivo Excel de referencias')
parser.add_argument('--lang', type=str, default='es', help='Idioma para BERTScore (por defecto: es)')
parser.add_argument('--rescale', action='store_true', help='Aplicar baseline rescaling (opcional)')

args = parser.parse_args()

# -------------------- CONFIGURACIÓN --------------------
# Nombre de archivos de entrada
archivo_requisitos = args.reqfile
archivo_referencias = args.reffile

# Usar baseline reescalado
usar_rescale = args.rescale

# Idioma para BERTScore
idioma = args.lang

# Carpeta de salida
nombre_experimento = "resultados_" + datetime.now().strftime("%Y%m%d_%H%M%S")
os.makedirs(nombre_experimento, exist_ok=True)

# -------------------- CARGA DE DATOS --------------------
print("\n Cargando requisitos y referencias...")
df_req = pd.read_excel(archivo_requisitos)
df_ref = pd.read_excel(archivo_referencias)

# -------------------- EVALUACIÓN --------------------
scorer = BERTScorer(
    lang=idioma,
    rescale_with_baseline=usar_rescale
)

ids = []
titulos = []
P_list = []
R_list = []
F1_list = []

print("\n Evaluando con BERTScore...")
for _, req_row in df_req.iterrows():
    id_req = req_row["ID"]
    titulo = req_row["Título"]
    texto_req = req_row["Texto"]

    #refs = df_ref[df_ref["ID"] == id_req]["Texto"].tolist()
    refs = df_ref[df_ref["ID"] == id_req]["Texto"].dropna().astype(str).tolist()

    if not refs:
        print(f" Requisito {id_req} no tiene referencias. Saltando...")
        continue

    # Ejecutar evaluación
    P, R, F1 = score([texto_req], [refs], lang=idioma, rescale_with_baseline=usar_rescale)

    ids.append(id_req)
    titulos.append(titulo)
    P_list.append(P[0].item())
    R_list.append(R[0].item())
    F1_list.append(F1[0].item())

    # Plot individual
    best_idx = F1.argmax().item()
    best_ref = refs[best_idx]

    #try:
    #    scorer.plot_example(texto_req, best_ref)
    #except Exception as e:
    #    print(f"No se pudo generar la matriz para {id_req}: {e}")

# -------------------- EXPORTAR RESULTADOS --------------------
df_resultados = pd.DataFrame({
    "ID": ids,
    "Título": titulos,
    "P": P_list,
    "R": R_list,
    "F1": F1_list
})

excel_path = os.path.join(nombre_experimento, "resultados_bertscore.xlsx")
df_resultados.to_excel(excel_path, index=False)
print(f"\n Resultados guardados en: {excel_path}")

# -------------------- GRÁFICAS GLOBALES --------------------
plt.figure()
plt.hist(F1_list, bins=20)
plt.xlabel("F1 Score")
plt.ylabel("Cantidad")
plt.title("Distribución de F1 Score")
plt.savefig(os.path.join(nombre_experimento, "histograma_f1.png"))

plt.figure(figsize=(10, 5))
plt.plot(F1_list, marker='o', label='F1 Score')
plt.plot(P_list, linestyle='--', label='Precisión')
plt.plot(R_list, linestyle='-.', label='Recall')
plt.title("BERTScore por requisito")
plt.xlabel("Índice del requisito")
plt.ylabel("Puntaje")
plt.ylim(0, 1)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(nombre_experimento, "lineas_metricas.png"))

print("\n Evaluación completada con éxito.")