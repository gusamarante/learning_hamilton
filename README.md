# learning_hamilton
My studies on the hamilton library

Although code in Hamilton is more verbose, it is much modular and easier to 
document.

The authors consider the verbosity a feature, it makes the code easier to 
understand and maintain in the long-term. Code complexity comes with the need 
of verbosity. The advantage is that it is all implemented in plain Python.

# Functions / DAGs

1. The **name** of a hamilton functions corresponds to a queriable artifact (dataframe/column/scalar/python object).
2. The **parameters** of the hamilton function specify which dependencies (other functions) it refers to

This means that a sequence of python functions are interpreted by Hamilton as 
a DAG ("flowcharts" or "pipelines" or "dataflows" or "workflows" or "ETLs").



