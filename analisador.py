import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

def selecionar_arquivos():
    arquivos = filedialog.askopenfilenames(title="Selecione os arquivos Excel", filetypes=[("Arquivos Excel", "*.xlsx")])
    if arquivos:
        contador_arquivos.set(f"{len(arquivos)} arquivo(s) importado(s)")
        global arquivos_selecionados
        arquivos_selecionados = arquivos

def selecionar_pasta():
    pasta = filedialog.askdirectory(title="Selecione a pasta contendo os arquivos Excel")
    if pasta:
        arquivos = [os.path.join(pasta, arquivo) for arquivo in os.listdir(pasta) if arquivo.endswith('.xlsx')]
        contador_arquivos.set(f"{len(arquivos)} arquivo(s) importado(s)")
        global arquivos_selecionados
        arquivos_selecionados = arquivos

def selecionar_diretorio():
    diretorio_destino = filedialog.askdirectory(title="Selecione o diretório de destino")
    if diretorio_destino:
        sucesso = exportar_analise(diretorio_destino)
        if sucesso:
            messagebox.showinfo("Exportação Concluída", f"Resultado da análise exportado para '{diretorio_destino}/resultado_analise.xlsx'.")
        else:
            messagebox.showwarning("Exportação Falhou", "Você precisa realizar uma análise antes de exportar os resultados.")

def analisar_arquivos():
    if arquivos_selecionados:
        combinar_dataframes(arquivos_selecionados)
        messagebox.showinfo("Sucesso", "Análise concluída com sucesso!\n\nExporte para seu diretório.")

def exportar_analise(diretorio_destino):
    if 'df_final' in globals():
        try:
            df_final.to_excel(f"{diretorio_destino}/resultado_analise.xlsx", index=False)
            return True
        except Exception as e:
            print(e)  # Mostrar erro no console para debug
            return False
    else:
        return False

def extrair_dados(arquivo):
    df = pd.read_excel(arquivo)
    data = {
        "ID": df.iloc[4, 2],
        "EXT": df.iloc[5, 2],
        "KM_INI": df.iloc[4, 7],
        "KM_FIM": df.iloc[5, 7],
        "TIPO": df.iloc[9, 2],
        "FORMA": df.iloc[9, 7],
        "LAT_MONT": df.iloc[7, 2],
        "LONG_MONT": df.iloc[8, 2],
        "DIM_MONT": df.iloc[11, 2],
        "LAD_MON": df.iloc[12, 2],
        "EST_MONT": df.iloc[13, 2],
        "MAT_MONT": df.iloc[14, 2],
        "CONSERVA_MONT": df.iloc[15, 2],
        "OK_MONT": df.iloc[17, 3],
        "LIMP_MONT": df.iloc[18, 3],
        "ASSO_MONT": df.iloc[19, 3],
        "AFOG_MONT": df.iloc[20, 3],
        "OBS_MONT": df.iloc[21, 2],
        "TESTA_DAN_MONT": df.iloc[17, 8],
        "TUB_MONT": df.iloc[18, 8],
        "CX_MONT": df.iloc[19, 8],
        "EROSAO_MONT": df.iloc[20, 8],
        "TRINCA_MONT": df.iloc[21, 8],
        "TAMPA_DAN_MONT": df.iloc[22, 8],
        "LAT_JUS": df.iloc[7, 7],
        "LONG_JUS": df.iloc[8, 7],
        "DIM_JUS": df.iloc[11, 7],
        "LAD_JUS": df.iloc[12, 7],
        "EST_JUS": df.iloc[13, 7],
        "MAT_JUS": df.iloc[14, 7],
        "CONSERVA_JUS": df.iloc[15, 7],
        "OK_JUS": df.iloc[17, 4],
        "LIMP_JUS": df.iloc[18, 4],
        "ASSO_JUS": df.iloc[19, 4],
        "AFOG_JUS": df.iloc[20, 4],
        "OBS_JUS": df.iloc[21, 2],
        "TESTA_DAN_JUS": df.iloc[17, 9],
        "TUB_JUS": df.iloc[18, 9],
        "CX_JUS": df.iloc[19, 9],
        "EROSAO_JUS": df.iloc[20, 9],
        "TRINCA_JUS": df.iloc[21, 9],
        "TAMPA_DAN_JUS": df.iloc[22, 9],
    }
    return data

def combinar_dataframes(arquivos):
    dados = []
    for arquivo in arquivos:
        data = extrair_dados(arquivo)
        dados.append(data)
    global df_final
    df_final = pd.DataFrame(dados)

# Criar a janela principal
root = tk.Tk()
root.title("Analisador de dados")
root.geometry("400x300")

# Rótulo para identificar a seção de importação
lbl_importacao = tk.Label(root, text="Importação de Arquivos", font=("Helvetica", 12, "bold"))
lbl_importacao.pack(pady=(10, 5))

# Botão para selecionar arquivos
btn_selecionar = tk.Button(root, text="Importar arquivo", command=selecionar_arquivos)
btn_selecionar.pack(pady=5)

# Botão para selecionar pasta
btn_selecionar_pasta = tk.Button(root, text="Importar pasta", command=selecionar_pasta)
btn_selecionar_pasta.pack(pady=5)

# Rótulo para identificar a seção de análise
lbl_analise = tk.Label(root, text="Análise de Arquivos", font=("Helvetica", 12, "bold"))
lbl_analise.pack(pady=(10, 5))

# Botão para analisar arquivos
btn_analisar = tk.Button(root, text="Analisar arquivos", command=analisar_arquivos)
btn_analisar.pack(pady=5)

# Rótulo para identificar a seção de exportação
lbl_exportacao = tk.Label(root, text="Exportação de Resultados", font=("Helvetica", 12, "bold"))
lbl_exportacao.pack(pady=(10, 5))

# Botão para exportar análise
btn_exportar = tk.Button(root, text="Exportar análise", command=selecionar_diretorio)
btn_exportar.pack(pady=5)

# Label para mostrar quantos arquivos foram importados
contador_arquivos = tk.StringVar()
contador_arquivos.set("Para iniciar, importe os arquivos")
lbl_contador = tk.Label(root, textvariable=contador_arquivos)
lbl_contador.pack()

# Executar o loop principal da interface
root.mainloop()