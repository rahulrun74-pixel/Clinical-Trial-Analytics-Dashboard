from modules.data_loader import load_data
from modules.report import *

df = load_data()

print(export_csv(df))

print(export_excel(df))

print(export_pdf(df))