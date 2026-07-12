from modules.data_loader import load_data
from modules.cleaner import clean_data, dataset_quality

df = load_data()

print("Before Cleaning")
print(dataset_quality(df))

df = clean_data(df)

print("\nAfter Cleaning")
print(dataset_quality(df))