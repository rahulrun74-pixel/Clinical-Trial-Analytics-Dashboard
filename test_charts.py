from modules.data_loader import load_data
from modules.charts import age_distribution

df = load_data()

fig = age_distribution(df)

fig.show()