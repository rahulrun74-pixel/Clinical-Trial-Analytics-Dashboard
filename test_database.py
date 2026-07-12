from modules.data_loader import load_data
from modules.database import *

df = load_data()

create_database()

save_dataframe(df)

print("Rows Saved :", row_count())

loaded = load_dataframe()

print(loaded.head())

print("Database Exists :", database_exists())