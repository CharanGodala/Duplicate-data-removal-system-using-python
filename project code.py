import pandas as pd
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
input_file = filedialog.askopenfilename(
    title="Select file to clean",
    filetypes=[
        ("CSV files", "*.csv"),
        ("Excel files", "*.xlsx"),
        ("All files", "*.*")
    ]
)
if not input_file:
    print("No file selected.")
    exit()
if input_file.lower().endswith(".csv"):
    df = pd.read_csv(input_file)
elif input_file.lower().endswith(".xlsx"):
    df = pd.read_excel(input_file)
else:
    print("Unsupported file type.")
    exit()
df_cleaned = df.drop_duplicates()
output_file = filedialog.asksaveasfilename(
    title="Save cleaned file",
    defaultextension=".xlsx",
    filetypes=[
        ("Excel files", "*.xlsx"),
        ("CSV files", "*.csv")
    ],
    initialfile="cleaned.xlsx"
)
if not output_file:
    print("Save cancelled.")
    exit()
if output_file.lower().endswith(".csv"):
    df_cleaned.to_csv(output_file, index=False)
else:
    df_cleaned.to_excel(output_file, index=False)
print("\n================================")
print("   DUPLICATE DATA REMOVAL")
print("================================")
print("Original rows      :", len(df))
print("Cleaned rows       :", len(df_cleaned))
print("Duplicates removed :", len(df) - len(df_cleaned))
print("Cleaned file saved :", output_file)