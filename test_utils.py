from modules.data_loader import load_data
from modules.utils import *

df = load_data()

valid, message = validate_dataset(df)

print(valid)

print(message)

print(dataset_summary(df))