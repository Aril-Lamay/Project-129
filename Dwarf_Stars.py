import pandas as pd
import csv

df = pd.read_csv("Dwarf_stars.csv")
df = df.dropna()
df["Mass"] = pd.to_numeric(df["Mass"], downcast= "float")
df["Radius"] = pd.to_numeric(df["Radius"], downcast= "float")

df["Radius"] = df["Radius"].apply(lambda r:r*0.102763)
df["Mass"] = df["Mass"].apply(lambda x:x*0.000954588)

df.to_csv("New_Dwarf_Stars.csv")