import pandas as pd
import numpy as np
from hamilton.function_modifiers import config, check_output, tag, parameterize, value, extract_columns

@extract_columns(*["spend", "signups"])
def spend_data() -> pd.DataFrame:
    """Generate sample spend and signup data."""
    dates = pd.date_range(start="2024-01-01", end="2025-12-31", freq="M")

    # Simulate total spending (e.g., in USD) with some seasonality and randomness
    spending = 50000 + 10000 * np.sin(np.linspace(0, 3 * np.pi, len(dates))) + np.random.randint(5000, 15000, len(dates))

    # Simulate number of signups with a trend and noise
    signups = 200 + (np.arange(len(dates)) * 5) + np.random.randint(50, 150, len(dates))

    # Create dataframe
    df = pd.DataFrame({
        "spend": spending.astype(int),
        "signups": signups.astype(int)
    }, index=dates)

    df.index.name = "month"
    return df

@tag(property="feature")
def avg_3wk_spend(spend: pd.Series) -> pd.Series:
  """Rolling 3 day average spend."""
  return spend.rolling(3).mean()

# @check_output(
#   importance="warn",
#   data_type=float,
#   range=(0,1),
# )
@tag(property="feature")
def spend_per_signup(spend: pd.Series, signups: pd.Series) -> pd.Series:
  """The cost per signup in relation to spend."""
  return spend / signups

def acquisition_cost_rolling_mean(spend: pd.Series) -> pd.Series:
  """Rolling 7 day average spend."""
  return spend.rolling(window=7,min_periods=1).mean()

# @config.when(lookback="short")
# def acquisition_cost_rolling_mean__short(spend: pd.Series) -> pd.Series:
#   """Rolling 3 day average spend."""
#   return spend.rolling(window=3, min_periods=1).mean()
#
# @config.when(lookback="long")
# def acquisition_cost_rolling_mean__long(spend: pd.Series) -> pd.Series:
#   """Rolling 7 day average spend."""
#   return spend.rolling(window=7,min_periods=1).mean()

@parameterize(
    acquisition_cost_rolling_mean_none={"window": value(1)},
    acquisition_cost_rolling_mean_short={"window": value(3)},
    acquisition_cost_rolling_mean_medium={"window": value(5)},
    acquisition_cost_rolling_mean_long={"window": value(7)}
)
def acquisition_cost_rolling_mean_base(spend: pd.Series, window: int) -> pd.Series:
  """Rolling {window} day average spend."""
  return spend.rolling(window=window).mean()

def spend_mean(spend: pd.Series) -> float:
  """Shows function creating a scalar. In this case it computes the mean of the entire column."""
  return spend.mean()


def spend_zero_mean(spend: pd.Series, spend_mean: float) -> pd.Series:
  """Shows function that takes a scalar. In this case to zero mean spend."""
  return spend - spend_mean


def spend_std_dev(spend: pd.Series) -> float:
  """Function that computes the standard deviation of the spend column."""
  return spend.std()


@tag(property="feature")
def spend_zero_mean_unit_variance(spend_zero_mean: pd.Series, spend_std_dev: float) -> pd.Series:
  """Function showing one way to make spend have zero mean and unit variance."""
  return spend_zero_mean / spend_std_dev