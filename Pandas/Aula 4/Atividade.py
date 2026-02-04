# Missão 1: Configuração Inicial

import pandas as pd
import numpy as np
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

dados_original = pd.read_excel("dados_clinica.xlsx", engine="openpyxl")
dados = dados_original.copy()

print("Colunas do DataFrame:")
print(dados.columns)
