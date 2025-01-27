import pandas as pd
tx_ex = pd.read_csv("/Users/jesusdavila/Documents/Notre Dame Spring 25/Unstructured Data Analytics/Notes/last_statements.csv")

print(tx_ex.loc[0, 'statements'])

for i, statement in enumerate(tx_ex['statements'].head(3), start=1):
    print(f"Statement {i}: {statement}\n")

