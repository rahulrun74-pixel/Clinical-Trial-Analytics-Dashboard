from modules.data_loader import load_data
from modules.prediction import train_models

df = load_data()

results = train_models(df)

print(results["metrics"])