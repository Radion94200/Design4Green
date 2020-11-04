import pandas as pd

dfs = pd.read_csv(f"../input_bdd/data.csv", sep='\t',
                  encoding="utf-16")
print(dfs)
