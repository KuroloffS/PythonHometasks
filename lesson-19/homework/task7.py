import sqlite3
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc

# Step 1: Connect to the Chinook database
try:
    conn = sqlite3.connect("chinook.db")
except sqlite3.Error as e:
    raise ConnectionError(f"Failed to connect to the database: {e}")

# Step 2: Load the employees table into a DataFrame
try:
    query = "SELECT * FROM employees"
    employees_df = pd.read_sql_query(query, conn)
except Exception as e:
    raise RuntimeError(f"Failed to load employees table: {e}")
finally:
    conn.close()

# Step 3: Data validation
required_columns = ["EmployeeId", "ReportsTo", "Salary"]
missing_columns = [col for col in required_columns if col not in employees_df.columns]
if missing_columns:
    raise ValueError(f"The following required columns are missing: {missing_columns}")

# Step 4: Efficiently normalize salaries within each department
try:
    # Replace missing ReportsTo values with a placeholder (-1)
    employees_df["ReportsTo"].fillna(-1, inplace=True)

    # Convert the DataFrame to a PyArrow Table for efficient computation
    table = pa.Table.from_pandas(employees_df)

    # Group by 'ReportsTo' and normalize the 'Salary'
    grouped = table.group_by(["ReportsTo"])
    normalized = grouped.apply(lambda group: group.set_column(
        group.schema.get_field_index("Salary"),  # Index of 'Salary' column
        "Salary",
        pc.normalize(group["Salary"], pc.min_max_scale())  # Normalize using Min-Max scaling
    ))

    # Convert the normalized PyArrow Table back to a pandas DataFrame
    normalized_df = normalized.to_pandas()
except Exception as e:
    raise RuntimeError(f"Failed to normalize salaries: {e}")

# Step 5: Save the normalized DataFrame back to the database
try:
    conn = sqlite3.connect("chinook.db")
    normalized_df.to_sql("normalized_employees", conn, if_exists="replace", index=False)
    print("Normalized salaries have been successfully saved to the 'normalized_employees' table.")
except Exception as e:
    raise RuntimeError(f"Failed to save normalized salaries: {e}")
finally:
    conn.close()

# Documentation
"""
Steps:
1. Load the Chinook database and extract the 'employees' table.
2. Validate that required columns ('EmployeeId', 'ReportsTo', 'Salary') exist.
3. Replace missing values in 'ReportsTo' with -1.
4. Normalize salaries within each department (grouped by 'ReportsTo') using PyArrow's efficient computation methods.
5. Save the normalized DataFrame back into the database as 'normalized_employees'.

Dependencies:
- sqlite3: For database interaction.
- pandas: For data manipulation.
- pyarrow: For efficient columnar data processing and normalization.
"""
