
"""
Launch an interactive D-Tale EDA dashboard
using the sales dataset.
"""

import os
import pandas as pd
import dtale


def main():
    try:
        # Load sales dataset
        file_path = "sales_data.csv"

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )

        print("Loading sales dataset...")

        df = pd.read_csv(file_path)

        print("Dataset loaded successfully!")
        print("Rows:", len(df))
        print("Columns:", df.columns.tolist())

        # Launch D-Tale dashboard
        print("\nLaunching D-Tale dashboard...")

        d = dtale.show(df, host="127.0.0.1", port=40000)

        print("D-Tale launched successfully!")
        print("Open this URL in your browser:")
        print(d._main_url)

        # Keep the dashboard running
        input("\nPress Enter to stop D-Tale...")

        d.kill()
        print("D-Tale stopped.")

    except FileNotFoundError as e:
        print("File error:", e)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
