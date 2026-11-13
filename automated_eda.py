
"""
Automated Exploratory Data Analysis using Pandas,
YData Profiling and Sweetviz.
"""

import sys
from pathlib import Path

import pandas as pd
import sweetviz as sv
import ydata_profiling
from packaging.version import Version
from ydata_profiling import ProfileReport


# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "sales_data.csv"
REPORT_DIR = BASE_DIR / "reports"


def verify_libraries():
    """Verify required library versions."""
    print("\nChecking library versions...")

    print("Python:", sys.version.split()[0])
    print("Pandas:", pd.__version__)
    print("YData Profiling:", ydata_profiling.__version__)
    print("Sweetviz:", sv.__version__)

    if Version(pd.__version__) < Version("2.0.0"):
        raise RuntimeError("Pandas 2.0.0 or higher is required.")

    if Version(ydata_profiling.__version__) < Version("4.6.0"):
        raise RuntimeError("YData Profiling 4.6.0 or higher is required.")

    if Version(sv.__version__) < Version("2.3.0"):
        raise RuntimeError("Sweetviz 2.3.0 or higher is required.")

    print("All library versions are compatible!")


def load_dataset():
    """Load the sales CSV dataset."""
    print("\nLoading sales dataset...")

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    if "revenue" not in df.columns:
        raise ValueError("The dataset must contain a 'revenue' column.")

    print("Dataset loaded successfully!")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    return df


def generate_ydata_report(df):
    """Generate and save the YData Profiling report."""
    print("\nGenerating YData Profiling report...")

    profile = ProfileReport(
        df,
        title="Sales Data EDA Report",
        minimal=True
    )

    report_path = REPORT_DIR / "ydata_report.html"
    profile.to_file(report_path)

    print("YData report saved:", report_path)


def generate_sweetviz_report(df):
    """Generate and save the Sweetviz report."""
    print("\nGenerating Sweetviz report...")

    report = sv.analyze(df, target_feat="revenue")

    report_path = REPORT_DIR / "sweetviz_report.html"
    report.show_html(
        filepath=str(report_path),
        open_browser=False
    )

    print("Sweetviz report saved:", report_path)


def main():
    """Run the complete automated EDA workflow."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    verify_libraries()

    df = load_dataset()

    generate_ydata_report(df)

    generate_sweetviz_report(df)

    print("\nAutomated EDA completed successfully!")


if __name__ == "__main__":
    main()
