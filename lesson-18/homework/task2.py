import pandas as pd

def load_iris_data():
    """
    Loads iris.json into a DataFrame, displays dataset shape and column names.
    Returns DataFrame on success, empty DataFrame on failure.
    """
    file_path = 'iris.json'
    iris_df = pd.DataFrame()

    try:
        # Load JSON data with explicit data type specification
        iris_df = pd.read_json(file_path, orient='columns')
        
        # Display dataset information
        print(f"Dataset shape: {iris_df.shape}")
        print("\nColumn names:")
        print(iris_df.columns.tolist())
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError as ve:
        print(f"JSON format error: {ve}")
    except pd.errors.EmptyDataError:
        print("Error: The JSON file is empty")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        return iris_df

if __name__ == "__main__":
    iris_data = load_iris_data()
    if not iris_data.empty:
        print("\nFirst 5 rows:")
        print(iris_data.head())