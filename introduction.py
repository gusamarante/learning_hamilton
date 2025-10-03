from hamilton import driver, base
import new_way
# from sample_data import spend_data
from time import time

# data = spend_data()

tic = time()
dr = (
    driver.Builder()
    # .with_config({"lookback": "short"})  # or "long"
    .with_modules(new_way)
    .with_adapters(base.PandasDataFrameResult())
    .build()
)

# outputs = ["spend", "signups", "avg_3wk_spend", "spend_per_signup", "spend_zero_mean", "spend_zero_mean_unit_variance", "acquisition_cost_rolling_mean"]
outputs = ["spend_zero_mean_unit_variance"]

# outputs = [var.name for var in dr.list_available_variables() if var.tags.get("property") == "feature"]  # Only outputs variables tagged as features
# outputs = [var.name for var in dr.list_available_variables(tag_filter={"property": "feature"})]  # Only outputs variables tagged as features
# outputs = ["acquisition_cost_rolling_mean_short", "acquisition_cost_rolling_mean_long"]

# input_dict = data.to_dict(orient="series")


dr.visualize_execution(
    final_vars=outputs,
    # inputs=input_dict,
    deduplicate_inputs=True,
    overrides=None,
    output_file_path="dag_executed.svg",
)



result = dr.execute(
  outputs,
  # inputs=input_dict
)
print(result.to_string())
print(f"New way took {time()-tic: 0.2f} seconds")