import pandas as pd

df = pd.read_csv("Newcastle Data Challenge Dataset.xlsx - Sheet1.csv")

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-z0-9_]", "", regex=True)
)

print("Cleaned columns:", df.columns.tolist())

print(df.isnull().sum())

if "club" in df.columns:
    df["club"] = df["club"].astype(str).str.strip().replace({"Nan": None})
    df["club"] = df["club"].fillna("Unknown")

if "gender" in df.columns:
    df["gender"] = df["gender"].astype(str).str.strip().str.title().fillna("Unknown")

if "first_name" in df.columns:
    df["first_name"] = df["first_name"].astype(str).str.strip().str.title()

numeric_columns = ["age", "vo2_max", "bmi", "n_marathons_run", "cadence"]

df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

df["has_trainer"] = df["has_trainer"].apply(lambda x: 1 if x == 1 else 0)

if {"id", "first_name"}.issubset(df.columns):
    df = df.drop_duplicates(subset=["id", "first_name"], keep="first")

df = df[(df["age"] > 10) & (df["age"] < 100)]
df = df[(df["bmi"] > 10) & (df["bmi"] < 60)]
df = df[(df["vo2_max"] > 10) & (df["vo2_max"] < 90)]

df.to_csv("cleaned_newcastle_dataset.csv", index=False)

print("Cleaned dataset saved to cleaned_newcastle_dataset.csv")
print(df.info())
print(df.head())
