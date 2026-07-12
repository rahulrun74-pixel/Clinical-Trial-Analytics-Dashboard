from modules.data_loader import load_data
from modules.insights import generate_insights

df = load_data()

insights = generate_insights(df)

for item in insights:
    print(item)