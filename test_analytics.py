from modules.data_loader import load_data
from modules.analytics import calculate_metrics

df = load_data()

metrics = calculate_metrics(df)

for key, value in metrics.items():
    print(key, ":", value)