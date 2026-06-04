import pandas as pd


def basic_info(df):

    print("="*50)

    print(df.info())

    print("="*50)

    print(df.describe(include="all"))


def missing_values(df):

    missing = pd.DataFrame(
        {
            "missing_count": df.isnull().sum(),
            "missing_pct": round(
                df.isnull().mean()*100,
                2
            )
        }
    )

    return missing.sort_values(
        "missing_pct",
        ascending=False
    )


def unique_counts(df):

    unique_df = pd.DataFrame(
        {
            "column": df.columns,
            "nunique": [
                df[col].nunique()
                for col in df.columns
            ]
        }
    )

    return unique_df