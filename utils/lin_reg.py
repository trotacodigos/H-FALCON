import pandas as pd
from sklearn.linear_model import LinearRegression

def fit_and_report(df: pd.DataFrame, label: str):
    # Adjust tot_score: convert 100 -> 10
    y = df["tot_score"].replace(100, 10).values
    X = df[cols].values

    # With intercept
    with_int = LinearRegression(fit_intercept=True)
    with_int.fit(X, y)
    r2_int = with_int.score(X, y)

    # Without intercept (matches strict weighted-sum formulation)
    wo_int = LinearRegression(fit_intercept=False)
    wo_int.fit(X, y)
    r2_no = wo_int.score(X, y)

    # Print results
    print(f"\n=== {label} : Linear Regression on 9 columns -> tot_score (100→10) ===")
    print("[With intercept]")
    print(f"R^2: {r2_int:.4f}")
    print(f"Intercept: {with_int.intercept_:.6f}")
    print("Coefficients (by column):")
    for c, v in zip(cols, with_int.coef_):
        print(f"  {c:>23}: {v:.6f}")

    print("\n[Without intercept]")
    print(f"R^2: {r2_no:.4f}")
    print("Coefficients (by column):")
    for c, v in zip(cols, wo_int.coef_):
        print(f"  {c:>23}: {v:.6f}")