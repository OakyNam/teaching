"""Demonstrate basic pandas loading, grouping, merging, and plotting."""
from __future__ import annotations

from io import StringIO

try:
    import pandas as pd
except ImportError:  # pragma: no cover - educational fallback
    pd = None



def main() -> None:
    if pd is None:
        print("pandas is not installed. Install it to run this lesson example.")
        return

    sales_csv = StringIO("""region,revenue,orders
North,1200,12
South,950,8
West,,5
""")
    targets_csv = StringIO("""region,target
North,1100
South,1000
West,900
""")

    sales_df = pd.read_csv(sales_csv)
    sales_df["revenue"] = sales_df["revenue"].fillna(sales_df["revenue"].median())
    summary_df = sales_df.groupby("region", as_index=False)["revenue"].sum()
    merged_df = summary_df.merge(pd.read_csv(targets_csv), on="region")
    merged_df["met_target"] = merged_df["revenue"] >= merged_df["target"]

    print("Sales data:")
    print(sales_df)
    print("\nSummary by region:")
    print(merged_df)

    try:
        axes = merged_df.plot(
            kind="bar",
            x="region",
            y=["revenue", "target"],
            title="Revenue vs Target",
        )
        print(f"\nPlot created successfully using {type(axes).__name__}.")
    except Exception as exc:  # matplotlib may be missing in some environments
        print(f"\nPlot skipped: {exc}")


if __name__ == "__main__":
    main()
