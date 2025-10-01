import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def spend_data():
    dates = pd.date_range(start="2024-01-01", end="2025-12-31", freq="M")

    # Simulate total spending (e.g., in USD) with some seasonality and randomness
    spending = 50000 + 10000 * np.sin(
        np.linspace(0, 3 * np.pi, len(dates))) + np.random.randint(5000, 15000,
                                                                   len(dates))

    # Simulate number of signups with a trend and noise
    signups = 200 + (np.arange(len(dates)) * 5) + np.random.randint(50, 150,
                                                                    len(dates))

    # Create dataframe
    df = pd.DataFrame({
        "spend": spending.astype(int),
        "signups": signups.astype(int)
    }, index=dates)

    df.index.name = "month"
    return df


# Example usage


if __name__ == "__main__":
    df = spend_data()
    df.plot(subplots=True)
    plt.show()