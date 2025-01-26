import sqlite3
import pandas as pd

def load_customers_data():
    """
    Connects to chinook.db, reads customers table into a DataFrame,
    and displays the first 10 rows with proper error handling.
    """
    database_path = 'chinook.db'
    customers_dataframe = None

    try:
        # Establish database connection using context manager
        with sqlite3.connect(database_path) as database_connection:
            # SQL query to select all customer records
            customers_query = "SELECT * FROM customers"
            
            # Read SQL query results into DataFrame
            customers_dataframe = pd.read_sql_query(customers_query, database_connection)
            
            # Display first 10 rows using formatted output
            print("First 10 rows of customers table:")
            print(customers_dataframe.head(10))
            
    except sqlite3.Error as database_error:
        print(f"Database error occurred: {database_error}")
    except FileNotFoundError:
        print(f"Database file not found at: {database_path}")
    except Exception as unexpected_error:
        print(f"An unexpected error occurred: {unexpected_error}")
    finally:
        if customers_dataframe is not None:
            return customers_dataframe
        return pd.DataFrame()  # Return empty DataFrame on failure

if __name__ == "__main__":
    customers_df = load_customers_data()