# 07 - Pandas Fundamentals
## Overview
Learn core pandas workflows for loading, inspecting, cleaning, and summarizing tabular data.
## Learning Goals
- Load CSV data into DataFrames.
- Filter, transform, and aggregate data.
- Export cleaned data safely.
## Core Example
```python
import pandas as pd
df = pd.read_csv("sales.csv")
summary = df.groupby("region")["revenue"].sum().reset_index()
print(summary)
```
## Exercises
1. Select rows where revenue is above a threshold.
2. Fill missing values in one numeric column.
3. Export transformed data to `output.csv`.
---
## Answer Key
1. Use boolean indexing, e.g. `df[df["revenue"] > 1000]`.
2. Use `fillna` with a chosen strategy.
3. Use `to_csv("output.csv", index=False)`.
---
⬅️ Previous: [06 - Testing and Debugging](./06_testing_debugging.md)
➡️ Next: [08 - pexpect Automation](./08_pexpect_automation.md)
