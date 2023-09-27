import pandas as pd
import glob
from tqdm import tqdm

file_paths = glob.glob(
    'C:/input/*.xlsx')  # this route for input folder excel

combined_df = pd.DataFrame()

for file_path in tqdm(file_paths, desc="Menggabungkan File Excel"):
    df = pd.read_excel(file_path)
    df = df.iloc[:, 1:]
    combined_df = pd.concat([combined_df, df], ignore_index=True)

combined_df.to_excel(
    'C:/output/file.xlsx', index=False)  # this route for Output folder excel
