"""Reference solution for pandas fundamentals."""
from __future__ import annotations

from io import StringIO
from pathlib import Path
from typing import Any

try:
    import pandas as pd
except ImportError:  # pragma: no cover - educational fallback
    pd = None



def load_sales_dataframe(csv_text: str) -> Any:
    sales_df = pd.read_csv(StringIO(csv_text))
    sales_df["revenue"] = sales_df["revenue"].fillna(sales_df["revenue"].median())
    return sales_df



def summarize_revenue(sales_df: Any) -> Any:
    return sales_df.groupby("region", as_index=False)["revenue"].sum()



def merge_targets(summary_df: Any, targets_df: Any) -> Any:
    merged_df = summary_df.merge(targets_df, on="region")
    merged_df["met_target"] = merged_df["revenue"] >= merged_df["target"]
    return merged_df



def export_clean_data(sales_df: Any, path: Path) -> None:
    sales_df.to_csv(path, index=False)



def run() -> None:
    if pd is None:
        print("pandas is not installed. Install it to run this solution.")
        return

    output_path = Path(__file__).parent / "clean_sales.csv"
    csv_text = """region,revenue,orders
North,1200,12
South,950,8
West,,5
"""
    targets_df = pd.read_csv(StringIO("""region,target
North,1100
South,1000
West,900
"""))

    try:
        sales_df = load_sales_dataframe(csv_text)
        summary_df = summarize_revenue(sales_df)
        merged_df = merge_targets(summary_df, targets_df)
        export_clean_data(sales_df, output_path)
        print(merged_df)
        print(f"Exported cleaned data to {output_path.name}")
    finally:
        if output_path.exists():
            output_path.unlink()


if __name__ == "__main__":
    run()
