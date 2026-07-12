from modules.data_loader import load_data, get_dataset_info

df = load_data()

print(df.head())

print()

print(get_dataset_info(df))