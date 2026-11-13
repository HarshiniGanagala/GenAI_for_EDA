
"""
Generate a sample sales dataset for EDA practice.
Creates 100,000 transaction records and saves them as CSV.
"""

import pandas as pd
import numpy as np


def generate_sales_data():
    try:
        # Set random seed for reproducibility
        np.random.seed(42)

        # Number of records
        rows = 100_000

        # Sample values
        products = ["Laptop", "Mobile", "Tablet", "Headphones",
                    "Keyboard", "Mouse", "Monitor"]

        categories = ["Electronics", "Accessories", "Computers"]
        regions = ["North", "South", "East", "West", "Central"]

        # Generate dataset
        data = {
            "transaction_id": np.arange(1, rows + 1),
            "customer_id": np.random.randint(1000, 10000, rows),
            "product": np.random.choice(products, rows),
            "category": np.random.choice(categories, rows),
            "quantity": np.random.randint(1, 10, rows),
            "price": np.round(np.random.uniform(100, 50000, rows), 2),
            "date": pd.to_datetime(
                np.random.choice(
                    pd.date_range("2023-01-01", "2024-12-31"),
                    rows
                )
            ),
            "region": np.random.choice(regions, rows)
        }

        # Create DataFrame
        df = pd.DataFrame(data)

        # Calculate revenue
        df["revenue"] = df["quantity"] * df["price"]

        # Introduce missing values
        price_missing = df.sample(frac=0.05, random_state=42).index
        region_missing = df.sample(frac=0.02, random_state=21).index

        df.loc[price_missing, "price"] = np.nan
        df.loc[region_missing, "region"] = np.nan

        # Save CSV file
        df.to_csv("sales_data.csv", index=False)

        print("Sales dataset generated successfully!")
        print(f"Total records: {len(df)}")
        print(f"Total columns: {len(df.columns)}")
        print("File saved as sales_data.csv")
        print("\nDataset preview:")
        print(df.head())

        print("\nMissing values:")
        print(df.isnull().sum())

    except Exception as error:
        print(f"Error generating dataset: {error}")


if __name__ == "__main__":
    generate_sales_data()
