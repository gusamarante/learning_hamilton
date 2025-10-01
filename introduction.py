from hamilton import driver, base
import new_way
from sample_data import spend_data
from time import time

data = spend_data()

tic = time()
dr = (
    driver.Builder()
    .with_modules(new_way)
    .with_adapters(base.PandasDataFrameResult())
    .build()
)

outputs = ["spend", "signups", "avg_3wk_spend", "spend_per_signup", "spend_zero_mean", "spend_zero_mean_unit_variance"]

input_dict = data.to_dict(orient="series")


dr.visualize_execution(
    final_vars=outputs,
    inputs=input_dict,
    deduplicate_inputs=True,
    overrides=None,
    output_file_path="dag_executed.svg",
)



result = dr.execute(
  outputs,
  inputs=input_dict
)
print(result.to_string())
print(f"New way took {time()-tic: 0.2f} seconds")