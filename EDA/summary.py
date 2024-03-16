# Import modules
import os
import time
import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
import seaborn as sns

# Define constants
DATE_FORMAT = "%d-%m-%Y"
INPUT_DIR = '../ETL/output/'
OUTPUT_DIR = 'output/'
SALES_FILE_PREFIX = 'ventas_integra'
SALES_FILE_EXT = '.xlsx'


# Start timer
start = time.time()

# Get list of files in input directory
files = os.listdir(INPUT_DIR)

# Filter files by prefix and extension
sales_df = [file for file in files if file.startswith(
    SALES_FILE_PREFIX) and file.endswith(SALES_FILE_EXT)]

# Get the newest file for each category by modification date
newest_sales_file = max(
    sales_df, key=lambda f: os.path.getmtime(INPUT_DIR + f))

# Import files to dataframes
sales_df = pd.read_excel(INPUT_DIR + newest_sales_file,
                         thousands=',', decimal='.')



sales_df.columns


SELECTED_VARS: list = ['Campaña','Cantidad', 'Costo Unitario Integra',
       'Costo Unitario Recepcion', 'Costo Total Integra',
       'Costo Total Recepcion', 'Tasa', 'Precio Unitario',
       'Precio Unitario Tasa', 'Dif Venta Unitaria', 'Total Venta',
       'Total Venta Tasa', 'Dif Venta Total', 'Margen Bruto Integra']

sales_df[SELECTED_VARS].drop('Campaña', axis=1).corr().T

sns.pairplot(sales_df[SELECTED_VARS], hue='Campaña')
plt.suptitle('Pairplot de variables seleccionadas', y=1.02)
plt.show()

print(f'{(time.time() - start)} seg')